class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        s = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                s += 1
            else:
                if s > ans:
                    ans = s
                s = 0
        if s > ans:
            ans = s
        return ans
        