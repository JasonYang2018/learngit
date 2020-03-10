#lianbiao
#单链表、循环链表、双向链表
#数组中出现次数超过一半的数字
#七大排序逐一理解
#1、冒泡排序

def bubb_sort(list):
    n = len(list)
    for i in range(0,n):
        for j in range(0,n-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

list = [56,78,23,12,89,24,5,6,7]
print (bubb_sort(list))