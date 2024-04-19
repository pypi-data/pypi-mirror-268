from ..client.core import Client
from ..request.core import Request


class WebSite:
    def __init__(self):
        self._clients = {}
        pass

    @property
    def clients(self): return self._clients

    def response(self, request: Request):
        if self.clients.get(request.cookie.id()) is None:
            self.clients[request.cookie.id()] = Client(request.cookie.id())
            # TODO 添加相关客户端信息
        return 'Hello World!'
