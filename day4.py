def product(*numbers):
    if len(numbers)==0 :
        raise TypeError
    else:
        sum=1
        for n in numbers:
            sum=sum*n
            
        return sum
        


print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))