"""
    https://leetcode.com/problems/partition-list/description/

    Algorithm:
        The best approach is to use two separate linked lists:

            One list for nodes < x
            One list for nodes >= x

            Then connect them at the end.

            This preserves:

            original relative order (stable partition)
            O(n) time
            O(1) extra space
        
    Time: O(n), space: O(1)
"""

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        greater = ListNode()

        smaller = small
        larger = greater
        current = head
        
        while current:
            if current.val >= x:
                larger.next = current
                larger = larger.next
            else:
                smaller.next = current
                smaller = smaller.next

            current = current.next

        larger.next = None
        smaller.next = greater.next

        return small.next
