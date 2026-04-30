class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        count = 0
        for i in range(0, len(s)):
            if s[i] == t[count]:
                count += 1
        ans = len(t) - count
        return ans