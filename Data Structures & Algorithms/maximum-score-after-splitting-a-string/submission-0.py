class Solution:
    def maxScore(self, s: str) -> int:
        temp = []
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            temp.append(score)
        return max(temp)
        