class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        p = 1
        numss = set(nums)
        while True:
            if p in numss:
                p += 1
            else:
                break
        return p