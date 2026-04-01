class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == (2 ** 31) - 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            i, j, distance = q.popleft()
            for dx, dy in directions:
                nextRow, nextCol = i + dx, j + dy
                if isValid(nextRow, nextCol):
                    grid[nextRow][nextCol] = distance + 1
                    q.append((nextRow, nextCol, distance + 1))
            
        