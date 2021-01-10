
list  = ["hello", 'test', "java", "bingo"]


# usage of quotation marks
# print("hello")
print('print("hello")')

# f-string
city = "Rome"
number = 4
print(f"{city} hello {number}")


# list index
print(list[0])
print(list[0:])   # 0<=index
print(list[:1])   # 0<=index<1
print(list[-1]) 
print(list[1:3])
print(list[2:])
print(list[-2:])
print(list)
list.append("hello1")
print(list)
x = list.pop()
print(list, x)


dict = {1:'A', 2:'B', 3:'C'}

print(dict[1], dict[2]) 

dict = {'first_name': 'Tom', 'last_name': "Cruise"}

print(dict['first_name'])
print(dict['last_name'])

dict['email'] = '3@gmail.com'

print(dict)

#Trap for the in operator 
print('first_name' in dict.keys()) # don't use this one. Slow
print('first_name' in dict)    # correct one.

list  = ["hello", 'test', "java", "bingo"]
print("hello" in list)

# tuple
X = ("hello", "test", "java", "bingo")
print(X)

list.sort(key = lambda x: x[-1])
print(list)

# lambda
plus = lambda x: x+1
print(plus(1))

def plus(x): 
  x = x+1

def sort_by_lastchar(x):
  return x[-1]

# set
x = {1, 3, 10 , 11}

list = [ 1, 3, 10 , 11]
y = set(list)
print(y)


#print(1 in x) 

# Example of an class and print an object of an class. 
class Actor: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __len__(self):
        return len(f"{self.first_name} {self.last_name}")
  
actor1 = Actor("Tom", "Cruise")    
print(actor1)
print(len(actor1))

a = 123_456
print(f"a is of type {type(a)}, its value is {a}")

