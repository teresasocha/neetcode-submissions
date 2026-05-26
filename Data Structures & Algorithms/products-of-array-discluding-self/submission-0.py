class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            product = 1
            j = 0
            while 0 <= j < i:
                product *= nums[j]
                j += 1
            j += 1
            while j < len(nums):
                product *= nums[j]
                j += 1
            ans.append(product)
        return ans
            
        