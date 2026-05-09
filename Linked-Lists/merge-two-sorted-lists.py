"""
    https://leetcode.com/problems/merge-two-sorted-lists/

    Algorithm:
        Iterative Approach:

        Each iteration should:
            Compare current nodes
            Attach the smaller node
            Move only that list forward
            Compare again
        
        After one list ends, the other list is already sorted, so append it directly.
    
    Time: O(m + n), space: O(1)
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next
