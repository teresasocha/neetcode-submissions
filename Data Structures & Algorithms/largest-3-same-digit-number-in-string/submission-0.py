class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        i = 0
        while i < len(num) - 2:
            if num[i+2] == num[i+1] == num[i]:
                temp = num[i:i+3]
                if temp > largest:
                    largest = temp
                i += 3
            else:
                i += 1
        return largest
        