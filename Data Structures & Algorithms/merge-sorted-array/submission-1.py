class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c1 = m - 1
        c2 = n - 1
        p = m + n -1
        while c1 >= 0 and c2 >= 0:
            if nums1[c1] <= nums2[c2]:
                nums1[p] = nums2[c2]
                c2 -= 1
            else:
                nums1[p] = nums1[c1]
                c1 -= 1
            p -= 1
        if c2 >= 0:
            for i in range(0, c2 + 1):
                nums1[i] = nums2[i]
        