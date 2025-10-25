from typing import Optional

from TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth: int = 0) -> int:
            if root is None:
                return depth
            depth += 1
            return max(dfs(root.left, depth), dfs(root.right, depth))

        return dfs(root) + 1
