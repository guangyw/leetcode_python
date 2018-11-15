class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lo = 1
        hi = m * n
        while lo < hi:
            mid = (hi + lo) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ == "__main__":
    s = Solution()
    print(s.findKthNumber(45,12,471))

