class SearchBinaryNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def CreateTree(self):
        #n=int(input('n='))
        l=[37 ,10, 18, 29, 50, 3, 1, 6, 5, 12, 20, 35, 13, 32, 41]
        for i in range (len(l)):    
            self.insert(l[i])
        return(self)    
    def DuyetTruoc(self,x):
        if (x!=None):
            print(x.data)
            self.DuyetTruoc(x.left)
            self.DuyetTruoc(x.right)
    def DuyetGiua(self,x):
        if (x!=None):
            self.DuyetGiua(x.left)
            print(x.data)
            self.DuyetGiua(x.right)
    def DuyetSau(self,x):
        if (x!=None):
            self.DuyetSau(x.left)
            self.DuyetSau(x.right)
            print(x.data)
    # def CreateTree(self):
    #     n=int(input('n='))
    #     for i in range(1,n+1):
    #         x=input('nhãn của nút:')
    #         self.insert(x)
    def insert(self, x):
        if self.data:
            if x < self.data:
                if self.left is None:
                    self.left = SearchBinaryNode(x)
                else:
                    self.left.insert(x)
            elif x> self.data:
                if self.right is None:
                    self.right = SearchBinaryNode(x)
                else:
                    self.right.insert(x)
        else:
            self.data = x
    def delete(self, x):
            if self == None:
                return(self)
            if x < self.data:
                if self.left:
                    self.left = self.left.delete(x)
                return(self)
            if x > self.data:
                if self.right:
                    self.right = self.right.delete(x)
                return(self)
            # đã tìm ra nút có giá trị x, hay self.data==x
            if self.right == None: # chỉ có con trái
                return (self.left)
            if self.left == None: # chỉ có con trái
                return (self.right)
    # root có 2 con, tìm con bé nhất của cây phải
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.data = min_larger_node.data
            self.right = self.right.delete(min_larger_node.data)
            return (self)
t=SearchBinaryNode(25)
t.CreateTree()
print("duyet truoc")
t.DuyetTruoc(t)
print("duyet giua")
t.DuyetGiua(t)
print("duyet sau")
t.DuyetSau(t)
t.delete(29)

print("duyet giua sau xoa")
t.DuyetGiua(t)