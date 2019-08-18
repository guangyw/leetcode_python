class Solution:
    def minimumTotalDfs(self, triangle):
        maxSum = float('-inf')
        
        def dfs(triangle, idx, sum):
            nonlocal maxSum
            if not triangle or not triangle[0]:
                maxSum = max(maxSum, sum)
                return
            
            dfs(triangle[1:], idx, sum + triangle[0][1])
            if len(triangle[0]) > idx + 1:
                dfs(triangle[1:], idx + 1, sum + triangle[0][1])
                                   
        dfs(triangle, 0, 0)
        return maxSum

# Get the idea of DP from Divide and Conquer solution
    def minumumTotalDp(self, triangle):
        row = len(triangle)
        for i in reversed(range(row -1)):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]

    def minimumTotalDnC(self, triangle):
        size = len(triangle)
        
        def dfs(x, y):
            if x == size:
                return 0
            
            left = dfs(x + 1, y)
            right = dfs(x + 1, y + 1)

            return triangle[x][y] + min(left, right)

        return dfs(0, 0)
    

if __name__ == "__main__":
    s = Solution()
    s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

    print(s)

        