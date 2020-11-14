def eat(n):
    if n==1:
        print('eat', n) # base/simple case
    else: # recursive case
        print('eat', n, end = ' ') # line 1
        eat(n-1) # line 2
#eat(5)

def eats(n):
    if n==1:
        print('eat', n, end = ' ') # base/simple case
    else: # recursive case
        eats(n-1) # line 2
        print('eat', n, end = ' ') # line 1        
#eats(5)

def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)
#print(fac(5))

def sum1ton(n):
    if n<1:
        return "error"
    else:
        if n==1:
            return n
        else:
            return n+sum1ton(n-1)
#print(sum1ton(100))

def printnto1(n):
    if n<1:
        if n == 1:
            print(n, '\n')
        else:
            print(n, end = ' ')
            printnto1(n+1)
    else:
        if n == 1:
            print(n)
        else:
            print(n, end = ' ')
            printnto1(n-1)
#printnto1(-5)
#printnto1(10)

def print1ton(n):
    if n<=1:
        if n==1:
            print(n, end = ' ')
        else:
            print1ton(n+1)
            print(n, end = ' ')          
#print1ton(-5)

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#print(fib(7))

def binarySearch(lo,hi,x,l):
    if hi < lo:
        return 'Not found'
    mid = (hi+lo)//2
    if x == l[mid]:
        return mid
    elif(l[mid]<x):
        return binarySearch(mid+1,hi,x,l)
    else:
        return binarySearch(lo,mid-1,x,l)
#l = [1,2,3,4,5,6,7,8,9]
#x = 5
#print(binarySearch(0,len(l)-1,x,l))

def move(n, A, C, B):
    if n == 1:
        print(n, 'from', A, 'to', C)
    else:
        move(n-1, A, B, C)
        print(n, 'from', A, 'to', C)
        move(n-1, B, C, A)
#move(3,'A','C','B')

def sum1(n, l):
    if n == 0:
        return l[n]
    else:
        return l[n] + sum1(n-1,l)
#l = [1,2,3,4,5,20]
#print(sum1(len(l)-1,l))

def sum2():