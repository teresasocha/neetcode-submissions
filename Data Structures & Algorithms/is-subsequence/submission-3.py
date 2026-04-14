class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        flag = True
        last_position = -1
        for i in range(0, len(s)):
            if flag == True:
                flag = False
                for j in range(last_position + 1, len(t)):
                    if s[i] == t[j]:
                        flag = True
                        last_position = j
                        break
            else:
                return False
        return flag
