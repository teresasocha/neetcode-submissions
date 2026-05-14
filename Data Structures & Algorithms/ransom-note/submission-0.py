class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        copy = magazine
        for letter in ransomNote:
            if letter in magazine:
                if magazine.count(letter) < ransomNote.count(letter):
                    return False
            else:
                return False
        return True
        