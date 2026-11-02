class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(mid):
            return nums[mid] >= target
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left if nums[left] == target else -1