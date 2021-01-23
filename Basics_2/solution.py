import random
from types import prepare_class

def solution1():
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    dict = {}
    for word in input_words:
        key = ''.join(sorted(list(word)))
        if key in dict:
            dict[key].append(word)
        else: 
            dict[key] = [word]
    result = list(dict.values())
    print("=== Result for problem 1: ===")
    print(result)

def solution2():
    A = [1, 3, 8, 5, 12, 3, 23, 8]
    print("=== Result for problem 2: ===")
    print(A[::2])
    print(A[1::2])

def solution3():
    A = [1, 3, 8, 5, 12, 3, 23, 8]    
    result = [x*x for x in A if x % 2 == 1] 
    print("=== Result for problem 3: ===")
    print(result)

def pascal_triangle(numRows):
    result = [[1], [1,1]]
    if numRows < 3:
        return result[:numRows]
    
    for i in range(2, numRows):
        result.append([1]*(i+1))
        for j in range(1, i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result

def solution4():
    print("=== Result for problem 4: ===")
    for numRows in [1, 2, 5, 8]:
        print(f"numRows: {numRows}")
        result = pascal_triangle(numRows)
        print(f"pascal triangle: {result}")

def pascal_triangle_row(n):
    """ get the nth row of the poscal triangle"""
    row = [1] * n
    for i in range(1,n-1):
        row[i] = row[i-1] * (n-i)//i
    return row
    
def solution5():
    print("=== Result for problem 5: ===")
    for i in range(1,8):
        print(f"{i}th row: {pascal_triangle_row(i)}")

def solution6():
    lst = list("abcdefghijklmnopqrstuvwxyz")
    password_lst = []

    # get four letters from a-z
    for i in range(4):
        password_lst.append(random.choice(lst))
    
    # get four letters from A-Z
    lst = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(4):
        password_lst.append(random.choice(lst))
    
    # get two digts from 0-9
    lst = list('0123456788')
    for i in range(2):
        password_lst.append(random.choice(lst))

    # get two special symbol letters.
    lst = list("~!@#$%^&*+-/.,{}[]();:\\")
    for i in range(2):
        password_lst.append(random.choice(lst))

    # Random permutation. We can use random.shuffleor use the famous Fisher-Yates shuffles 
    # mentioned in https://en.wikipedia.org/wiki/Random_permutation
    random.shuffle(password_lst)

    password = ''.join(password_lst)
    print("=== Result for problem 6: ===")
    print(f"{password}")

def main():
    solution1()
    solution2()
    solution3()
    solution4()
    solution5()
    solution6()


if __name__ == "__main__":
    main()