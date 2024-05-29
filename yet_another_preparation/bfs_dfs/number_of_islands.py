from typing import List

class Solution:
    def draw_land(self, x: int, y: int, grid: List[List[int]]):
        if grid[x][y] == "0":
            return
        
        grid[x][y] = "0"

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for move in moves:
            adj_x, adj_y = move
            if 0 <= x + adj_x < len(grid) and 0 <= y + adj_y < len(grid[x]):
                self.draw_land(x + adj_x, y + adj_y, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.draw_land(i, j, grid)
                    number_of_islands += 1

        return number_of_islands
        