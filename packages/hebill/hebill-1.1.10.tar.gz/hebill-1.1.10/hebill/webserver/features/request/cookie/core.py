class Cookie(dict):
    def __init__(self, data: dict = None):
        super().__init__()
        if data is not None:
            self.update(data)

    def id(self): return self.get('id', None)

