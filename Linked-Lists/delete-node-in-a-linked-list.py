"""
    https://leetcode.com/problems/delete-node-in-a-linked-list/description/

    Algorithm:
        Since we are not given the head of the list, we cannot traverse the list to find the previous node.

        But we are guaranteed:
            the node is not the last node
            all values are unique

        So we use a clever trick.
        Key Idea:

        Instead of deleting the current node directly:

        Copy the value of the next node into the current node.
        Skip the next node.
        
    Time: O(n), space: O(1)
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
