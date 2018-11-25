class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, res = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack[-1]
                stack.pop()
                res += 0 if not stack else ((
                    min(height[i], height[stack[-1]])-height[bottom])*(i - stack[-1] - 1))
            stack.append(i)
        return res

    def trapWith2Pointers(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = 0
        right = len(height) -1
        
        maxLeft = 0
        maxRight = 0
        
        trappedWater = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    trappedWater += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    trappedWater += maxRight - height[right]
                right -= 1
            
        return trappedWater


if __name__ == "__main__":
    s = Solution()
    result = s.trap([0,1,0,2,1,0,1,3])