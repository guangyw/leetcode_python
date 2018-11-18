import collections

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slidingDeque = collections.deque()
        maxLength = 0
        
        for c in s:
            if c in slidingDeque:
                maxLength = max(maxLength, len(slidingDeque))
                while c in slidingDeque:
                    slidingDeque.popleft()
            
            slidingDeque.append(c)
        
        return max(maxLength, len(slidingDeque))