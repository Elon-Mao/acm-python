# https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def update_height(parent_node, tree_node):
            if tree_node is None:
                return -1
            tree_map[tree_node.val] = tree_node
            tree_node.parent = parent_node
            tree_node.height = max(update_height(tree_node, tree_node.left), update_height(tree_node, tree_node.right)) + 1
            return tree_node.height

        def cal_sub_height(tree_node, sub_height):
            if tree_node == root:
                return sub_height
            parent_node = tree_node.parent
            sibling_node = parent_node.left if tree_node == parent_node.right else parent_node.right
            sibling_height = sibling_node.height if sibling_node is not None else -1
            return cal_sub_height(parent_node, max(sibling_height, sub_height) + 1)

        tree_map = {}
        update_height(None, root)
        return list(map(lambda query: cal_sub_height(tree_map[query], -1), queries))


solution = Solution()
print(solution.treeQueries(
    TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7))),
    [3, 2, 4, 8]))
