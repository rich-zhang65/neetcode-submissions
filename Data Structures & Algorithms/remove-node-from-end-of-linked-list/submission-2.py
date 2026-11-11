# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count_node = head
        length = 0
        while count_node:
            count_node = count_node.next
            length += 1

        dummy = ListNode(next=head)
        prev_node, next_node = dummy, head

        for i in range(length - n):
            temp = next_node
            next_node = next_node.next
            prev_node = temp

        prev_node.next = next_node.next
        return dummy.next
