#Definition for singly-linked list.
# encoding=utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node = ListNode(0)
        first = node
        while l1 is not None and l2 is not None:
            if l1.val + l2.val < 10:
                node.next = ListNode(l1.val+l2.val+carry)
                node = node.next
                carry = 0
            else:
                node.next = ListNode(l1.val+l2.val+carry-10)
                node = node.next
                carry = 1
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            if l1.val+carry<10:
                node.next = ListNode(l1.val+carry)
                node = node.next
                carry = 0
            else:
                node.next = ListNode(0)
                node = node.next
                carry = 1
            l1 = l1.next
        while l2 is not None:
            if l2.val+carry<10:
                node.next = ListNode(l2.val+carry)
                node = node.next
                carry = 0
            else:
                node.next = ListNode(0)
                node = node.next
                carry = 1
            l2 = l2.next
        if carry == 1:
            node.next = ListNode(1)
        
        first = first.next
        return first
            


        

