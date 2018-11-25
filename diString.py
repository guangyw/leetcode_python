#Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
#Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
#If S[i] == "I", then A[i] < A[i+1]
#If S[i] == "D", then A[i] > A[i+1]

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)
        result = []
        for c in S:
            if c == "I":
                result.append(lo)
                lo = lo + 1
            if c == "D":
                result.append(hi)
                hi = hi - 1
                
        return result