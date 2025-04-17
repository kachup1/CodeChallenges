'''Basic binary tree
    Creates the following tree:
        1
       / \
      2   3
'''
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
node_one = TreeNode(1)
node_two = TreeNode(2)
node_three = TreeNode(3)

node_one.left = node_two #Node two is the left child of node one
node_one.right = node_three #Node three is the right child of node one

'''
Binary Search Tree Example:
    Created the following tree:
        By Key:          By Value:
           1               Yoda  
          / \              / \
         2   3          Luke  R2D2
'''
class TreeNode():
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
# Create individual nodes
z = TreeNode(2, 'Yoda')
x = TreeNode(1, 'Luke')
y = TreeNode(3, 'R2D2')
# Build the tree by linking nodes
root = x
root.left = z
root.right = y

'''
Example of Binary Search Tree Implementation
'''
class TreeNode():
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
def search_bst(node, key):
    #Base case: node is None or we find the key
    if node is None or node.key == key:
        return node
    
    #If the key to be found is less than the current nodes key, search in the left subtree
    if key < node.key:
        return search_bst(node.left, key) 
    
    #If the key to be found is greater than the current nodes key, search in the right subtree
    return search_bst(node.right, key)