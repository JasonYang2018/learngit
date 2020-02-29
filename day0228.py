
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printChain(node):
    while node:
        print(node.val)
        node = node.next


if __name__ == '__main__':
    # 1 -> 2 -> 3
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)
    list1.next = list2
    list2.next = list3
    list3.next = None
    printChain(list1)

'''

s = "string"
ret = []
ret = s
print(ret[1])