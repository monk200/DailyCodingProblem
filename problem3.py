"""
Daily Coding Problem #3

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

# GIVEN CODE
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# SOLUTION
def serialize(root):
    return preorder(root) + ": " + inorder(root)


def inorder(root):      # left child -> node -> right child -> ...
    string = ""

    if root.left is not None:
        string += inorder(root.left)
    string += root.val + " "
    if root.right is not None:
        string += inorder(root.right)

    return string


def preorder(root):     # node -> left child -> ... -> right child -> ...
    string = ""

    string += root.val + " "
    if root.left is not None:
        string += preorder(root.left)
    if root.right is not None:
        string += preorder(root.right)

    return string


def deserialize(s):
    x = list(s.split(" "))      # temp list just to convert nodes in string to elements
    # separate given string into the preorder and inorder traversals
    preorder = x[:x.index(":")]
    inorder = x[x.index(":")+1:len(x)-1]

    return deserializeHelper(preorder, inorder, 0, 0, len(inorder)-1)


def deserializeHelper(preorder, inorder, preIndex, inIndex, end):
    if (preIndex > len(preorder)-1) or (inIndex > end):     # return None if preIndex or inIndex go past the end of their arrays
        return None
    root = preorder[preIndex]       # establish root node

    if root in inorder:
        newInIndex = inorder.index(root)       # index splits inorder traversal into left and right trees

        return Node(root, deserializeHelper(preorder, inorder, preIndex + 1, inIndex, newInIndex-1),
                    deserializeHelper(preorder, inorder, preIndex + newInIndex - inIndex + 1, newInIndex+1, end))
    else:
        return None


# TEST CASES
node = Node('root', Node('left', Node('left.left')), Node('right'))     # given test case (leaning left tree)
"""
creates tree seen below
        root
        /  \
    left  right
    /
left.left
"""
#print(serialize(node))
assert deserialize(serialize(node)).val == 'root'
assert deserialize(serialize(node)).left.val == 'left'
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).right.val == 'right'
#print(serialize(deserialize(serialize(node))))

node2 = Node('3', Node('9'), Node('20', Node('15'), Node('7')))     # leaning right tree
"""
creates tree seen below
        3
       / \
      9  20
        /  \
       15   7
"""
#print(serialize(node2))
assert deserialize(serialize(node2)).val == '3'
assert deserialize(serialize(node2)).left.val == '9'
assert deserialize(serialize(node2)).right.val == '20'
assert deserialize(serialize(node2)).right.left.val == '15'
assert deserialize(serialize(node2)).right.right.val == '7'
#print(serialize(deserialize(serialize(node2))))

node3 = Node('A')       # single node tree
#print(serialize(node3))
assert deserialize(serialize(node3)).val == 'A'
#print(serialize(deserialize(serialize(node3))))

node4 = Node('A', Node('B', Node('C')))     # left branches only
#print(serialize(node4))
assert deserialize(serialize(node4)).val == 'A'
assert deserialize(serialize(node4)).left.val == 'B'
assert deserialize(serialize(node4)).left.left.val == 'C'
#print(serialize(deserialize(serialize(node4))))

node5 = Node('A', None, Node('B', None, Node('C')))     # right branches only
#print(serialize(node5))
assert deserialize(serialize(node5)).val == 'A'
assert deserialize(serialize(node5)).right.val == 'B'
assert deserialize(serialize(node5)).right.right.val == 'C'
#print(serialize(deserialize(serialize(node5))))

