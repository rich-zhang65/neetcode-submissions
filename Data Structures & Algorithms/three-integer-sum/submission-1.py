class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        for i, curr in enumerate(nums):
            if i != 0 and curr == nums[i-1]:
                continue 

            ptr1 = i + 1
            ptr2 = len(nums) - 1

            while ptr1 < ptr2:
                cand = nums[ptr1] + nums[ptr2]

                if cand == -curr:
                    ans.append((curr, nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
                    while ptr1 < ptr2 and nums[ptr1-1] == nums[ptr1]:
                        ptr1 += 1
                    while ptr2 > ptr1 and nums[ptr2+1] == nums[ptr2]:
                        ptr2 -= 1
                elif cand > -curr:
                    ptr2 -= 1
                else:
                    ptr1 += 1

        return ans
        