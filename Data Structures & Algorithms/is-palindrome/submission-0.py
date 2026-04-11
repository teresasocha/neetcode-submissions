class Solution:
    def isPalindrome(self, s: str) -> bool:
        hlp = [letter for letter in s if letter.isalnum()]
        ans = ""
        for letter in hlp:
            ans += letter
        return ans.lower() == ans[::-1].lower()