# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        firstyk = head
        secondyk = head
        while secondyk and secondyk.next:
            firstyk = firstyk.next
            secondyk = secondyk.next.next
            if firstyk == secondyk:
                return True

        return False