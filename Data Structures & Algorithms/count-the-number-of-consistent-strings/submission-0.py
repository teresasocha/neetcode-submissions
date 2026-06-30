class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            flag = True
            for w in set(word):
                if w not in allowed:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans
