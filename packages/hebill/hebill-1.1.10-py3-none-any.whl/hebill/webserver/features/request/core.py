from .get.core import Get
from .post.core import Post
from .cookie.core import Cookie


class Request:
    def __init__(self, cookie: dict = None, get: dict = None, post: dict = None, headers: dict = None):
        self._cookie = Cookie(cookie)
        self._get = Get(get)
        self._post = Post(post)
        self._headers = Post(headers)

    @property
    def cookie(self): return self._cookie

    @property
    def get(self): return self._get

    @property
    def post(self): return self._post

    @property
    def headers(self): return self._headers
