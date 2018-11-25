class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        scores = []
        
        for op in ops:
            if op == "C":
                scores.pop()
            elif op == "D":
                score = scores[-1]
                scores.append(2 * score)
            elif op == "+":
                score = scores[-1] + scores[-2]
                scores.append(score)
            else:
                scores.append(int(op))
        print(scores)
        return sum(scores)

if __name__ == "__main__":
    s = Solution()
    s.calPoints(["5","2","C","D","+"])
