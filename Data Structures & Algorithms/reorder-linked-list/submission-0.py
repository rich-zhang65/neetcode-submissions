# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node, next_node = None, slow.next
        while next_node:
            temp = next_node.next
            next_node.next = prev_node
            prev_node = next_node
            next_node = temp

        slow.next = None
        
        dummy = head
        while prev_node:
            temp = dummy.next
            dummy.next = prev_node
            dummy = dummy.next

            prev_node = prev_node.next
            dummy.next = temp
            dummy = dummy.next
