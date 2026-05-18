class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            max_l = 1
            l = 1
            i = 1
            while i < len(nums):
                if nums[i-1] < nums[i]:
                    l += 1
                    i += 1
                else:
                    if l > max_l:
                        max_l = l
                    l = 1
                    i += 1
            if l > max_l:
                max_l = l        
            l = 1
            i = 1
            while i < len(nums):
                if nums[i-1] > nums[i]:
                    l += 1
                    i += 1
                else:
                    if l > max_l:
                        max_l = l
                    l = 1
                    i += 1
            if l > max_l:
                max_l = l
        return max_l




        