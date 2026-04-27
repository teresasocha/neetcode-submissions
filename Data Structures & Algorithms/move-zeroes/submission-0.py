class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        