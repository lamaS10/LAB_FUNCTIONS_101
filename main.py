



def calcute_num (num:int):
    '''it take an intger number then will print decreasing number pattern '''
    while num != 0:
        for i in range(num,0,-1):
            print(i,end=" ")
        print()
        num-=1
    
calcute_num(5)

print(calcute_num.__doc__)