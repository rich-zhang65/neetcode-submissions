class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = (nums2, nums1) if len(nums1) < len(nums2) else (nums1, nums2)
        m, n = len(nums1), len(nums2)
        left, right = 0, n
        left_part_size = (m + n) // 2

        # binary search for max boundary - ends when the start of right partition is found in nums2
        while left < right:
            mid = left + (right - left + 1) // 2
            nums1_idx = left_part_size - mid - 1

            if nums2[mid - 1] > nums1[nums1_idx + 1]:
                right = mid - 1
            else:
                left = mid

        left_max = max(
            nums1[left_part_size - left - 1] if left_part_size - left - 1 >= 0 else float('-infinity'),
            nums2[left - 1] if left - 1 >= 0 else float('-infinity')
        )
        right_min = min(
            nums1[left_part_size - left] if left_part_size - left < m else float('infinity'),
            nums2[left] if left < n else float('infinity')
        )

        return right_min if (m + n) % 2 else (left_max + right_min) / 2
        