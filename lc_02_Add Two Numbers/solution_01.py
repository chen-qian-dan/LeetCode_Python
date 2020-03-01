
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0

        head = ListNode(0)
        tail = head
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, remainder = divmod(val1 + val2 + carry, 10)
            tail.next = ListNode(remainder)
            tail = tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return head.next
