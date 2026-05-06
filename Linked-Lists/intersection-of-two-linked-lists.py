""" 
    https://leetcode.com/problems/intersection-of-two-linked-lists/



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
