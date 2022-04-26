class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # we will store last index of the merged array beforehand
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        # taking care of leftover values         
        nums1[:n] = nums2[:n]