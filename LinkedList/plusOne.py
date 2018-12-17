import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils import ListNode

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversedList = self.reverseList(head)
        carry, reversedList.val = divmod(reversedList.val + 1, 10)

        ptr = reversedList

        while carry > 0:
            if ptr.next == None:
                ptr.next = ListNode(carry)
                carry = 0
            else: 
                carry, ptr.next.val = divmod(ptr.next.val + 1, 10)
                ptr = ptr.next

        return self.reverseList(reversedList)
            

    
    def reverseList(self, head):

        pre, ptr = None, head

        while ptr:
            ptr.next, ptr, pre = pre, ptr.next, ptr
            
        return pre

if __name__ == "__main__":
    s = Solution()
    l = ListNode(9)
    s.plusOne(l)

    print(s)

