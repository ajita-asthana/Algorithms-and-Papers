# 1019. Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = [] # monotonic stack 
        ans = [] 


        curr = head 
        while curr:
            while stack and curr.val > ans[stack[-1]]:
                idx = stack.pop()
                ans[idx] = curr.val
            stack.append(len(ans))
            ans.append(curr.val)
            curr = curr.next 
