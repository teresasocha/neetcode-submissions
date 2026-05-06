class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        temp = [i for i in range(1, len(nums) + 1)]
        for num in temp:
            if num not in nums:
                ans.append(num)
        return ans        