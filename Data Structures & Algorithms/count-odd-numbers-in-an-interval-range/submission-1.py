class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high == low:
            return high % 2
        return (high - low)//2 + 1
        