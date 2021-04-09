"""
Daily Coding Problem #8

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

# SOLUTION
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def univalTree(root):
    _, count = univalHelper(root, 0)
    return count


def univalHelper(root, count):
    if root is None:        # base case, past the leaf node
        return True, count

    # recursive step to check nodes below root
    leftSubtree, leftCount = univalHelper(root.left, count)
    rightSubtree, rightCount = univalHelper(root.right, count)
    count = leftCount + rightCount

    if (not leftSubtree) or (not rightSubtree):
        return False, count
    if (root.left is not None) and (root.left.val != root.val):
        return False, count
    if (root.right is not None) and (root.right.val != root.val):
        return False, count

    count += 1      # subtree is unival if this point is reached
    return True, count


# TEST CASES
n = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert univalTree(n) == 5, "Should be 5"     # checks the given case
