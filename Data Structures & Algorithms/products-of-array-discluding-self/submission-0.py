class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)

        if arr_len == 1:
            return nums

        prefixes = [1 for _ in range(arr_len)]
        suffixes = [1 for _ in range(arr_len)]

        prefixes[0] = nums[0]
        suffixes[arr_len-1] = nums[arr_len-1]

        for i in range(1, arr_len):
            prefixes[i] = prefixes[i-1] * nums[i]
            suffixes[arr_len - 1 - i] = suffixes[arr_len - i] * nums[arr_len - 1 - i]

        sol = []
        for i in range(arr_len):
            if i == 0:
                sol.append(suffixes[1])
            elif i == arr_len - 1:
                sol.append(prefixes[arr_len - 2])
            else:
                sol.append(prefixes[i-1] * suffixes[i+1])

        return sol
        