import decimal
from ..string.core import String


class Dimensions(dict):
    names = []

    def __init__(self, dimensions: dict = None):
        super().__init__()
        if dimensions is not None:
            for key in self.names:
                if key in dimensions:
                    self.__setitem__(key, dimensions[key])
        for key in self.names:
            if key not in self.keys():
                self.__setitem__(key, None)
        self._error = ''

    def __setitem__(self, key, value):
        if key in self.names:
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, decimal.Decimal):
                if value >= 0:
                    super().__setitem__(key, value)
                else:
                    self._error = f'Value {value} is negative, not allowed.'
            elif isinstance(value, str):
                num = String(value)
                if num.digitalizable():
                    if num.digitize() < 0:
                        super().__setitem__(key, num.digitize())
                    else:
                        self._error = f'Value {value} is negative, not allowed.'
                else:
                    self._error = f'Value of {value} is string, but nor not digitalizable.'
            elif value is None:
                super().__setitem__(key, None)
            else:
                self._error = f'Value type of {value} is not supported.'
        else:
            self._error = f'Key name {key} is not supported.'

    def all_available(self):
        for n, v, in self.items():
            if v is None:
                return False
        return True
