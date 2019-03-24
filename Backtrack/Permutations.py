class Solution:
    def permute(self, nums):
        result = []
        cur = []
        def backtrack(idx):
            if idx == len(nums):
                result.append(cur[:])
            
            cur.append(nums[idx])
            backtrack(idx + 1)
            cur.pop()
        
        backtrack(0)
        return result

s = Solution()
s.permute([1,2,3])