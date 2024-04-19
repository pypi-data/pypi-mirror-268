class Client(dict):
    def __init__(self, cid):
        super().__init__()
        self. _id = cid

    def id(self): return self._id

