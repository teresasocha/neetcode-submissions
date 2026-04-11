class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(0 , len(min(strs))):
            for s in strs:
                if min(strs)[i] != s[i]:
                    return ans
            ans += min(strs)[i]
        return ans

        