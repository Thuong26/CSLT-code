class SearchBinary_Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def CreateTree(self):
        # L=[37,10,18,29,50,3,1,6,5,12,20,35,13,41]
        L=[]
        n=int(input("so luong nut nhap vao: "))
        for i in range(1,n+1):
            x=int(input("Nhan cua nut: "))
            self.insert(x)
            L=L+[x]
        return(self)
    def addLeft(self,dataleft): 
        # data nut nay co hay chua, co the bo if
        if self.data:
            # neu chua thi se lay dataleft
            self.left=SearchBinary_Node(dataleft)
        else:
            # co thi se lay dataright, bo luon else
            self.data=dataleft
    def addRight(self,dataright):
        if self.data:
            self.right=SearchBinary_Node(dataright)
        else:
            self.right=dataright
    def LNR(self,root):
        if (root!=None):
            self.LNR(root.left)
            print(root.data,end=" ")
            self.LNR(root.right)
    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" is not Found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+" is not Found"
            return self.right.findval(val)
        else:
            return str(self.data) + " is found"
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=SearchBinary_Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=SearchBinary_Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data=(data)
            
    def delete(self, x): 
        if self == None:
            return self
        if x < self.data:
            if self.left:
                self.left = self.left.delete(x)
            return self
        if x > self.data:
            if self.right:
                self.right = self.right.delete(x)
            return self
# root.data==x
        if self.right == None: # chỉ có con trái
            return self.left
        if self.left == None: # chỉ có con trái
            return self.right
# root có 2 con, tìm con bé nhất của cây phải
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
            self.data = min_larger_node.data
            self.right = self.right.delete(min_larger_node.data)
        return self

root=SearchBinary_Node(25)
root.CreateTree()
print("\nDuyet giua")
root.LNR(root)
root.findval(18)
root.insert(55)
root.delete(20)
root.delete(10)
print("\nDuyet giua")
root.LNR(root)