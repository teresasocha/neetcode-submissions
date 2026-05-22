class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if nums[0] % 2 == 0:
            flag = 0
        else:
            flag = 1
        for i in range(1, len(nums)):
            n = nums[i] % 2
            if n == flag:
                return False
            else:
                flag = n
        return True
        