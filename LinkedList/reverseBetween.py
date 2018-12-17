import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils import ListNode

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        i = 1
        fakeHead = preReverse = ListNode(0)
        preReverse.next = ptr = head
      
        
        while i < m and ptr != None:
            preReverse = ptr
            ptr = ptr.next
            i = i + 1
        
        lastReverseNode = ptr
        pre = ptr
        ptr = ptr.next
        i += 1
        
        while ptr and i <= n :
            nextNode = ptr.next
            ptr.next = pre
            
            pre = ptr
            ptr = nextNode
            
            i += 1
        
        preReverse.next = pre
        lastReverseNode.next = ptr
        
        return fakeHead.next

if __name__ == "__main__":
    s = Solution()
    l = ListNode([1,2,3,4,5])
    s.reverseBetween(l, 2, 4)

    print(s)