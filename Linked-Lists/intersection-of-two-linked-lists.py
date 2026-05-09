""" 
    https://leetcode.com/problems/intersection-of-two-linked-lists/

    Algorithm:
        Use two pointers:
        pA starts at headA
        pB starts at headB
        Move each pointer one step at a time.
        When a pointer reaches the end, redirect it to the other list’s head.
        If the lists intersect, the pointers will eventually meet at the intersection node.
        If they do not intersect, both will eventually become null.

        This works because both pointers travel the same total distance:

        lengthA + lengthB

    Time: O(m+n), space: O(1)
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = headA
        listB = headB

        while listA != listB:
            listA = listA.next if listA else headB
            listB = listB.next if listB else headA

        return listA
