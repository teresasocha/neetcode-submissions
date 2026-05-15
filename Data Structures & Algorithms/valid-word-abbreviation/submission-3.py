class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length = 0
        i = 0
        while i < len(abbr):
            temp = 0
            if abbr[i].isnumeric():
                if abbr[i] == '0':
                    return False
                temp = int(abbr[i])
                i += 1
                while i < len(abbr) and abbr[i].isnumeric():
                    temp = temp * 10 + int(abbr[i])
                    i += 1
                length += temp
            else:
                if length >= len(word) or abbr[i] != word[length]:
                    return False
                length += 1
                i += 1
        return len(word) == length

