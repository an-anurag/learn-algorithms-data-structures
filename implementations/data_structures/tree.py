"""
Implement tree
"""

# approach 1:
# with list of list in python


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root


def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root,newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = BinaryTree(4)
print(r)
insertLeft(r, 3)
insertRight(r, 5)
print(r)
l = getLeftChild(r)
r = getRightChild(r)
print(l)
print(r)


# Approach 2: 
# with OOP


class BinaryTree:
    
    def __init__(self, node):
        self.node = node
        self.left_child = None
        self.right_child = None
        
    def add_left_child(self, node):
        
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        
        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t
            
    def add_right_child(self, node):
        
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        
        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_node(self, node):
        self.node = node

    def get_root_val(self):
        return self.node


tree = BinaryTree('A')
print(tree)
root = tree.get_root_val()
print(root)

left_child = tree.get_left_child()
print(left_child)
right_child = tree.get_right_child()
print(right_child)


# after node added
tree.add_left_child("B")
tree.add_right_child("C")

left_child = tree.get_left_child()
print(left_child.get_root_val())

right_child = tree.get_right_child()
print(right_child.get_root_val())

tree.add_left_child('D')
print(tree.get_left_child())