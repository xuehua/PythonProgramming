import random
import heapq

# for loop for dictionary to iterate dictionary items.
dict = {"Alice":30, "Brad": 40, "Carey":50}
# approach 1
for name, age in dict.items():
    print(f"name: {name}, age: {age}")

for name in dict:
    print(f'name: {name}, age: {dict[name]}')

# update of dictionary can modify and add new items at the same time.
dict0 = {'A': 3, 'B': 4, 'C':4}
dict1 = {'A': 4, 'D': 7}
dict0.update(dict1)
print(dict0)

# use zip to initialize dictionary
dict = {x:y for x,y in zip('12345', 'ABCDE')}
print("dict using zip is: ", dict)

#write to file
file = open("numbers.txt", "w")

for i in range(50):
    number = str(random.randint(1, 10000))
    file.write(number + "\n")

file.close()

# Use heapq to find the k largest numbers in the numbers.txt.

def find_largest_k_numbers(k, filename):

    min_heap = []
    with open(filename, "r") as file:
        for line in file:
            number = int(line)
            heapq.heappush(min_heap, number)
            if len(min_heap) == k+1:
                heapq.heappop(min_heap)
            #print(min_heap)
    return min_heap

print(find_largest_k_numbers(10, "numbers.txt"))