my_string = 'python'

print("The string is :")
print(my_string)

my_key = ['p', 'y', 't', 'h', 'o', 'n', 't', 'e', 's', 't']
print("The key is ")
print(my_key)
joined_list = ''.join(my_key)

my_result = my_string in joined_list

print("The result is :")
if(my_result == True):
   print("The string is present in the character list")
else:
   print("The string is not present in the character list")
