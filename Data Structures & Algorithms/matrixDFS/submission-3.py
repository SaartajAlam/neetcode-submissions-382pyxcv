class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and (i,j) not in visited and grid[i][j] == 0
        
        def dfs(i, j):
            if not isValid(i, j):
                return 0
            if i == ROWS - 1 and j == COLS - 1:
                return 1
            paths = 0
            visited.add((i, j))
            for dx, dy in directions:
                nextRow, nextCol = i + dx, j + dy
                if isValid(nextRow, nextCol):
                    paths += dfs(nextRow, nextCol)
            visited.remove((i, j))
            return paths

        return dfs(0, 0)