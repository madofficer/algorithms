from typing import Optional

from TreeNode import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: TreeNode, s: int = 0) -> None:
            nonlocal res
            if root.left is None and root.right is None:
                res += 2 * s + root.val
                return

            if root.left:
                dfs(root.left, 2 * s + root.val)

            if root.right:
                dfs(root.right, 2 * s + root.val)

        dfs(root)

        return res

