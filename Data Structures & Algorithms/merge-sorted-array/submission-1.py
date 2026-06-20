class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n, i = m - 1, n - 1, len(nums1) - 1
        while m >= 0 or n >= 0:
            if n < 0 or (m >= 0 and nums1[m] >= nums2[n]):
                nums1[m], nums1[i] = nums1[i], nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
