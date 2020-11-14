class node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left if left is not None else None
        self.right = right if right is not None else None

def add(r,data):
    if not r:
        return node(data)
    else:
        if data < r.data:
                r.left = add(r.left,data)
        else:
            r.right = add(r.right,data)
        return r
def inorder(r):
    if r:
        inorder(r.left)
        print(r.data, end = ' ')
        inorder(r.right)
def printSideway(r,level):
    if r:
        printSideway(r.right, level+1)
        print(' '*3*level , r.data)
        printSideway(r.left, level+1)
def height(r):
    if not r:
        return -1
    else:
        hl = height(r.left)
        hr = height(r.right)
        if hl>hr:
            return hl+1
        else:
            return hr+1
def path(r,data):
    if r.data is not data:
        print(r.data, '->' ,end=' ')
        if data < r.data:
            path(r.left,data)
        else:
            path(r.right,data)
    else:
        print(data)
def search(r,d):
    if not r:
        return None
    if r.data is d:
        return r.data
    else:
        if d < r.data:
            return search(r.left,d)
        else:
            return search(r.right,d)
def depth(r,d):
    if not r:
        return -1
    else:
        if r.data is d:
            return height(r)
        else:
            if d < r.data:
                return depth(r.left,d)
            else:
                return depth(r.right,d)
def smallest(r):
    if r:
        if r.left is not None:
            return smallest(r.left)
        else:
            return r.data
        

l = [14,4,9,7,15,3,18,16,20,5,16]
print('intput :',l)
r = None
for ele in l:
    r = add(r,ele)       
print('inorder :' , end = ' ')
inorder(r)
print()
print('printSideWay :')
printSideway(r, 0)
print('height of', r.data, '=', height(r))
d = 5
print('path :', d, '=', end = ' ')
path(r, d)
d = 9
t = search(r, d)
print(t)
d = 18
print('depth of node data', d, '=', depth(r, d))
print('smallest data =',smallest(r))