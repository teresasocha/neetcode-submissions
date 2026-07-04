class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        l = len(s)
        ans = 0
        while(i < l):
            if (s[i] == 'I'):
                if (i < l - 1):
                    if (s[i + 1] == 'V'):
                        ans += 4
                        i += 1
                    elif (s[i + 1] == 'X'):
                        ans += 9
                        i += 1
                    else:
                        ans += 1
                else:
                    ans += 1
            elif (s[i] == 'X'):
                if (i < l - 1):
                    if (s[i + 1] == 'L'):
                        ans += 40
                        i += 1
                    elif (s[i + 1] == 'C'):
                        ans += 90
                        i += 1
                    else:
                        ans += 10
                else:
                        ans += 10
            elif (s[i] == 'C'):
                if (i < l - 1):
                    if (s[i + 1] == 'D'):
                        ans += 400
                        i += 1
                    elif (s[i + 1] == 'M'):
                        ans += 900
                        i += 1
                    else:
                        ans += 100
                else:
                        ans += 100
            elif (s[i] == 'V'):
                ans += 5
            elif (s[i] == 'L'):
                ans += 50
            elif (s[i] == 'D'):
                ans += 500
            else:
                ans += 1000
            i += 1
        return ans
                    