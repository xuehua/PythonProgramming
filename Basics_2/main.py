import copy

#help(id)
# Assignment, shallow copy and Deep copy
# Assignment
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

old_list[2][2] = 9
print(old_list, new_list)
print(id(old_list), id(new_list))
print(old_list is new_list)  # is operator check whether both variables are pointing to one object.

# Shallow copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = copy.copy(old_list)

old_list[2][2] = 9

print(old_list, new_list)
print(id(old_list), id(old_list[2]))
print(id(new_list), id(new_list[2]))
print(old_list is new_list)  # is operator check whether both variables are pointing to one object.

#Deep copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = copy.deepcopy(old_list)

old_list[2][2] = 9
print(old_list, new_list)
print(id(old_list), id(old_list[2]))
print(id(new_list), id(new_list[2]))

# class property decorator
class Actor: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

actor = Actor("Tom", "Hanks")
print (actor.full_name)

# Initialize a matrix using * operator
# bad example in https://www.geeksforgeeks.org/initialize-matrix-in-python/
N=5
M=4
res0 = [ [0 for i in range(M)]] * N 
res1 = [[0] * M] * N 

res0[1][1] = 1
res1[1][1] = 1
print("res0:", res0)
print("res1:", res1)

# Correct way to do it 
res2 = [[0]*M for i in range(N)]
res2[1][1] = 1
print("res2:", res2)


# -(n//2) != -n//2
print(f"-(3//2): {-(3//2)}")
print(f"-3//2 : {-3//2}")
print(f"(-3)//2: {(-3)//2}")

# flatten a matrix
A = [[0,1,2],[3,4,5],[6,7,8]]
lst = [x for row in A for x in row ]
print(lst)
