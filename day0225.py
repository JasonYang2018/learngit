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
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                #ret = array[j]
                #array[j]=array[j+1]
                #array[j+1]=ret 
                array[j],array[j+1]=array[j+1],array[j]
    return array

array = [9,8,10,15,7,3,20,14,2,6,7,5,90]
maopaoSort(array)
print (array)


