def solution1(): 
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    full_name = f"{first_name} {last_name}"
    print(f"Your full name is {full_name}") 

def solution2():
    a = 1
    b = 2
    a, b = b, a
    print(f"a is {a}, b is {b}")

class Actor: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

def solution3():
    actors = [Actor("Tom", "Hanks"), Actor("Gary", "Oldman"), Actor("Casey", "Affleck"),
            Actor("Leonardo", "DiCaprio"), Actor("Eddie", "Redmayne")]

    actors_by_firstname = sorted(actors, key=lambda x: x.first_name) 
    print("Actor list ordered by first name:")
    for actor in actors_by_firstname:
        print(actor)  

    print("Actor list ordered by last name:") 
    actors_by_lastname = sorted(actors, key=lambda x: x.last_name) 
    for actor in actors_by_lastname:
        print(actor)   

def solution4():
    num_list = [1, 3, 13, 5, 8, 20, 302, 22, 35, 34, 15, 7, 29]
    target = 38
    
    dict = {}
    for index, num in enumerate(num_list):
        if target - num in dict: 
            print(f"found! Indeces are {dict[target - num]} and {index}\n"
                f"Values are {target - num} and {num}")
            return
        else:
            dict[num] = index

    print("Not found!")

def solution5():
    number_string = input("Input an integer please.\n")
    number = int(number_string)
    new_number = number + 99
    digits = len(str(new_number))
    print(f"{number} + 99 is {new_number}.")
    print(f"Number of digits for {new_number} is {digits}")

def solution6():
    hour_of_day = int(input("Input an hour of a day.\n"))
    if hour_of_day > 23 or hour_of_day < 0:
        print("Invalid hour!")
    elif hour_of_day == 0:
        print("12 am")
    elif hour_of_day < 12:
        print(f"{hour_of_day} am")
    elif hour_of_day == 12:
        print(f"{hour_of_day} pm")
    else:
        print(f"{hour_of_day - 12} pm")


def main():
    solution1()
    solution2()
    solution3()
    solution4()
    solution5()
    solution6()

if __name__ == "__main__":
    main()