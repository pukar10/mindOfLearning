# Create a nodeTree class for a binary tree 

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
    


    
        
