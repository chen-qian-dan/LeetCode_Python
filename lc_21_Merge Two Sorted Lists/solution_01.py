
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Qian Chen
20191210Tue
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        head = cur = ListNode(0)

        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        else:
            cur.next = l2

        return head.next











