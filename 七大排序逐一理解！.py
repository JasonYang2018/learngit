#lianbiao
#单链表、循环链表、双向链表
#数组中出现次数超过一半的数字
#七大排序逐一理解
#1、冒泡排序

def bubb_sort(list):
    n = len(list)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if list[j]<list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

array = [56,78,23,12,89,24,5,6,7]
#print (bubb_sort(list))

#2 快速排序
def quicksort(array):
    if len(array) <2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        for i in array[1:]:
            if i<=pivot:
                less.append(i)
            else:
                greater.append(i)
    return quicksort(less)+[pivot]+quicksort(greater)

print ('快速排序：', quicksort(array))