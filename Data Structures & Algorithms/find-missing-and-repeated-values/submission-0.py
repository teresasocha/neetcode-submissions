class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        temp = []
        for g in grid:
            for num in g:
                temp.append(num)
        values = [i for i in range(1, len(grid) * len(grid) + 1)]
        for num in values:
            if temp.count(num) > 1:
                ans.append(num)
                break
        for num in values:
            if num not in temp:
                ans.append(num)
        return ans
