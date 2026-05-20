class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for num in set(arr):
            if arr.count(num) == num:
                ans = num
        return ans
        