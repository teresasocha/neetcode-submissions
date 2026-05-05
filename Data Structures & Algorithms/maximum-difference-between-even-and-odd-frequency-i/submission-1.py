class Solution:
    def maxDifference(self, s: str) -> int:
        even = []
        odd = []
        for letter in s:
            frequency = s.count(letter)
            if frequency % 2 == 0:
                even.append(frequency)
            else:
                odd.append(frequency)
        return max(odd) - min(even)      