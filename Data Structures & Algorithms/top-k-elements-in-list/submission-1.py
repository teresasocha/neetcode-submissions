class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [n for n in nums]
        for n in nums:
            while ans.count(n) > 1:
                ans.remove(n)    
        while len(ans) > k:
            min_count = nums.count(ans[0])
            min_index = 0
            for i in range(1, len(ans)):
                if nums.count(ans[i]) < min_count:
                    min_count = nums.count(ans[i])
                    min_index = i
            ans.remove(ans[min_index]) 
        return ans