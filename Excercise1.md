## Problem 1. Input function and string operations. 
1) Prompt "What is your first name?" and let user to input the first name
2) Prompt "What is your last name?" and let user to input the last name.
3) Based on 1 and 2, we can get the full name by combing first name and last name. Print 
out "Your full name is " and the full name. 

## Problem 2. Swap values of two variables
Assign two variables a, b with values 0, 1. Then swap the values of these 
two variables and print out their values.

## Problem 3. Lambda function, list, class and sort function.
1) Create a list of actors using the below Actor class 
2) Sort the list using first name and last name respectively.
Hints: Use lamba functions as keys of sort function to sort the actor list 
based on first name and last name respectively.

    class Actor: 
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name 

        def __str__(self):
            return f"{self.first_name} {self.last_name}"


## Problem 4. Dictionary usage. 
Given an array of integers, return indices of the two numbers such that they add up to a 
specific target. You may assume that each input would have exactly one solution, and you 
may not use the same element twice. 
Example: Given nums = 2, 7, 11, 15, target = 9, 
Because nums0 + nums1 = 2 + 7 = 9, return 0, 1.

## Problem 5. Input function and string/integer conversion.  
1) Prompt "Input a integer please" and let user input an integer.
2) Convert the input to an interger and assign it to a variable of number. 
3) Print out the number of digits that (number + 99) has.

