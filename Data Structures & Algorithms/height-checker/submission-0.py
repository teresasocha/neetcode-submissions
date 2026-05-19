class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        h = sorted(heights)
        for i in range(0, len(h)):
            if h[i] != heights[i]:
                ans += 1
        return ans
        