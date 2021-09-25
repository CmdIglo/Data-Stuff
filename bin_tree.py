class treeNode():
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

tree = treeNode(1)
tree.right = treeNode(2)
tree.left = treeNode(3)
tree.left.left = treeNode(4)
tree.left.right = treeNode(5)
tree.right.left = treeNode(6)
tree.right.right = treeNode(7)

def solution(treeNode):
    
    if not treeNode:
        return None

    treeNode.right, treeNode.left = treeNode.left, treeNode.right
    
    solution(treeNode.right)
    solution(treeNode.left)

    return treeNode

def printTree(tree):
    print(tree.val)
    if tree.left:
        printTree(tree.left)
    if tree.right:
        printTree(tree.right)

printTree(tree)

print(" \n ")

inverted_tree = solution(tree)

printTree(inverted_tree)
