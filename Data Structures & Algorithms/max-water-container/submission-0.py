class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        water = 0
        for i in range(0, len(heights) - 1):
            for j in range(i + 1, len(heights)):
                w = (j - i) * min(heights[i], heights[j])
                if w > water:
                    water = w
        return water
        