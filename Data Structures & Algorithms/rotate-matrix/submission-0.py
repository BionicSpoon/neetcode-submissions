class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose and reverse each row
        # in place with temp rows

        ROWS, COLS = len(matrix), len(matrix[0])
        for i in range(ROWS):
            for j in range(i+1, COLS):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(ROWS):
            for j in range(COLS // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][COLS - j - 1]
                matrix[i][COLS - j - 1] = temp

            