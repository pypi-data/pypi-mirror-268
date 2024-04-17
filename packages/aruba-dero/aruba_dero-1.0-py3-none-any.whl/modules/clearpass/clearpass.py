import os
import pathlib
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from getpass import getpass

from bullet import Check, colors, Input, Bullet
from pyclearpass import *

import utils as utils
from Module import Module
from .utils import *
from .temp_webserver import TemporaryWebServer


class ClearPassModule(Module):
    def __init__(self):
        # Api
        super().__init__()
        self.api_host: str | None = None  # E.g. https://clearpass.example.com:8080
        self.client_id: str | None = None
        self.client_access_token: str | None = None
        self.verify_ssl: bool = True
        self.client_secret: str | None = None
        self.login = None
        # Webserver
        self.bind_addr: str = "127.0.0.1"
        self.bind_port: int = 8080
        self.serve_dir: str = "cppmCerts"
        # Preparation & Execution
        self.supported_server_certificates: list[str] = ["HTTPS(ECC)", "HTTPS(RSA)", "RADIUS"]
        self.servers: list[any] | None = None
        self.certificate: Certificate | None = None
        self.cert_is_pkcs12 = False  # Indicating that a pkcs12 file was loaded, so no additional key file is needed
        self.passphrase: str | None = None
        self.server_certificate_type: str | None = None  # One of supported_server_certificates
        # Other
        self.run_retries: int = 0

    def setup(self):
        parser = ArgumentParser(description="Update certificate on ClearPass server",
                                formatter_class=ArgumentDefaultsHelpFormatter)
        parser.add_argument("--insecure", help="Ignore SSL Verification", action="store_true")
        args = parser.parse_args()
        config = vars(args)

        self.api_host = os.environ.get("CPPM_CERT_API_HOST") or self.ask_api_host()
        self.verify_ssl = os.environ.get("CPPM_CERT_VERIFY_SSL") or not config.get('insecure')
        self.client_id = os.environ.get("CPPM_CERT_CLIENT_ID")
        self.client_secret = os.environ.get("CPPM_CERT_CLIENT_SECRET")
        self.client_access_token = os.environ.get("CPPM_CERT_API_TOKEN")

        self.serve_dir = os.environ.get("CPPM_CERT_SERVE_DIR") or self.serve_dir
        return True

    def ask_api_host(self) -> str:
        if not self.api_host:
            print("No API host provided.")
            return Input("Enter Api Host: ", default="https://127.0.0.1:443", word_color=colors.foreground["yellow"]).launch()
        return self.api_host

    def has_credentials(self) -> bool:
        return bool(self.client_id and self.client_secret) or bool(self.client_access_token)

    def ask_credentials(self):
        if self.client_id:
            print(f"Client ID found: {self.client_id}")
            self.client_secret = getpass(prompt="Please enter client secret: ", stream=None)
        else:
            self.client_access_token = getpass(prompt="Enter client access token: ", stream=None)
        return self.client_access_token or self.client_secret

    def pre_run(self):
        if self.client_access_token:
            self.login = ClearPassAPILogin(server=f"{self.api_host}/api",
                                           api_token=f"{self.client_access_token}",
                                           verify_ssl=self.verify_ssl)
        else:
            self.login = ClearPassAPILogin(server=f"{self.api_host}/api",
                                           granttype="client_credentials",
                                           clientsecret=f"{self.client_secret}", clientid=f"{self.client_id}",
                                           verify_ssl=self.verify_ssl)
        if not self.test_login():
            return False

        print("Retrieving cluster servers...")
        servers = self.collect_cluster_servers()
        self.select_servers(servers)
        if len(self.servers) == 0:
            print("No servers selected. Exiting...")
            return False

        # Check if the certificate is already installed
        self.check_current_certificates()

        # Prompt user to select network interface to bind webserver to
        self.select_bind_address()

        # Make sure the root directory exists and is not empty
        return self.prepare_srv_directory()

    def run(self):
        certificate_file = utils.cli_file_picker("Select the certificate: ", root_path=self.serve_dir,
                                                 current_path=self.serve_dir)
        if certificate_file is None:
            print("Cannot select file. Exiting...")
            return False

        # Check if the selected file is a valid certificate file / PEM/DER
        _, certificate = check_cert_and_convert_to_pem(certificate_file)
        if not certificate:
            # Check for PKCS12 file
            print("Selected file might be a PKCS12 file. Please provide the passphrase. Press Enter to skip.")
            self.passphrase = getpass(prompt="Enter passphrase: ", stream=None)
            _, certificate = pkcs12_to_pem(certificate_file, self.passphrase)

            if not certificate:
                print("\nInvalid certificate file or wrong passphrase. Try again.")
                self.retry()
            else:
                print("PKCS12 file loaded successfully.")
                #todo grab key format
                self.cert_is_pkcs12 = True

        self.reset_retries()
        self.certificate = certificate

        if not self.cert_is_pkcs12:
            key_file = utils.cli_file_picker("Select the certificate key: ", root_path=self.serve_dir,
                                             current_path=self.serve_dir)
            _, private_key = check_key_and_convert_to_pem(key_file)

            if not private_key:
                print("Invalid key file. Try again.")
                self.retry()

            if not private_key.public_key() == self.certificate.public_key():
                print("Certificate and key do not match. Try again.")
                self.retry()

            print("Certificate and key match.")
            print("Bundling into PKCS12 file...")

            if not self.passphrase:
                print("Creating PKCS12 file. Please provide the passphrase.")
                self.passphrase = getpass(prompt="Enter passphrase: ", stream=None)

            _, p12_data = bundle_pkcs12(self.certificate, private_key, self.passphrase)

            p12_file = f"{os.path.splitext(certificate_file)[0]}.p12"
            with open(p12_file, "wb") as file:
                file.write(p12_data)
            key_file = p12_file

            if isinstance(private_key, RSAPrivateKey):
                self.supported_server_certificates.remove("HTTPS(ECC)")
            elif isinstance(private_key, EllipticCurvePrivateKey):
                self.supported_server_certificates.remove("HTTPS(RSA)")

        else:
            key_file = certificate_file

        self.select_certificate_type()

        if not self.servers:
            print("No servers selected. Aborting...")
            return False

        with TemporaryWebServer(self.bind_port, self.bind_addr, self.serve_dir) as webserver:

            if not webserver.process:
                print("Failed to start webserver. Exiting...")
                return False

            if webserver.host == "0.0.0.0":

                webhost = os.environ.get("CPPM_CERT_SERVE_HOST") or Input("Enter host ip: ", default=f"{utils.get_net_ifaces()[-1].get("ip4")}", word_color=colors.foreground["yellow"]).launch()
                webhost += f":{webserver.port}"
            else:
                webhost = f"https://{webserver.host}:{webserver.port}"

            print(f"Serving on http://{webserver.host}:{webserver.port}...")

            body = {
                "certificate_url": f"http://{webhost}/{pathlib.PurePath(os.path.relpath(certificate_file, start=self.serve_dir)).as_posix()}",
                "pkcs12_file_url": f"http://{webhost}/{pathlib.PurePath(os.path.relpath(key_file, start=self.serve_dir)).as_posix()}",
                "pkcs12_passphrase": f"{self.passphrase}",
            }

            if not self.server_certificate_type:
                print("No certificate type selected. Aborting...")
                return False

            for server in self.servers:
                res = ApiPlatformCertificates.replace_server_cert_name_by_server_uuid_service_name(self.login,
                                                                                                   server_uuid=server[
                                                                                                       'server_uuid'],
                                                                                                   service_name=self.server_certificate_type,
                                                                                                   body=body)
                if res.get("status") and res["status"] != 200:
                    print(
                        f"Failed to update certificate on {server.get("name")}: {res.get("status")} {res.get("title")}: {res.get("validation_messages")}")
                    print("\n!!This module is not performing a rollback. Please check the server manually!!")
                    print("!!This module is not performing a rollback. Please check the server manually!!")
                    print("!!This module is not performing a rollback. Please check the server manually!!\n")
                    return False
                else:
                    print(f"Updated certificate on {server.get("name")} successfully. Expiring at {res.get("expiry_date")}")
                    # Todo. maybe add link to download ics to renew in time?
        return True

    def post_run(self):
        return True

    def test_login(self) -> bool:
        print("\nTrying to login...")
        try:
            res = ApiApiOperations.get_oauth_me(self.login)
            if res.get('status') or not res.get('info'):
                print(f"Failed to login: {res.get("status")}: {res.get("detail")}")
                return False
            print(f"Logged in as {res.get("info")}")
            return True
        except Exception as e:
            print(f"Failed to login: {e}")
            return False

    def collect_cluster_servers(self):
        # Collect all instances managed on api host
        cluster_res = ApiLocalServerConfiguration.get_cluster_server(self.login)
        # TODO: Response Validation, maybe json schema?
        servers = []
        for item in cluster_res['_embedded']['items']:
            servers.append({"server_uuid": item.get("server_uuid"), "name": item.get("name"), "fqdn": item.ger("fqdn")})
        return servers

    def select_certificate_type(self) -> str:
        choices = self.supported_server_certificates
        if len(choices) == 1:
            return choices[0]

        cli = Bullet(
            prompt="Select certificate type to update:",
            choices=choices,
            indent=0,
            align=5,
            margin=2,
            bullet="*",
            bullet_color=colors.bright(colors.foreground["cyan"]),
            word_color=colors.bright(colors.foreground["yellow"]),
            word_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["black"],
            pad_right=5,
            return_index=True
        )
        cert_type = cli.launch()
        self.server_certificate_type = choices[cert_type[1]]

    def select_servers(self, all_servers: list) -> None:
        choices = [f"{server.get("name")}-{server.get("fqdn")}" for server in all_servers]
        cli = Check(
            prompt="Select servers to update certificates:",
            choices=choices,
            check="*",
            margin=2,
            check_color=colors.bright(colors.foreground["yellow"]),
            check_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["white"],
            word_color=colors.foreground["white"],
            word_on_switch=colors.foreground["black"],
            return_index=True
        )
        servers = cli.launch()
        self.servers = [all_servers[i] for i in servers[1]]

    def select_bind_address(self) -> None:
        # Get available network interfaces
        available_ifaces = utils.get_net_ifaces()
        available_ifaces.append({"name": "‼ All interfaces ‼", "ip4": "0.0.0.0", "ip6": "::"})

        # Select network interface to bind webserver to
        cli = Bullet(
            prompt="Select network interface to bind the webserver to:",
            choices=[f"{iface.get('name') or 'Unknown'} : {iface.get('ip4')} - {iface.get('ip6')}" for iface in
                     available_ifaces],
            indent=0,
            align=5,
            margin=2,
            bullet="*",
            bullet_color=colors.bright(colors.foreground["cyan"]),
            word_color=colors.bright(colors.foreground["yellow"]),
            word_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["black"],
            pad_right=5,
            return_index=True
        )
        selected_iface = cli.launch()

        selected_iface = available_ifaces[selected_iface[1]]
        bind_addr = selected_iface.get('ip4') or "0.0.0.0"

        bind_port = Input("Enter bind port: ", default="8080", word_color=colors.foreground["yellow"]).launch()
        self.bind_addr = bind_addr
        self.bind_port = bind_port

    def prepare_srv_directory(self) -> bool:
        print("\n")
        if not os.path.exists(self.serve_dir):
            os.mkdir(self.serve_dir)
            print(f"Created directory: {self.serve_dir}")
        if len(os.listdir(self.serve_dir)) == 0:
            print(f"Directory {self.serve_dir} is empty.")
            print("Please place the certificate and key files in the directory and press Enter to continue.")
            try:
                input("Press Enter to continue...")
            except EOFError:
                pass
            if len(os.listdir(self.serve_dir)) == 0:
                print("Still no files found.")
                return False
        return True

    def check_current_certificates(self) -> None:
        print("\nChecking current certificates...")
        for server in self.servers:
            server_uuid = server.get("server_uuid")
            for cert_type in self.supported_server_certificates:
                res = ApiPlatformCertificates.get_server_cert_name_by_server_uuid_service_name(self.login,
                                                                                               server_uuid=server_uuid,
                                                                                               service_name=cert_type)
                pass  # todo check current certificate

    def retry(self):
        allowed = self.run_retries < 3
        if allowed:
            self.run_retries += 1
            return self.run()
        return False

    def reset_retries(self):
        self.run_retries = 0
