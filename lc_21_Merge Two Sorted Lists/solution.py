# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        phead = pCurrent = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pCurrent.next = l1
                pCurrent = pCurrent.next
                l1 = l1.next

            else:
                pCurrent.next = l2
                pCurrent = pCurrent.next
                l2 = l2.next

        if l1 is not None:
            pCurrent.next = l1
        else:
            pCurrent.next = l2

        return phead.next









a = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print(a.mergeTwoLists(l1, l2))

