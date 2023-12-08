# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        tail = None

        while l1 or l2 or carry:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val

            sum_val = val1 + val2 + carry
            carry, sum_val = sum_val // 10, sum_val % 10

            node = ListNode(sum_val)

            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head