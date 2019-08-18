class Solution:
    def paintAll(self, n):
        results = []
        self.tryPaint([], results, n)
        print(results)
    
    
    def tryPaint(self, current, all, n):
        for color in [0, 1]:
            if (len(current) > 1 and color == current[-1] and color == current[-2]):
                return
            
            current.append(color)
            if(len(current) == n):
                all.append(current)
                return

            self.tryPaint(current.copy(), all, n)

if __name__ == "__main__":
    s = Solution()
    s.paintAll(3)