class Solution:
    def validPalindrome(self, s: str) -> bool:
        word = ""
        tab = [letter for letter in s if letter.isalnum()]
        for letter in tab:
            word += letter

        if word == word[::-1]:
            return True
        for i in range(0, len(word)):
            temp = ""
            if i == 0:
                temp = word[1:]
            elif i == 1:
                temp = word[0] + word[2:]
            else:
                temp = word[: i] + word[i + 1 : ]
            if temp == temp[::-1]:
                return True
        return False
