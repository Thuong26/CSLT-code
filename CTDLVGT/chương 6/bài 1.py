class Node:
    def __init__(self,data):
        self.data =data
        self.left =None
        self.right =None
    def addLeft(self, x):
        self.left=Node(x)             
    def addRight(self, x):
        self.right=Node(x)
    def LNR(self,root):
        if (root != None):
            self.LNR(root.left)
            print(root.data)
            self.LNR(root.right)
    def NLR(self,root): 
        if (root != None):
            print(root.data)
            self.NLR(root.left)
            self.NLR(root.right)
    def LRN(self,root):
        if (root != None):
            self.LRN(root.left)
            self.LRN(root.right)
            print(root.data)
Root=Node(10)
Root.addLeft(34)
Root.addRight(89)
Root.left.addLeft(45)
Root.addRight(89)
Root.left.addRight(50)
Root.NLR(Root)
Root.LNR(Root)
Root.LRN(Root)