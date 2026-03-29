# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        q = deque([(root, float("-inf"))])
        while q:
            for _ in range(len(q)):
                node, val = q.popleft()
                if node.val >= val:
                    res += 1
                if node.left:
                    q.append([node.left, max(node.val, val)])
                if node.right:
                    q.append([node.right, max(node.val, val)])
        return res
