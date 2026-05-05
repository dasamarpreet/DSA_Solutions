"""
    https://leetcode.com/problems/odd-even-linked-list/
    This problem is not about values — it's about position-based grouping.

    Pointer manipulation in-place (no extra memory allowed).

    Time: O(n), space: O(1)
"""

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = even_head

        return head
