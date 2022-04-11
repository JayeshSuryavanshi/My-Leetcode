class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[] for _ in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        entries = rows * cols
        
        for i in range(entries):
            new_grid[i//cols].append(grid[(i - k) % entries // cols][(i - k) % entries % cols])
        
        return new_grid
        