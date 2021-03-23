"""
Daily Coding Problem #6

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
"""

# SOLUTION
class Node:
    def __init__(self, data):
        self.data = data        # data attached to the node
        # ??? should this next line be get_pointer(self) or 0 ???
        self.both = get_pointer(self)       # each node would need to have a variable that contains the xor'd pointers for the node before and after it

class XOR_LL:
    def __init__(self, node):
        # head and tail both initialized as the same node
        self.head = node
        self.tail = node
        # no pointers needed yet because they are the same node and either end goes to null (set as 0)
        self.head.both = 0
        self.tail.both = 0

    def add(self, element):
        self.tail.both ^= get_pointer(element)      # tail now also points to this element
        element.both = get_pointer(self.tail) ^ 0       # this element points to the (old) tail and to 0 (end of list)
        self.tail = element     # set new tail to be element

    def get(self, index):
        currNode = self.head
        for i in range(0, index+1):
            if i == index:      # return Node once index is reached
                return currNode.data
            nextPointer = currNode.head.both ^ get_pointer(currNode)        # undo the xor
            if nextPointer == 0:        # return last element in list if index > length of list
                return currNode.data
            currNode = dereference_pointer(nextPointer)

