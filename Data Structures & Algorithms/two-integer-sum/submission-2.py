class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums[i + 1::]:
                ans.append(i)
                for j in range(i + 1, len(nums)):
                    if nums[j] + nums[i] == target:
                        ans.append(j)
                        return ans
