class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        for i in range(len(nums)):
            curr = nums[i]

            if i != 0 and curr == nums[i-1]:
                continue 

            pairs = self.twoSum(nums[i+1:], -curr)
            
            for pair in pairs:
                ans.append([curr, pair[0], pair[1]])

        return ans

    def twoSum(self, numbers: List[int], target: int):
        ptr1 = 0
        ptr2 = len(numbers) - 1

        ans = []
        while ptr1 < ptr2:
            cand = numbers[ptr1] + numbers[ptr2]

            if cand == target:
                ans.append((numbers[ptr1], numbers[ptr2]))
                ptr1 += 1
                ptr2 -= 1
                while ptr1 < ptr2 and numbers[ptr1-1] == numbers[ptr1]:
                    ptr1 += 1
                while ptr2 > ptr1 and numbers[ptr2+1] == numbers[ptr2]:
                    ptr2 -= 1
            elif cand > target:
                ptr2 -= 1
            else:
                ptr1 += 1

        return ans
        