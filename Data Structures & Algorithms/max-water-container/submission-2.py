class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        water = 0
        while i < j:
            w = (j - i) * min(heights[i], heights[j])
            water = max(water, w)
            if heights[i] < heights[j]:
                i +=1
            else:
                j -=1
        return water
        