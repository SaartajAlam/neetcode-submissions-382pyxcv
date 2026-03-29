class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and board[i][j] == "O" and (i, j) not in visited
        
        def dfs(i, j):
            visited.add((i, j))
            for dx, dy in directions:
                nextRow, nextCol = i + dx, j + dy
                if isValid(nextRow, nextCol):
                    dfs(nextRow, nextCol)
        
        for i in range(COLS):
            if board[0][i] == "O" and (0, i) not in visited:
                dfs(0, i)
            if board[ROWS - 1][i] == "O" and (ROWS - 1, i) not in visited:
                dfs(ROWS - 1, i)
        
        for j in range(ROWS):
            if board[j][0] == "O" and (j, 0) not in visited:
                dfs(j, 0)
            if board[j][COLS - 1] == "O" and (j, COLS - 1) not in visited:
                dfs(j, COLS - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"