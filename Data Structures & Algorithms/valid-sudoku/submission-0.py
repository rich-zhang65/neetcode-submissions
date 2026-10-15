class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_digits = defaultdict(set)
        col_digits = defaultdict(set)
        square_digits = defaultdict(set)

        for row_idx in range(len(board)):
            row = board[row_idx]

            for col_idx in range(len(row)):
                value = row[col_idx]

                if value == '.':
                    continue

                square_idx = (row_idx // 3) * 3 + (col_idx // 3)

                if value in row_digits[row_idx]:
                    return False
                if value in col_digits[col_idx]:
                    return False
                if value in square_digits[square_idx]:
                    return False

                row_digits[row_idx].add(value)
                col_digits[col_idx].add(value)
                square_digits[square_idx].add(value)

        return True
                