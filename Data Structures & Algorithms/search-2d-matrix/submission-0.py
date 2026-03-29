class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top = 0
        bot = ROWS - 1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                bot = mid - 1
        candidate = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[candidate][mid] > target:
                r = mid - 1
            elif matrix[candidate][mid] < target:
                l = mid + 1
            else:
                return True
        return False
