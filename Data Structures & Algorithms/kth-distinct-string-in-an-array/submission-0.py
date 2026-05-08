class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        for a in arr:
            if arr.count(a) == 1:
                count += 1
                if count == k:
                    return a
        return ""           
        