def replaceVowelsWithO(test_str, O):
 
    
    vowels = 'AEIOUaeiou'
 
    
    for ele in vowels:
 
        
        test_str = test_str.replace(ele,O)
 
    return test_str
 
 

input_str = "PYTHON"
 

O = "S"

print("Given String:", input_str)
print("Given Specified Character:", O)
print("After replacing vowels with the specified character:",
      replaceVowelsWithO(input_str, O))

