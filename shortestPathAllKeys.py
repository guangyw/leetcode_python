import collections

class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        numOfKeys = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    starti = i
                    startj = j
                if grid[i][j] in "abcdef":
                    numOfKeys += 1
        
        moves = set()
        deque = collections.deque()
        
        deque.append([starti, startj, 0, ".abcdef", 0])
        
        while deque:
            i, j, steps, validSteps, totalCollected = deque.popleft()
            
            if grid[i][j] in "abcdef" and grid[i][j].upper() not in validSteps:
                validSteps += grid[i][j].upper()
                totalCollected +=1
                
            if totalCollected == numOfKeys:
                return steps
            
            for x, y in directions:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] in validSteps:
                    if (i + x, j + y, validSteps) not in moves:
                        moves.add((i+x, j+y, validSteps))
                        deque.append([i + x, j + y, steps + 1, validSteps, totalCollected])
            
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))