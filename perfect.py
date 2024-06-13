## perfect number

##1st Method

##def perfect(n):
##    sum=1
##    for i in range(2,(n//2)+1):
##        if(n%i==0):
##            sum+=i
##    if n==sum:
##        return True
##    else:
##        return False
##n=int(input())
##result=perfect(n)
##print(result)


##spy number 1124

##def isspy(n):
##    s=0
##    m=1
##    while n:
##        d=n%10#4
##        n=n//10#112
##        s+=d
##        m*=d
##    return s==m  
##        
##n=int(input())
##result=isspy(n)
##print(result)

import math as m
def issemiprime(n):
    sq=
    for i in range(2,sq+1):
        if(n%i==0)

n=int(input())
result=issemiprime(n)
print(result)



