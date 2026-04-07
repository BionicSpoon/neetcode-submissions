class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # this is the middle index of the combined list
        # in other words, we need to find this many elements less then the current num
        # then we will have found the median
        # if the total number of nums is odd, there will be one, otherwise two (but this rounds down)

        mid = (len(nums1) + len(nums2)) // 2
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums2) - 1

        while True:
            m = (l + r) // 2

            nums1_idx = mid - m - 2

            print(nums1_idx)

            n1 = nums1[nums1_idx + 1] if nums1_idx + 1 < len(nums1) else float('infinity')
            n2 = nums2[m + 1] if m + 1 < len(nums2) else float('infinity')
            l1 = nums1[nums1_idx] if nums1_idx >= 0 else float('-infinity')
            l2 = nums2[m] if m >= 0 else float('-infinity')

            print(f'(max({l1=}, {l2=}) + min({n1=}, {n2=})) / 2')

            if l1 <= n2 and l2 <= n1:
                if (len(nums1) + len(nums2)) % 2:
                    return min(n1, n2)
                return (max(l1, l2) + min(n1, n2)) / 2
            elif l2 > n1:
                r = m - 1
            else:
                l = m + 1
