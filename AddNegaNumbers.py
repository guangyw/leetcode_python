class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1, arr2 = arr1[::-1], arr2[::-1]
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
            
        smallSize = len(arr2)
        
        res = []
        borrow = carry = 0
        for i in range(len(arr1)):
            val = -borrow + carry + arr1[i] + (arr2[i] if i < smallSize else 0)
            
            if val < 0:
                carry = 1
                rem = 1
                borrow = 0
            else:
                carry = 0
                borrow = val // 2
                rem = val % 2
            
            res.append(rem)
            
        if carry > 0:
            res.append(1)
        
        if borrow > 0:
            res.extend([1,1])
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
            
        return res[::-1]
                        

s = Solution()
print(s.addNegabinary([1,1,1,1,1], [1,0,1]))