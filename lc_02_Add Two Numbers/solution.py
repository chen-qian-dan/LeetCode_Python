# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nVal1 = 0
        nVal2 = 0

        # list to int
        scala = 1
        while l1.next is not None:
            nVal1 += scala * l1.val
            scala *= 10
            l1 = l1.next
        nVal1 += scala * l1.val

        scala = 1
        while l2.next is not None:
            nVal2 += scala * l2.val
            scala *= 10
            l2 = l2.next
        nVal2 += scala * l2.val

        nRet = nVal1 + nVal2

        reminder = nRet % 10
        head = tail = ListNode(reminder)
        nRet //= 10
        while nRet > 0:
            reminder = nRet % 10
            node = ListNode(reminder)
            tail.next = node
            tail = tail.next
            nRet //= 10

        return head
