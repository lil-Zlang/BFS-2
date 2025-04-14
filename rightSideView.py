# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            length =len(queue)
            for i in range (length):
                node = queue.popleft()
                if i == length - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res  

        #Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node exactly once during the BFS traversal.

#Space Complexity: O(W), where W is the maximum width of the binary tree.
