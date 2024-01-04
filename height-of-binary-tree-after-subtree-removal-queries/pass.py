# https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def cal_height(tree_node):
            if tree_node is None:
                return -1
            tree_map[tree_node.val] = tree_node
            tree_node.height = max(cal_height(tree_node.left), cal_height(tree_node.right)) + 1
            return tree_node.height

        def cal_sub_height(tree_node, sub_height, depth):
            left_height = -1 if tree_node.left is None else tree_node.left.height
            right_height = -1 if tree_node.right is None else tree_node.right.height
            if tree_node.left is not None:
                cal_sub_height(tree_node.left, max(sub_height, right_height + depth), depth + 1)
            if tree_node.right is not None:
                cal_sub_height(tree_node.right, max(sub_height, left_height + depth), depth + 1)
            tree_node.sub_height = sub_height

        tree_map = {}
        cal_height(root)
        cal_sub_height(root, -1, 1)
        return list(map(lambda query: tree_map[query].sub_height, queries))


solution = Solution()
print(solution.treeQueries(
    TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7))),
    [3, 2, 4, 8]))
