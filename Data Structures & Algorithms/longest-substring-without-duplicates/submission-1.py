class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(0, length):
            a = 1
            j = i + 1
            while j < length:
                if s[j] not in s[i:j]:
                    a += 1
                else:
                    break
                j += 1
            if a > ans:
                ans = a
        return ans
        