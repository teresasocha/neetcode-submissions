class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while target != numbers[l] + numbers[r]:
            if target > numbers[l] + numbers[r]:
                l += 1
            else:
                r -= 1
        ans = [l + 1 , r + 1]
        return ans