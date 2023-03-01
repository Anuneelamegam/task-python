
x={"Sid":122,"name":"user1","company":"Besant",120:450}
print(x)
{'Sid': 122, 'name': 'user1', 'company': 'Besant', 120: 450}

print(type(x))


x={"Sid":122,"name":"user1","company":"Besant",120:450,"a":[1,2,3,5]}
print(x)
{'Sid': 122, 'name': 'user1', 'company': 'Besant', 120: 450, 'a': [1, 2, 3, 5]}

print(x["name"])

x={}
print(x)

x[100]="C"
x[101]="C++"
x[102]="Java"
x[103]="python"
print(x)
{100: 'C', 101: 'C++', 102: 'Java', 103: 'python'}

x[150]="Java"

print(x)
{100: 'C', 101: 'C++', 102: 'Java', 103: 'python', 150: 'Java'}

x[102]="JavaScript"
print(x)
{100: 'C', 101: 'C++', 102: 'JavaScript', 103: 'python', 150: 'Java'}

x[500]="ruby"
print(x)
{100: 'C', 101: 'C++', 102: 'JavaScript', 103: 'python', 150: 'Java', 500: 'ruby'}
del x[101]
print(x)
print(len(x))
print(max(x))
print(min(x))      
     
