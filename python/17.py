a=10
b=0

print(a//2)
print(b//a)
try:
    print(a//0)#error
except:
    print("ZeroDivision Error")
print("Thank You!!!")
