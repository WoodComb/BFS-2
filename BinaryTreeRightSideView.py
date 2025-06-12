'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

# // Time Complexity : O(n)
# // Space Complexity : O(h)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : no

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can do level order traversal
        # then, we can just return the last element of every level
        # null edge case
        if not root:
            return []

        # we need a result array and a queue
        res = []
        q = deque()

        # init the first value
        q.append(root)
        while q:
            # critical for knowing which level we are in
            q_len = len(q)
            temp_res = []
            for i in range(q_len):
                curr_node = q.popleft()
                if curr_node.left: q.append(curr_node.left)
                if curr_node.right: q.append( curr_node.right)
                temp_res.append(curr_node.val)
            res.append(temp_res[-1])
        return res
        
