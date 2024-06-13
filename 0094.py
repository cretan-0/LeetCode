class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)
        in_order(root)
        return res
