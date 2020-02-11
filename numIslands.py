class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Traverse the grid:
        # Found island piece, increment number of islands. DFS to convert all
        # neighbor island pieces into water.
        
        if len(grid) == 0: # Empty grid
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        n_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    n_islands += 1
                    dfs(r, c)
        
        return n_islands
            