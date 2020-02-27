#二分查找法

def bSearch(array,target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid]<array[right]:
            right = mid - 1
        else:
            left = mid + 1

    return 0


#maopao paixu

def maopaoSort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                #ret = array[j]
                #array[j]=array[j+1]
                #array[j+1]=ret 
                array[j],array[j+1]=array[j+1],array[j]
    return array

array = [9,8,10,15,7,3,20,14,2,6,7,5,90,22,16]
maopaoSort(array)
print ('maopaopaixu:',array)

#xuanzepaixu选择排序
def selectionSort(alist):
    for i in range(len(alist)):
        min_index=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[min_index]:
                min_index=j
                alist[i],alist[min_index] = alist[min_index],alist[i]

        #if min_index != i:
            
    return alist

alist = [54,226,93,17,77,31,44,55,20]
selectionSort(alist)
print('xuanzepaixu:',alist)