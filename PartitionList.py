# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


# Reasoning for this solution is trying to balantly update the list based on positions, in place.
# A better approach would be to move nodes with larger values to the end of the list, instead of delicately moving pieces in place.
class WrongSolution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        itr = ListNode(0)
        itr.next = head
        insertPtr = None
        while itr.next != None:            
            if itr.next.val >= x:
                if insertPtr == None:
                    insertPtr = itr
                itr = itr.next
            else:
                if insertPtr == None:
                    itr = itr.next
                else:
                    breakPtr = insertPtr.next
                    insertPtr.next = itr.next
                    insertPtr = insertPtr.next
                    continuePtr = itr.next.next
                    itr.next.next = breakPtr
                    itr.next = continuePtr
        return head

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        
        while head != None:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
   
        l1.next = h2.next
        l2.next = None 

        return h1.next

def init_link_list(stringList):
    dummyHead = ListNode(0)
    ptr = dummyHead
    for i in range(len(stringList)):
        ptr.next = ListNode(stringList[i])
        ptr = ptr.next
    return dummyHead.next


if __name__ == "__main__":
    inputList = init_link_list([1,4,3,2,5,2])
    s = Solution()
    s.partition(inputList, 3)

