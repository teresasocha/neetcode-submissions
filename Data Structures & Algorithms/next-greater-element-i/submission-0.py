class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums1)):
            id = nums2.index(nums1[i]) + 1
            for j in range(id, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
            if len(ans) < i + 1:
                ans.append(-1)
        return ans