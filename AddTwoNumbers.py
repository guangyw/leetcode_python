from Utils import ListNode
class Solution:
    def addTwoNumbers(self, l1, l2):
        h1 = l1
        h2 = l2
        h3 = dumbHead = ListNode(0)
        carry = 0
        while h1 or h2 or carry:
            v1 = v2 = 0
            if h1:
                v1 = h1.val
                h1 = h1.next
            if h2:
                v2 = h2.val
                h2 = h2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            h3.next = ListNode(val)
            h3 = h3.next

        return dumbHead.next
    
if __name__ == "__main__":
    s = Solution()
    result = s.addTwoNumbers(ListNode([9,8]), ListNode([1]))
    print(result)