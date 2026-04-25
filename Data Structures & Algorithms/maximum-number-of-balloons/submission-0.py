class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = int(text.count('l')/2)
        o = int(text.count('o')/2)
        n = text.count('n')
        balloon = [b, a, l, o, n]
        return min(balloon)