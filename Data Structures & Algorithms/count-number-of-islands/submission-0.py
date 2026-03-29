class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n and (i, j) not in visited and grid[i][j] == "1"

        def dfs(i, j):
            for dx, dy in directions:
                nextRow, nextCol = i + dx, j + dy
                if isValid(nextRow, nextCol):
                    visited.add((nextRow, nextCol))
                    dfs(nextRow, nextCol)
    
        islands = 0
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    visited.add((i, j))
                    dfs(i, j)
        return islands