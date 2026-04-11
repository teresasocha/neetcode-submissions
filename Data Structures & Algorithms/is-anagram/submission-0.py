class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) == set(t):
            for i in range (0, len(s)):
                if s.count(s[i]) != t.count(s[i]):
                    return False
                return True
        return False