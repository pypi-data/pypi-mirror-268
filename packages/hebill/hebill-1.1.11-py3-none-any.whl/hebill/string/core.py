class String(str):
    def __new__(cls, value):
        return str.__new__(cls, value)

    def contains(self, part: str):
        return part in self

    def _digitize(self, return_number=False):
        if self.count('.') > 1 or self.count('-') > 1:
            return None if return_number else False
        number = self.strip()
        negative = False
        is_float = False
        if '-' in self:
            if not self.startswith('-'):
                return None if return_number else False
            negative = True
            number = self.replace('-', '')
        integer_part = number
        decimal_part = ''
        if '.' in number:
            integer_part, decimal_part = number.split('.')
            if not decimal_part.isdigit():
                return None if return_number else False
            is_float = True
        if ',' in integer_part:
            parts = integer_part.split(',')
            if any(len(part) != 3 for part in parts[1:]):
                return None if return_number else False
        if not return_number:
            return True
        integer_part = integer_part.replace(',', '')
        if is_float:
            number = float(f'{integer_part}.{decimal_part if len(decimal_part) > 0 else 0}')
            return number if not negative else -number
        if integer_part == '':
            return 0
        return int(integer_part)

    def digitalizable(self) -> bool:
        return self._digitize()

    def digitize(self):
        return self._digitize(True)
