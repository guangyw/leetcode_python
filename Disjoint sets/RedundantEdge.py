class Solution:
    def findRedundantConnection(self, edges):
        ds = DisjointSets(len(edges))
        
        for edge in edges:
            if not ds.union(edge[0], edge[1]):
                return edge
            
    
class DisjointSets:
    def __init__(self, size):
        self._par = list(range(size + 1))
        self._rnk = [0] * (size +1) 
        
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

if __name__ == "__main__":
    s = Solution()
    result = s.findRedundantConnection([[1,2],[1,3],[2,3]])
    print(result)
