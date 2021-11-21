class Anagram:

    def __init__(self):
        pass

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str_array = [0] * 26
        for _s_ in s:
            str_array[ord(_s_) - 97] = str_array[ord(_s_) - 97] + 1
        print(str_array)
        for _t_ in t:
            str_array[ord(_t_) - 97] = str_array[ord(_t_) - 97] - 1
        print(str_array)
        for _str_ in str_array:
            if _str_ != 0:
                return False
        return True

    def __repr__(self):
        return 'Anagram'