class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        
        for num in nums:
            for i in range(32):
                valAtBitI = ((1 << i) & num) >> i
                bits[i] = (bits[i] + valAtBitI) % 3
        
        theOne = 0
        
        for i in range(31):
            if bits[i]:
                theOne |= 1 << i
        
        # to deal with negative numbers
        if bits[-1]:
            theOne -= 1 << 31

        return theOne