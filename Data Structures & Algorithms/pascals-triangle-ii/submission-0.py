class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        i = 1
        while i <= rowIndex:
            temp = [pascal[0]]
            for j in range(1, len(pascal)):
                temp.append(pascal[j-1] + pascal[j])
            temp.append(pascal[len(pascal) - 1])
            pascal = temp
            i += 1
        return pascal
        