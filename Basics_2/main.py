import copy

#help(id)
# Assignment, shallow copy and Deep copy
# Assignment
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

old_list[2][2] = 9
print(old_list, new_list)
print(id(old_list), id(new_list))

# Shallow copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = copy.copy(old_list)

old_list[2][2] = 9

print(old_list, new_list)
print(id(old_list), id(old_list[2]))
print(id(new_list), id(new_list[2]))

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

