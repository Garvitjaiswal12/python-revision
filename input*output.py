#  python-revision
# 	           **BASIC INPUT OUTPUT**

# 1) Accept numbers from a user
"""n1=str(input("enter 1st no. "))
n2=str(input("enter 2nd no. "))
print(f"1st no. is ={n1} and 2nd no. is = {n2}")"""

# 2) Display three string “Name”, “Is”, “James” as “Name**Is**James”
# print("Name", "Is","James",sep="**")

# 3) Display float number with 2 decimal places using print()
"""n=float(input("enter decimal no."))
print(f"{n:.2f}")"""

# 4) Sum of two integers
# 5) Accept two integers from user and print the sum
#    Ex - The sum of 45 & 12 = 57
"""n1=int(input("n1 "))
n2=int(input("n2 "))
n3=n1+n2
print(f"{n1}+{n2}={n3}")
"""
# 6) Accept the User's name, age and print in following manner
#    Ex - Hello Shery, you are 12 years old.
"""name=str(input("name="))
age=int(input("age="))
print(f"Hello {name}, you are {age} years old.")"""
#                 **CONDITIONAL STATEMENTS** 
# 7) Take 3 int inputs from user and check and print the result.
# 	all are equal
# 	any of two are equal
# 	( use and or )
"""n1 = int(input("n1="))
n2 = int(input("n2="))
n3 = int(input("n3="))

if n1 == n2 == n3:
    print("all 3 equal")
elif n1 == n2 or n2 == n3 or n1 == n3:
    print("any 2 are equal")
else:
    print("distinct")
"""
# 8) Accept two numbers and print the greatest between them
n1 = int(input("n1="))
n2 = int(input("n2="))
if(n1!=n2):
    if(n1>n2):
       print("1st no. is greater")
    else:
        print("2nd no. is greater")
else:
    print("no.s are equal")
# 9) Accept the gender from the user as char and print the respective greeting message
#      Ex - Good Morning Sir (on the basis of gender)
# 10) Extend the previous program and handle the wrong inputs.
#       Print Good Morning sir for input m or M & Good morning Maam for input F or f 
#       else print Wrong Input
# 11) Accept an integer and check whether it is an even number or odd.
# 12) Accept name and age from the user. Check if the user is a valid voter or not.
#       Vaid - Hello Shery, You are a valid voter.
#       Invalid - Sorry Shery, you can't cast the vote.
# 	Part 2 - Print after how many years the user will be eligible
# 13) Accept the parameters and calculate the Compound Interest & print it on STDOUT (Use Math class methods)
# 14) Accept a year and check if it a leap year or not (google to find out what's a leap year)
# 15) Accept an english alphabet from user and check if it is a consonent or a vowel;

#               **ITERATIVE STATEMENTS**
# 16) Accept an integer and Print hello world n times
# 17) Print natural number up to n. 
# 18) Reverse for loop. Print n to 1.
# 19) Take a number as input and print its table
#        5 * 1 = 5
#        5 * 2 = 10 ... up to 10 terms
# 20) Sum up to n terms.
# 21) Factorial of a number
# 22) Print the sum of all even & odd numbers in a range seperately.
# 23) Print all the numbers which are either divisible by 3 or 5 in a range 
# 24) Print all the factors of a number.
# 25) Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43
# 26)  Accept a number and check if it a perfect number or not.
#       A number whose sum of factors(excluding number itself)  = Number 
#       Ex -  6 = 1, 2, 3 = 6
# 27) Separate each digit of a number and print it on the new line
# 28) Check if the number is Prime or not.
# 29) Accept a number and print its reverse
# 30) Accept a number and check if it is a palindromic number (If number and its reverse are equal)
#        Ex - 12321 - Reverse - 12321



#                    **String Problems**
# 31) Print string in reverse, its length, in uppercase, lowercase and copy into another string
# 32) Arrange string characters such that lowercase letters should come first
# 33) Count all letters, digits, and special symbols from a given string
#     Given: str1 = "P@#yn26at^&i5ve"
#     Expected Outcome:
#     Total counts of chars, digits, and symbols
#     Chars = 8
#     Digits = 3
#     Symbol = 4
# 34) Compare two strings without using inbuilt functions
# 35) Count Vowels from given string
# 36) Reverse a string
# 37) check string is palindrome or not

#                     **01 LIST PROBLEMS**
# 38) Accept List elements and reprint it
# 39) Print  List elements in reverse order
# 40) Print positive and negative elements of an List
# 41) Print list in ascending or descending order
# 42) Accept size n from user and create a n size List then take n inputs into the and finally 
#    Print the sum of all elements in the List in the following manner
#    10 + 20 + 30 = 60
# 43) Mean of List elements.
# 44) Find the greatest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
# 45) Find the smallest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index
# 46) Find the second greatest element0 
#    {2, 96, 69, 77, 145, 20} = Second greatest element = 96
# 47) Check if List is sorted or not.
# 48) Pallindromic List - Write a program to check if elements of an List are same or not it read from front or back Example : are= [2,3,15,15,3,2]



#                       **Dictionary (hash map) questions**

# 49) Write a Python program to iterate over dictionaries using for loops
# 50) Write a Python script to merge two Python dictionaries.
# 51) Write a Python program to sum all the values in a dictionary.
# 52) Convert a list to dictionary 
# 53) count the frequency of each elements
# 54) Write a Python program to combine two dictionary by adding values for common keys.



#                       **Patterns questions**

# 55) Right Triangle - Star
# 	*
# 	* *
# 	* * *
# 	* * * *
# 	* * * * *
# 56) Right Triangle - Number
# 	1
# 	1 2
# 	1 2 3 
# 	1 2 3 4
# 	1 2 3 4 5
# 57) Right Triangle - Alphabet
# 	A
# 	A B
# 	A B C
# 	A B C D
# 	A B C D E



# *****************----Project making------*****************

# 58) File handling Project
# 59) A normal game
# 60) OOPS Project

# amstrong no.
# palindrome no. 
# fibonacci 
# fibonacci using recursion
# calculator 
