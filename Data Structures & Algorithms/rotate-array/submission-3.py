class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k %= len(nums)
        n = nums[-k:] + nums[:-k]
        for i in range(0, len(nums)):
            nums[i] = n[i]
        