# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, next_node = None, head

        while next_node is not None:
            next_next_node = next_node.next
            next_node.next = prev_node
            prev_node = next_node
            next_node = next_next_node

        return prev_node
        