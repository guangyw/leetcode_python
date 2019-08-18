class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        
        start = 0
        j = 0
        result = []
        for i, c in enumerate(S):
            j = max(last[c], j)
            if j == i:
                result.append(j - start + 1)
                start = i + 1
            
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))