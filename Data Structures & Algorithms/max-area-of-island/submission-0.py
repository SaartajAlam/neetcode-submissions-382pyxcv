class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n and (i, j) not in seen and grid[i][j] == 1

        def dfs(i, j):
            seen.add((i, j))
            area = 1
            for dx, dy in directions:
                nextRow, nextCol = i + dx, j + dy
                if isValid(nextRow, nextCol):
                    area += dfs(nextRow, nextCol)
            return area

        seen = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = max(res, dfs(i, j))
        return res

