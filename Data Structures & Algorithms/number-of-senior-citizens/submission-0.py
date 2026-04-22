class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = [person for person in details if int(person[11:13]) > 60]
        return len(seniors)
        