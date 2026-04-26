class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        h = 0
        if len(word1) > len(word2):
            for i in range(0, len(word2)):
                ans += word1[i]
                ans += word2[i]
                h = i 
            ans += word1[i + 1::]
        else:
            for i in range(0, len(word1)):
                ans += word1[i]
                ans += word2[i]
                h = i
            if len(word1) < len(word2):
                ans += word2[i+1::]
        return ans