import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils import ListNode

#class Solution:
#    def reverseKGroup(self, head, k):
#        """
#        :type head: ListNode
#        :type k: int
#        :rtype: ListNode
#        """
#               
#        i = 0
#        ptr = head
#        
#        while ptr:
#            ptr = ptr.next
#            i = i + 1
#        
#        groups = i / k
#        
#        ptr = head
#        dummy = ListNode(0)
#        dummy.next = head
#        
#        m = n = 0
#        
#        last = None
#        pre = None
#
#        while m < groups:
#            if last and m > 1:
#                last.next = pre
#                
#            
#            while n < k:
#                nextNode = ptr.next
#                ptr.next = pre
#
#                pre = ptr
#                ptr = nextNode
#                n = n + 1
#                
#            n = 0
#            m = m + 1
#        
#        last.next = nextNode
#        
#        return dummy.next
                
if __name__ == "__main__":
    s = Solution()
    l = ListNode([1,2,3,4,5])
    s.reverseKGroup(l, 2)

    print(s)