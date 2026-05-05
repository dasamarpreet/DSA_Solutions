""" https://leetcode.com/problems/linked-list-cycle-ii/

    Floyd's Tortoise & Hare OR Floyd's Cycle Detection Algorithm
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s_point = f_point = head

        while f_point and f_point.next:
            s_point = s_point.next
            f_point = f_point.next.next

            if f_point == s_point:
                break
        else:
            return None
        
        s_point = head
        while f_point != s_point:
            s_point = s_point.next
            f_point = f_point.next

        return f_point
