class Palindrome:

    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(s: str) -> bool:
        _s_ = []
        for index in range(0, len(s)):
            if Palindrome.is_letter_or_digit(s[index]):
                _s_.append(s[index].lower())
        s = "".join(_s_)
        for index in range(0, len(s)):
            if s[index] != s[len(s) - 1 - index]:
                return False
        return True

    @staticmethod
    def is_letter_or_digit(s) -> bool:
        return str(s).isalnum()

    def __repr__(self):
        return 'Palindrome'