
def calcute_num (num:int):
    '''it take an intger number then will print decreasing number pattern from num to 1 ,then convert to String it will return srting value'''
    paterns=""
    while num != 0:
    
        for i in range(num,0,-1):
            paterns +=str(i)+" "
        paterns+="\n"
    
        num-=1
    return paterns
         
    
result=calcute_num(5)

print(result)
print(calcute_num.__doc__)