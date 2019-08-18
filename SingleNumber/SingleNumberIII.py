# We are trying to find the two single number a, b
# XOR the whole list will get c = a ^ b
# We know that a != b, so c != 0
# Meaning there is at least one bit in c that's not 0
# And that bit in a and b are different 
# 在某一个二进制位上 a != b

class Solution:
    def singleNumber(self, nums):
        xors = 0

        for num in nums:
            xors ^= num
            
        idx = -1
        
        for i in range(32):
            if (xors & (1 << i)) >> i != 0:
                idx = i
                break
        
        xor1 = 0
        xor2 = 0
        
        for num in nums:
            mask = 1 << idx
            if (num & mask) >> idx:
                xor1 ^= num
            else:
                xor2 ^= num
        
        return [xor1, xor2]