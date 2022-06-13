# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cu = head
        while cu:
            while cu.next and cu.next.val == cu.val:
                cu.next = cu.next.next
            cu = cu.next
        return head
