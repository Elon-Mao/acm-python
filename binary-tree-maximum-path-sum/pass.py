# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -1000

        def max_path_sum(node):
            if node is None:
                return 0
            left_path_sum = max_path_sum(node.left)
            right_path_sum = max_path_sum(node.right)
            node_max_sum = max(node.val, node.val + left_path_sum, node.val + right_path_sum)

            nonlocal max_sum
            max_sum = max(max_sum, node_max_sum, node.val + left_path_sum + right_path_sum)
            return node_max_sum

        max_path_sum(root)
        return max_sum


solution = Solution()
print(solution.maxPathSum(root=TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
