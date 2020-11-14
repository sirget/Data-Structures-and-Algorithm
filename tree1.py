class node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    def __str__(self):
        return str(self.data)
    def getData(self): # accessor
        return self.data
    def getLeft(self): # accessor
        return self.left
    def getRight(self): # accessor
        return self.right
    def setData(self, data): # mutator
        self.data = data
    def setLeft(self, left): # mutator
        self.left = left
    def setRight(self, right): # mutator
        self.right = right
class BST:
    def __init__(self,root = None):
        self.root = None if root is None else root
    def addI(self,data):
        if self.root is None:
            self.root = node(data)
        else:
            fp = None
            p = self.root
            while p:
                fp = p
                p = p.left if data < p.data else p.right
            if data < fp.data:
                fp.left = node(data)
            else:
                fp.right = node(data)
    def add(self,data):
        self.root = BST._add(self.root,data)
    def _add(root,data):
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left,data)
            else:
                root.right = BST._add(root.right,data)
        return root
    def inOrder(self):
        BST._inOrder(self.root)
        print()
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root.data, end = ' ')
            BST._inOrder(root.right)
    def printSideway(self):
        BST._printSideway(self.root,0)
        print()
    def _printSideway(root,level):
        if root is not None:
            BST._printSideway(root.right,level+1)
            print('   '*level,root.data,sep = '')
            BST._printSideway(root.left,level+1)
    def preOrder(self):
        BST._preOrder(self.root)
        print()
    def _preOrder(root):
        if root is not None:
            print(root.data,end = ' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)
    def postOrder(self):
        BST._postOrder(self.root)
        print()
    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data,end = ' ')
    def search(self,data):
        print(BST._search(self.root,data))
    def _search(root,data):
        if root is None:
            return None
        else:
            if root.data is data:
                return root
            elif data < root.data:
                return BST._search(root.left,data)
            elif data > root.data:
                return BST._search(root.right,data)
    def path(self,data):
        if BST._search(self.root,data) is not None:
            BST._path(self.root,data)
        else:
            print(None)
    def _path(root,data):
        if root is None:
            return None
        else:
            if root.data is data:
                print('->',root.data,end = ' ')
                return None
            elif data < root.data:
                print('->',root.data,end = ' ')
                return BST._path(root.left,data)
            else:
                print('->',root.data,end = ' ')
                return BST._path(root.right,data)
    def dele(self,data):
        if BST._search(self.root,data) is not None:
            print('start')
            self.root = BST._dele(self.root,data)
        else:
            print(None)
    def _dele(root,data):
        if root.data is data:
            if root.left and root.right:
                incus, par = BST._findMin(root.right,root)
                if par.left is incus:
                    par.left = incus.right
                else:
                    par.right = incus.right
                incus.left = root.left
                incus.right = root.right
                return incus
            else:
                if root.right is not None:
                    return root.right
                else:
                    return root.left
        elif data < root.data:
            root.left = BST._dele(root.left,data)
        else:
            root.right = BST._dele(root.right,data)
        return root
    def _findMin(root,parent):
        if root.left is not None:
            return BST._findMin(root.left,root)
        else:
            return root, parent
l = [int(e) for e in input("insert integers : ").split()]
print(l)
t=BST()
for ele in l:
    t.addI(ele)
#t.preOrder()
#t.postOrder()
t.printSideway()
#t.search(6)
#t.path(4)
t.inOrder()
t.dele(15)
t.printSideway()
t.inOrder()
