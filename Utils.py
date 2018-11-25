class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x) :
        if type(x) is list:
            ptr = dummyHead = ListNode(0)
            for val in x:
                ptr.next = ListNode(val)
                ptr = ptr.next
            self.val = dummyHead.next.val
            self.next = dummyHead.next.next
        else:
            self.val = x
            self.next = None 