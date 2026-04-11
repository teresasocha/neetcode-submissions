class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = len(s) - 1
        if s[i] == ' ':
            while s[i] == ' ':
                counter += 1
                i -= 1
        while i > -1:
            if s[i] == ' ':
                return len(s[i + 1::]) - counter
            i -= 1
        return len(s) - counter
