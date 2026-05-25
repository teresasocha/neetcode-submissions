class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        for num in set(nums):
            if nums.count(num) > len(nums)//3:
                ans.append(num)
        return ans
        