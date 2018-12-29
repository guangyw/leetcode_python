#import bisect
from bisect import bisect, bisect_left

class RangeModule(object):

    #def __init__(self):
    #    self.X = [0, 10**9]
    #    self.track = [False] * 2

    #def addRange(self, left, right, track=True):
    #    def index(x):
    #        i = bisect.bisect_left(self.X, x)
    #        if self.X[i] != x:
    #            self.X.insert(i, x)
    #            self.track.insert(i, self.track[i-1])
    #        return i
    #    i = index(left)
    #    j = index(right)
    #    self.X[i:j] = [left]
    #    self.track[i:j] = [track]

    #def queryRange(self, left, right):
    #    i = bisect.bisect(self.X, left) - 1
    #    j = bisect.bisect_left(self.X, right)
    #    return all(self.track[i:j])

    #def removeRange(self, left, right):
    #    self.addRange(left, right, False)
    
    def __init__(self):
        self.range = [-float('inf'), float('inf')]

    def addRange(self, left, right):
        self._updateRange(left, right, 0)
        
    def queryRange(self, left, right):
        li = bisect(self.range, left)
        ri = bisect_left(self.range, right)
        return li == ri and li % 2 == 0
    
    def removeRange(self, left, right):
        self._updateRange(left, right, 1)

    def _updateRange(self, left, right, op):
        li = bisect_left(self.range, left)
        ri = bisect(self.range, right)
        
        if li % 2 == op:
            li = li - 1
            left = self.range[li]
        if ri % 2 == op:
            right = self.range[ri]
            ri += 1
            
        self.range[li:ri] = [left, right]
        


# Your RangeModule object will be instantiated and called as such:
left = 2
right = 4
obj = RangeModule()
obj.addRange(left,right)
obj.addRange(3, 5)
obj.addRange(7, 30)
param_2 = obj.queryRange(left,right)
obj.removeRange(left,right)