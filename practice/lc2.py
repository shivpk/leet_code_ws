"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def parse_node(node):
            node_val_str = str(node.val)
            n = node
            while n.next:
                n = n.next
                node_val_str += str(n.val)

            return int(node_val_str[::-1])

        sum1 = str((parse_node(l1) + parse_node(l2)))
        node = ListNode(int(sum1[0]))

        for s in sum1[1:]:
            node = ListNode(int(s), node)

        return node


n1 = ListNode(3)
n2 = ListNode(4, n1)
l1 = ListNode(2, n2)

n1 = ListNode(4)
n2 = ListNode(6, n1)
l2 = ListNode(5, n2)

Solution().addTwoNumbers(l1, l2)
