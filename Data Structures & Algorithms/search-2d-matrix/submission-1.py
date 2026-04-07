class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # encode both row and col in a single int:
        # decode with row, col = l // len(matrix), l % len(matrix[0]) 
        l = 0
        r = (len(matrix)) * len(matrix[0]) - 1 

        # print(l, r)
        while l <= r:
            mid = (l + r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            # print(f'{mid=}, {row=}, {col=}')
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
            # print(l, r)
        return False