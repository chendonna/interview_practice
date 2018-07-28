"""
    get the height of a binary search tree -> number of edges
    between a tree's root and its furthest reach
    ex. single node has a height of 0
"""
def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0
    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)

    if left_height > right_height:
        return left_height
    else:
        return right_height
