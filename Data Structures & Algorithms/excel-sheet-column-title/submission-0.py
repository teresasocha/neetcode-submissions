class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        columnTitle = ""
        while n > 0:
            n -= 1
            n, modulo = divmod(n, 26)
            columnTitle = chr(modulo + 65) + columnTitle
        return columnTitle