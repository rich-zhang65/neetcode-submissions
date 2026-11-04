class Solution:
    def findMin(self, nums: List[int]) -> int: 
        left, right = 0, len(nums) - 1
        ans = nums[0]

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # look in the right half
                left = mid + 1
            else:
                # look in the left half
                right = mid

        return nums[left]
        