class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            for dx, dy in directions:
                nextRow, nextCol = i + dx, j + dy
                if isValid(nextRow, nextCol):
                    area += dfs(nextRow, nextCol)
            return area
        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res