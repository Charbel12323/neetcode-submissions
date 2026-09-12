"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_copy = {} # old copy -> new copy

        curr = head

        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = old_to_copy[curr]

            copy.next = old_to_copy.get(curr.next)
            copy.random = old_to_copy.get(curr.random)

            curr = curr.next
        
        return old_to_copy[head]