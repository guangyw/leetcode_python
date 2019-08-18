class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        totalIslands = 0
        
        def findIsland(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x, y) in visited or grid[x][y] != "1":
                return
            
            visited.add((x, y))
            
            for direction in dirs:
                findIsland(x + direction[0], y + direction[1])

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    findIsland(i, j)
                    totalIslands += 1
                    
        return totalIslands

if __name__ == "__main__":
    s = Solution()
    result = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    print(result)