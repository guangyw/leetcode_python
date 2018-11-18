class Solution:
    def maxNumberFromOneArray(self, nums, k):
        stack = []
        total = len(nums)

        for i in range(total):
            while stack and nums[i] > stack[-1] and total - i - 1 + len(stack) >= k:
                stack.pop()
            stack.append(nums[i])

        return stack
    

if __name__ == "__main__":
    s = Solution()
    print(s.maxNumberFromOneArray([1,3,8,7,5,9,6], 4))
