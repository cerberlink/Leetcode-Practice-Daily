"""
The problem is linked: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3347/

Invert a binary tree.

input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9


output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root


input = [4, 2, 7, 1, 3, 6, 9]
print(Solution().invertTree(input))
