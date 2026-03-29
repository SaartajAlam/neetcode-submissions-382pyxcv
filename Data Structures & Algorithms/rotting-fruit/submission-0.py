class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1

        q = deque()
        fresh = time = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in directions:
                    nextRow, nextCol = i + dx, j + dy
                    if isValid(nextRow, nextCol):
                        fresh -= 1
                        grid[nextRow][nextCol] = 2
                        q.append((nextRow, nextCol))
            time += 1
        return time if fresh == 0 else -1
