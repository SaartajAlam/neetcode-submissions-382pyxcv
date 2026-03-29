class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        length = 1
        visit = set()
        q = deque()
        visit.add((0, 0))
        q.append((0, 0))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1], [1, 1], [1, -1]]
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if newRow == ROWS or newCol == COLS or min(newRow, newCol) < 0 or (newRow, newCol) in visit or \
                    grid[newRow][newCol] == 1:
                        continue
                    q.append((newRow, newCol))
                    visit.add((newRow, newCol))
            length += 1
        return -1
