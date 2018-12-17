import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils import ListNode

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        pre = None
        
        while ptr:
            nextNode = ptr.next
            ptr.next = pre
            
            pre = ptr
            ptr = nextNode
        
        return pre

    def reverListRecursive(self, head):
        if head == None or head.next == None:
            return head
        
        ptr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return ptr     

    def listRotation(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ptr = head
        dummyHead = ListNode(0)
        pre = dummyHead
        
        while ptr.next:
            pre.next = ptr.next
            ptr.next = ptr.next.next
            pre.next.next = ptr
            
            pre = ptr
            ptr = ptr.next
            
        
        return dummyHead.next