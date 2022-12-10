"""
Rotate List 

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10**9
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head # check for valid linked list
        
        length, tail = 1, head # start at position 1, get length that will be needed for rotate

        while tail.next:
            tail = tail.next
            length += 1 # find length of linked list, find the end element

        k = k % length # if K is larger than the length of the linked, modulo it
        if k == 0:
            return head # multiple of len of list, rotating it by K will return original linked list
        
        cur = head
        for _ in range(length - k - 1): # find pivot point for rotation, start at the beginning
            cur = cur.next
        
        new_head = cur.next # head of linked list becomes element that needs to be at the start
        cur.next = None # becomes the new tail (end of linked list)
        tail.next = head # point last element to the head (start) of linked list
        return new_head # presumably all of the previous assignments modify the linked list in place
