class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)

        prefixes = [1] * arr_len
        suffixes = [1] * arr_len

        for i in range(1, arr_len):
            prefixes[i] = prefixes[i-1] * nums[i-1]
            suffixes[arr_len - 1 - i] = suffixes[arr_len - i] * nums[arr_len - i]

        sol = []
        for i in range(arr_len):
            sol.append(prefixes[i] * suffixes[i])

        return sol
        