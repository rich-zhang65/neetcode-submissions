class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def condition(mid_m, mid_n):
            return matrix[mid_m][mid_n] >= target

        m = len(matrix)
        n = len(matrix[0])

        def convertIdx(idx):
            return idx // n, idx % n

        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left < right:
            mid = left + (right - left) // 2

            mid_m, mid_n = convertIdx(mid)
            if condition(mid_m, mid_n):
                right = mid
            else:
                left = mid + 1

        left_m, left_n = convertIdx(left)
        return matrix[left_m][left_n] == target
        