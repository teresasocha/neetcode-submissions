class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        p = 1
        while True:
            if p in nums:
                p += 1
            else:
                break
        return p