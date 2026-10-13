class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)

        sol = [1] * arr_len

        for i in range(1, arr_len):
            sol[i] *= sol[i-1] * nums[i-1]


        suffix = 1
        for i in range(arr_len - 2, -1, -1):
            sol[i] *= suffix * nums[i+1]
            suffix *= nums[i+1]

        return sol