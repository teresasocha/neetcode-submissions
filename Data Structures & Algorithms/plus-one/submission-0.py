class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = 1
        i = len(digits) - 1
        while (i >= 0):
            if (digits[i] + r < 10):
                digits[i] += r
                r = 0
            else:
                digits[i] = digits[i] + r - 10
                r = 1
            i -= 1
        if r > 0:
            digits.insert(0, r)
        return digits