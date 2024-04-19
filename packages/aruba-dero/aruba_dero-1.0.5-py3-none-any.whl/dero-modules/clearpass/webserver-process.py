import http.server
import os
import socketserver
import argparse

parser = argparse.ArgumentParser(description="Temporary Webserver for CPPM",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("addr", help="Webserver Bind Address", type=str)
parser.add_argument("port", help="Webserver Port", type=int)
parser.add_argument("-D", "--root-dir", help="Webserver Root Dir", type=str)
args = parser.parse_args()
config = vars(args)

root_dir = os.path.abspath(config.get("root_dir"))
server_hostname, server_address = 'localhost', config.get("addr")
server_port = config.get("port")


def dir_exists_non_empty(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"Directory {path} does not exist")
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"{path} is not a directory")
    if not os.listdir(path):
        raise argparse.ArgumentTypeError(f"{path} is empty")
    return path


def start_server():
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(root_dir)

    with socketserver.TCPServer((server_address, server_port), handler) as httpd:
        print(f"Serving {root_dir}: http://{server_address}:{server_port}")
        httpd.serve_forever()


dir_exists_non_empty(root_dir)
start_server()
