class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)/2
        for n in nums:
            if nums.count(n) > length:
                return n      