class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def addLeft(self,dataleft): 
        # data nut nay co hay chua, co the bo if
        if self.data:
            # neu chua thi se lay dataleft
            self.left=Node(dataleft)
        else:
            # co thi se lay dataright, bo luon else
            self.data=dataleft
    def addRight(self,dataright):
        if self.data:
            self.right=Node(dataright)
        else:
            self.right=dataright
    def LNR(self,root):
        if (root!=None):
            self.LNR(root.left)
            print(root.data,end=" ")
            self.LNR(root.right)
    def NLR(self,root):
        if (root != None):
            print(root.data)
            self.NLR(root.left)
            self.NLR(root.right)
    def LRN(self,root):
        if (root != None):
            print()
            print(root.data)
            self.LRN(root.left)
            self.LRN(root.right)
root=Node(10)
root.addLeft(34)
root.addRight(89)
root.left.addLeft(45)
root.addRight(89)
root.left.addRight(50)
root.LNR(root)
root.NLR(root)
root.LRN(root)

    
