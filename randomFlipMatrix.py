from random import randint
class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.dict = {}
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.endIdx = n_rows * n_cols - 1
        

    def flip(self):
        """
        :rtype: List[int]
        """
        randIdx = randint(0, self.endIdx)
        realIdx = self.dict.get(randIdx, randIdx)

        idxToSwap = self.dict.get(self.endIdx, self.endIdx)

        self.dict[randIdx] = idxToSwap
        self.endIdx = self.endIdx - 1
        return divmod(realIdx, self.n_cols)
         

    def reset(self):
        """
        :rtype: void
        """
        self.dict = {}
        self.endIdx = self.n_rows * self.n_cols -1
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()