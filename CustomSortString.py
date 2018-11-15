class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        occurrence = {}
        result = []
        for i in T:
            if i in S:
                if i not in occurrence:
                    occurrence[i] = 1
                else:
                    occurrence[i] = occurrence[i] + 1 
            else:
                result.append(i)
        for j in S:
            if j in occurrence:
                for _ in range(occurrence[j]):
                    result.append(j)
        
        return ''.join(result)