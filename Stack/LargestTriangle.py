class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        maxRect = 0
        heights.append(-1)
        
        for i in range(len(heights)):
            if heights[i] == heights[stack[-1]]:
                continue
            else:
                while heights[i] < heights[stack[-1]]:
                    cur = stack.pop()
                    curRect = heights[cur] * (i - stack[-1] -1)
                    maxRect = max(curRect, maxRect)
            stack.append(i)
        

            
        return maxRect


s = Solution()

s.largestRectangleArea([0, 9])
#s.largestRectangleArea([2,1,5,6,2,3])