def bubblesort(l):
    print('Bubble :', end=' ')
    for last in range(len(l)-1, -1, -1):
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l


def selectionsort(l):
    print('selection :', end=' ')
    for last in range(len(l)-1, -1, -1):
        big = l[0]
        ibig = 0
        for i in range(1, last+1):
            if l[i] > big:
                big = l[i]
                ibig = i
        l[last], l[ibig] = l[ibig], l[last]
    return l


def insertionsort(l):
    print('insertion :', end=' ')
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    return l


def shellsort(l):
    print('shell :', end=' ')
    for inc in range(5, 0, -2):
        for i in range(inc, len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if iEle < l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
    return l


def merge(arr, l, r, rE):
    start = l
    lE = r-1
    result = []
    while l <= lE and r <= rE:
        if arr[l] < arr[r]:
            result.append(arr[l])
            l += 1
        else:
            result.append(arr[r])
            r += 1
    while l <= lE:
        result.append(arr[l])
        l += 1
    while r <= rE:
        result.append(arr[r])
        r += 1
    for ele in result:
        arr[start] = ele
        start += 1
        if start > rE:
            return


def mergesort(arr, l, r):
    if l < r:
        m = (l + (r-1))//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m+1, r)
    return arr


def quicksort(l, left, right):
    if left == right-1:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
        return
    if left < right:
        pivot = l[left]
        i, j = left+1, right
        while i < j:
            while i < right and l[i] <= pivot:
                i += 1
            while j > left and l[j] >= pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
        if left is not j:
            l[left], l[j] = l[j], pivot
        quicksort(l, left, j-1)
        quicksort(l, j+1, right)
    return l


def QS(L, str):
    global time
    if L == []:
        return L
    if str == 'First':
        pivot = L.pop(0)
    elif str == 'End':
        pivot = L.pop()
    elif str == 'Mid':
        pivot = L.pop(int((len(L)-1)/2))
    left = []
    right = []
    for i in L:
        time += 1
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    left = QS(left, str)
    right = QS(right, str)
    liss = []
    for i in left:
        liss.append(i)
    liss.append(pivot)
    for i in right:
        liss.append(i)
    return liss


L1 = "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1".split(' ')
L2 = []
for i in L1:
    L2.append(int(i))
print(L2, "\n")

time = 0
#LL = QS(L2, 'First')
#print("QuickSortFirst\t", time, "\t", LL)
time = 0
LL = QS(L2, 'End')
print("QuickSortEnd\t", time, "\t", LL)
time = 0
LL = QS(L2, 'Mid')
print("QuickSortMid\t", time, "\t", LL)


def test():
    l = [11, 10, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
    print(l)
    print(bubblesort(l))
    l = [11, 10, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
    print(l)
    print(selectionsort(l))
    l = [11, 10, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
    print(l)
    print(insertionsort(l))
    l = [11, 10, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
    print(l)
    print(shellsort(l))
    l = [11, 10, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
    print(l)
    print('merge :', end=' ')
    print(mergesort(l, 0, len(l)-1))
    l = [11, 10, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
    print(l)
    print('quick :', end=' ')
    print(quicksort(l, 0, len(l)-1))

# test()
