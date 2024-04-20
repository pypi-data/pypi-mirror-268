import errno
import os
import subprocess


class TemporaryWebServer:
    def __init__(self, port: int = 8080, host: str = "127.0.0.1", serv_dir: str = ""):
        self.port = port
        self.host = host
        self.serv_dir = serv_dir
        self.process: subprocess.Popen[bytes] | None = None
        pass

    def __enter__(self):
        self.process = self.start_webserver()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop_webserver()

    def start_webserver(self) -> subprocess.Popen[bytes] | None:
        if self.serv_dir is None:
            return None
        try:
            webserver_exec_path = os.path.join(os.path.dirname(__file__), "webserver-process.py")
            process = subprocess.Popen(["python", f"{webserver_exec_path}", f"{self.host}", f"{self.port}", "-D", f"{self.serv_dir}"],
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL)
            return process
        except OSError as e:
            if e.errno == errno.EADDRINUSE:
                print(f"Port {self.port} already in use. Incrementing..")
                self.port += 1
                self.start_webserver()
            else:
                print(f"Failed to start webserver: {e}")
        return None

    def stop_webserver(self):
        if self.process:
            try:
                self.process.kill()
            except ProcessLookupError as e:
                return
