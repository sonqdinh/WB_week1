class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS / BFS for any 'O' on the border 
        # Adjust the board[r][c] into 'Z' values
        # Traverse the board once more time to adjust the remain '0' to 'X'
        # 'Z' to '0'
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'Z'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
                
        if len(board) != 0:
            rows, cols = len(board), len(board[0])
            for r in range(rows):
                dfs(r, 0)
                dfs(r, cols - 1)

            for c in range(cols):
                dfs(0, c)
                dfs(rows - 1, c)

            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == 'Z':
                        board[r][c] = 'O'
                    elif board[r][c] == 'O':
                        board[r][c] = 'X'