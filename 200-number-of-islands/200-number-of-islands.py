class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        row = len(grid)
        column = len(grid[0])
        
        islands = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    islands += 1
        return islands
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return 0
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
            
        
                