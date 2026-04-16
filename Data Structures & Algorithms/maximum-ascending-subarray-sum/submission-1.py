class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                s += nums[i]
            else:
                if s > ans:
                    ans = s
                s = nums[i]
        if s > ans:
            ans = s
        return ans

        