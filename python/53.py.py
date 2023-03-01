def isPalindrome(s1):
    return s1 == s1[::-1]
def isPalindrome(s2):
    return s2 == s2[::-1]
def isPalindrome(s3):
    return s3 == s3[::-1]
   
  
# Driver code
s1 = (input("enter a string:"))
s2 = (input("enter a string:"))
s3 = (input("enter a string:"))

ans1 = isPalindrome(s1)
ans2 = isPalindrome(s2)
ans3 = isPalindrome(s3)

if ans1:
    print("Yes")
else:
    print("No")
if ans2:
    print("Yes")
else:
    print("No")
    
if ans3:
    print("Yes")
else:
    print("No")
    
  
  
