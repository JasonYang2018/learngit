L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
'''
L.append('Jason')

L1= list(range(20))
print (L)
print (L[::-1])

print (L[-2])

print (L[-2:-1])

print (L1[-10:])
print (L1[:-1])
print (L1)
print (L1[1:])
print (L1[::-1])










def trim(s):
    if len(s) !=0 and s[0:1] == " ":
        return trim(s[1:])
    elif len(s) !=0 and s[-1] == " ":
        return trim(s[:-1])

    return s


def findMinAndMax(L):
    if len(L)==0:
        return None
    min=L[0]
    max=L[0]
    for x in L:
        if x<min:
            min=x
        if x>max:
            max=x
    return min,max
'''

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n>1:
        num = fibonacci(n-1)+fibonacci(n-2)
        return num
    return None
'''
for n in range(100):
   print (fibonacci(n))

'''

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a=1
    b=0
    ret=0
    for n in range(0,n-1):
        ret = a + b
        b = a
        a = ret
    return ret


for n in range(100):
   print        (fib(n))
