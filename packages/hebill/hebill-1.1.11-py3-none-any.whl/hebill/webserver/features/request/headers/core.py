class Headers(dict):
    def __init__(self, data: dict = None):
        super().__init__()
        if data is not None:
            self.update(data)

    @property
    def host(self): return self.get('Host')

