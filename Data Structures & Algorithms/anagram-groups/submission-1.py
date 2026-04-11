class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[strs[0]]]
        for i in range(1, len(strs)):
            found = False

            for an in ans:
                flag = True
                if set(an[0]) != set(strs[i]):
                    flag = False
                for letter in set(an[0]):
                    for letter in an[0]:
                        if an[0].count(letter) != strs[i].count(letter):
                            flag = False
                if flag:
                    an.append(strs[i])
                    found = True
                    break
            if not found:
                ans.append([strs[i]])
        return ans
