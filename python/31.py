def checkHarshad( n ) :
    sum = 0
    temp = n
    while temp > 0 :
        sum = sum + temp % 10
        temp = temp // 10
    
    return n % sum == 0
 
a=int(input("enter a number:"))
b=int(input("enter a number:"))

if(checkHarshad(a)) : print("Yes")
else : print ("No")
 
if (checkHarshad(b)) : print("Yes")
else : print ("No")
