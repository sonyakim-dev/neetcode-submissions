class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [10,20,20,40,0,0]
        #            m   i
        # [1,2]
        #    n

        # [10,20,20,0,30,40]
        #         m i
        # [1,30]
        #    n
        m, n, i = m - 1, n - 1, len(nums1) - 1
        while m >= 0 or n >= 0:
            if n < 0 or (m >= 0 and nums1[m] >= nums2[n]):
                nums1[m], nums1[i] = nums1[i], nums1[m]
                m -= 1
                i -= 1
            elif m < 0 or (n >= 0 and nums1[m] < nums2[n]):
                nums1[i] = nums2[n]
                n -= 1
                i -= 1
