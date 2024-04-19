class Excel:
    @staticmethod
    def convert_number_to_letters(number):
        result = ''
        while number > 0:
            number, remainder = divmod(number - 1, 26)
            result = chr(remainder + ord('A')) + result
        return result

    @staticmethod
    def convert_letters_to_number(letters: str):
        letters = letters.upper()
        result = 0
        for char in letters:
            result = result * 26 + (ord(char.upper()) - ord('A')) + 1
        return result
