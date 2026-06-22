class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        for n in nums:
            l = 1
            s = n + 1
            while s in nums:
                l += 1
                s += 1
            if max_len < l:
                max_len = l
        return max_len
        
        