"""
    https://leetcode.com/problems/rotate-list/description/

    Algorithm:
        Find the length of the list.
        Connect the tail to the head to form a circular list.
        Compute the effective rotations:
            k = k % length
        Find the new tail:
            (length - k - 1) steps from the head.
        Break the circle.
        
    Time: O(n), space: O(1)
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head

        while tail.next:
            length += 1
            tail = tail.next
        
        tail.next = head

        eff_rotation = k % length
        count_new_tail = length - eff_rotation - 1
        
        new_tail = head
        
        for _ in range(count_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
