def bubble(l):
    print(l)
    for last in range(len(l)-1, -1,-1):# จาก last ind ถึง ind 0
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i] #swap
                swaped = True
                print(l)
        if not swaped:
            print(l)
            break

#l = [5,6,2,3,0,1,4]
#bubble(l)
#print('------------------\n')
def selection(l):
    print(l)
    for last in range(len(l)-1, -1, -1):# จาก last ind ถึง ind 0
        biggest = l[0] # ค่าใหญ่สุด
        biggest_i = 0 # ตําแหน่ง ของค่าใหญ่สุด
        for i in range(1, last+1): # จากตําแหน่ง 1 ถึง last หาค่าใหญ่สุด
            if l[i] > biggest: # if ที@ i ใหญ่กว่าค่าเดิม
                biggest = l[i] # เปลี@ยน ค่าใหญ่ที@สุด เป็น ค่าใหม่ที@ i
                biggest_i = i # เก็บ index ค่าใหญ่อันใหม่
    #swap elements biggest and last element
        l[last], l[biggest_i ] = l[biggest_i], l[last]
        print(l)

#selection(l)
#print('------------------\n')

def insertion(l):
    print(l)
    for i in range(1, len(l)): #from index 1 to last index
        iEle = l[i] #insert element
        for j in range(i, -1, -1):
            if iEle<l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
        print(l)

#insertion(l)
#print('------------------\n')

def shell(l, dIncrements):
    print(l)
    for inc in dIncrements: #for each deminishing increment
        for i in range(inc,len(l)): #insertion sort เก็บทีละตัว
            iEle = l[i] #inserting element
            for j in range(i, -1, -inc):#insertion sort -inc at a time to-1
                if iEle<l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
        print(l)

#l = [10,11,1,13,2,6,4,12,5,8,7,9,3]
#dIncrements = [5,3,1]
#shell(l, dIncrements)

def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right-1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd: # copy remaining left half if any
        result.append(l[left])
        left += 1
    while right <= rightEnd: # copy remaining right half if any
        result.append(l[right])
        right += 1
    for ele in result: # copy result back to list l
        l[start] = ele
        start += 1
        if start > rightEnd:
            break

def mergeSort(l, left, right):
    center = (left+right)//2
    if left < right:
        mergeSort(l, left, center)
        mergeSort(l, center+1, right)
        merge(l, left, center+1, right)
#l = [5,3,6,1,2,7,8,4]
#print(l)
#mergeSort(l,0, len(l)-1)
#print(l)

def quick(l, left, right):
    if left == right-1 : #only 2 elements
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left] #swap
        return
    if left<right:
        #partition
        pivot = l[left] #first element pivot
        i, j = left+1, right
        while i<j:
            while i<right and l[i]<=pivot:
                i += 1
            while j>left and l[j]>=pivot:
                j -= 1
            if i<j:
                l[i], l[j] = l[j], l[i] #swap
        if left is not j:
            l[left], l[j] = l[j], pivot # swap pivot to index j
        quick(l, left, j-1)
        quick(l, j+1, right)

l = [5,1,4,9,6,3,8,2,7,0]
quick(l,0,len(l)-1)
print(l)