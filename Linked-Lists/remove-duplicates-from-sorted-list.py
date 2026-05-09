"""
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/

    Algorithm:
        Since the list is already sorted, duplicates will always be adjacent.

            So:
                compare current node with next node
                if equal → skip next node
                otherwise move forward    
    
    Time: O(n), space: O(1)
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            
            else:
                current = current.next

        return head
