"""
    https://leetcode.com/problems/add-two-numbers/description/

    Algorithm:
        For each pair of nodes:

        Add:
        current digit from l1
        current digit from l2
        carry

        Create a new node with:
            sum % 10

        Update carry:
            sum // 10
        Move to the next nodes.

        Continue until:
            both lists are exhausted
            and no carry remains.
    
    Time: O(max(m, n)), space: O(max(m, n))
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry

            carry = sum // 10
            digit = sum % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
