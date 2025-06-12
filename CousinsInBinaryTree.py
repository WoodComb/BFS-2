'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
'''

# // Time Complexity : O(n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : no

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # null edge case:
        if not root:
            return False
        # set up queue, we dont need result array in this case
        q = deque([root])

        while q:
            len_q = len(q)
            x_there = y_there = False
            
            for _ in range(len_q):
                curr_node = q.popleft()

                # check if children are x & y - that means they are siblings, not cousins
                if curr_node.left and curr_node.right:
                    if (curr_node.left.val == x and curr_node.right.val == y) or\
                    (curr_node.left.val == y and curr_node.right.val == x):
                        return False

                # check if node is x or y
                if curr_node.val == x:
                    x_there = True
                
                if curr_node.val == y:
                    y_there = True
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            
            if x_there and y_there:
                return True
            if x_there or y_there:
                return False
        
        return False
         
        