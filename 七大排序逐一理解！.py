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

#归并排序


题目：输入两个链表，找出它们的第一个公共结点。

思路：用python解决的话，相对比较简单，把链表1中的值依次放到list1，然后依次遍历链表2，如果遍历到的值在list1中，说明找到了第一个公共结点，return即可。当然边界情况需要考虑。

python代码如下：

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        list2 = []
        node1 = pHead1
        node2 = pHead2
        while node1:
            list.append(node1.val)
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next