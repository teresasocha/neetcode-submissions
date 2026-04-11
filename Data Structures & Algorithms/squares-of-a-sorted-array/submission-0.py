class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [num*num for num in nums]
        return sorted(ans)        