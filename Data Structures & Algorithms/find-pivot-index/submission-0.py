class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        elif sum(nums[:len(nums) - 1]) == 0:
            return len(nums) - 1
        else:
            for i in range(1, len(nums) - 1):
                if sum(nums[:i]) == sum(nums[i + 1:]):
                    return i
        return -1
        