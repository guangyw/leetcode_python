class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: 
            return 0
        
        ds = DisjointSets(len(M))
        
        for i in range(len(M)):
            for j in range(i + 1, len(M[0])):
                if M[i][j] == 1:
                    ds.union(i, j)
        
        circles = set()
        for i in range(len(M)):
            circles.add(ds.find(i))
        return len(circles)
        
        
class DisjointSets:
    def __init__(self, size):
        self._par = list(range(size))
        self._rnk = [0] * (size) 
        
    def find(self, x):
        if self._par[x] != x:
            self._par[x] = self.find(self._par[x])
        return self._par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        
        elif self._rnk[xr] > self._rnk[yr]:
            self._par[yr] = xr
        elif self._rnk[xr] < self._rnk[yr]:
            self._par[xr] = yr
        else:
            self._par[yr] = xr
            self._rnk[xr] += 1
            
        return True
    
    def totalParents(self):
        return self._par