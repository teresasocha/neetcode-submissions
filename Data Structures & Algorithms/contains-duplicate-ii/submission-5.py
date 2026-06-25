class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k != 0:
            if k >= len(nums):
                if len(nums) != len(set(nums)):
                    return True
            for i in range(0, len(nums) - k, k):
                if len(nums[i:i+k]) != len(set(nums[i:i+k])):
                    return True
            if len(nums[len(nums) - k - 1::]) != len(set(nums[len(nums) - k - 1::])):
                return True
        return False