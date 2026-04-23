class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            an = [1]
            for j in range(1, i):
                an.append(ans[i-1][j-1] + ans[i-1][j])
            an.append(1)
            ans.append(an)
        return ans

        