#Max Area of Island

class Solution:
    #def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #visited : dict[int, bool] = dict()
    def maxAreaOfIsland(self, grid):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows = len(grid)
        columns = len(grid[0])
        visited = [[False for i in range(columns)] for j in range(rows)]
        maxArea = 0

        for i in range(rows):
            for j in range(columns):
                #while stack.count > 0:
                if (visited[i][j]):
                    continue
                if grid[i][j] == 1:
                    stack = []
                    area = 0
                    stack.append((i,j))
                    visited[i][j] = True
                    while len(stack) > 0:
                        node = stack.pop()
                        area = area + 1
                        for direction in directions:
                            iNext = node[0] + direction[0]
                            jNext = node[1] + direction[1]
                            if (iNext >= 0 and jNext >= 0 and iNext < rows and jNext < columns and grid[iNext][jNext] == 1 and not visited[iNext][jNext]):
                                stack.append((iNext, jNext))
                                visited[iNext][jNext] = True
                    maxArea = max(maxArea, area)
        return maxArea

s = Solution()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s.maxAreaOfIsland(grid))
