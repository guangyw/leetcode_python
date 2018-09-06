#takeaway:
#RLE: Run-length encoding
import itertools

class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        runs, count = self.Rle(S)

        expWordsCount = 0

        for word in words:
            wordRun, wordCount = self.Rle(word)
            if runs != wordRun:
                continue
            expWordsCount += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, wordCount))

    def Rle(self, S):
        return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(S)])

    def RleBeforeZip(self, S):
        return [(k, len(list(grp))) for k, grp in itertools.groupby(S)]
        
if __name__ == "__main__":
    s = Solution()
    testString = "heeeeelloooo"
    testSquareBracket = s.RleBeforeZip(testString)
    #splattedList = *testSquareBracket
    rleValue = s.Rle(testString)
    print(rleValue)