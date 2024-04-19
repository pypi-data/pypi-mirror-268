import os
from .features.handle.core import Handle
from http.server import HTTPServer


class WebServer:
    def __init__(self, host: str = '', port: int = 8000, root: str = None):
        self._handle = Handle
        self._host = host
        self._port = port
        self._server = None
        self._root = root if root else os.getcwd()

    @property
    def handle(self): return self._handle

    @property
    def host(self) -> str: return self._host

    @property
    def port(self) -> int: return self._port

    @property
    def server(self) -> HTTPServer:
        if self._server is None:
            self._server = HTTPServer((self.host, self.port), self.handle)
        return self._server

    def start(self):
        print(f'服务器开始运行')
        print(f'- http://127.0.0.1:{self.port}')
        print(f'- http://localhost:{self.port}')
        from ..sys import Sys
        ips = Sys.local_ips()
        for ip in ips:
            print(f'- http://{ip}:{self.port}')
        if self.host:
            print(f'服务器开始运行：{self.host if self.host else '<all>'}:{self.port}')
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print(f'服务器已经停止工作')
            pass

    def close(self):
        self.server.server_close()
