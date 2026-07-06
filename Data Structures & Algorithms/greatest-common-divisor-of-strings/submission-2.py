class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        i = 1
        minl = min(len(str1), len(str2))
        l1 = len(str1)
        l2 = len(str2)
        while i <= minl:
            temp = str1[:i]
            temp1 = int(l1/i) * temp
            temp2 = int(l2/i) * temp
            if temp1 == str1 and temp2 == str2:
                ans = temp
            i += 1
        return ans
        