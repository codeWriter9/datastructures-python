class UniqueCharacter:

    def __init__(self):
        pass

    @staticmethod
    def first_uniq_char(s: str) -> int:
        unique = -1
        _dict_ = dict()
        arr = [0] * 26
        for ch in s:
            arr[ord(ch) - ord('a')] = arr[ord(ch) - ord('a')] + 1
        for index in range(0, len(s)):
            _dict_[index] = arr[ord(s[index]) - ord('a')]
        for key in _dict_.keys():
            if _dict_[key] == 1:
                return key
        return unique

    def __repr__(self):
        return 'UniqueCharacter'
