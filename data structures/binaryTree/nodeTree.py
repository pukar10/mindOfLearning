# Create a binary tree 
class nodeTree:
    def __init__(self, data) -> 'nodeTree':
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = nodeTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = nodeTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Inorder, left -> root -> right
def printInorder(root):        
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

# Postorder, left -> right -> root
def printPostorder(root):
    if root: 
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

# Preorder, root -> left -> right
def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

tree1 = nodeTree(10)
tree1.insert(5)
tree1.insert(15)

# Inorder, 5, 10, 15
# Postorder, 5, 15, 10
# Preorder, 10, 5, 15    
# 
# printInorder(tree1)
# printPostorder(tree1)
# printPreorder(tree1)