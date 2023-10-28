# Functions and Methods Homework

# 1. Complete the following questions: ____ Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as (4/3)pi r**3

def vol(radius):
    print((4/3)*(3.14)*(radius**3))

# vol(2)

# 2. Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num >= low and num <= high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')

# ran_check(30, 2, 7)

# 3. Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!

# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33

def up_low(str):
    upper = 0
    lower = 0

    for letter in str:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    print('No. of Upper Case Characters : ',upper)
    print('No. of Lower Case Characters : ',lower)

# up_low('Hello Mr. Rogers, how are you this fine Tuesday')


# 4. Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(mylist):
    unique = []
    for num in mylist:
        if num not in unique:
            unique.append(num)
    print(unique)

# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# 5. Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(mylist):
    product = 1
    for num in mylist:
        product = product * num
    print(product)

# multiply([1, 2, 3, -4])



# 6. Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

def palindrome(str):
    str = str.replace(' ','')
    if (str == str[::-1]):
        print(True)
    else:
        print(False)

# palindrome('helleh')
# palindrome('nurses run')


# 7. Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: You may want to use .replace() method to get rid of spaces.

import string

def ispanagram(str, alphabet = string.ascii_lowercase):
    # all 26 lower case alphabet letters
    # it sets all unique characters
    alphabet = set(alphabet)
    
    # remove space from the sentence
    str = str.replace(' ','')

    # lowercase all the words in the string
    str = str.lower()

    # it sets all unique characters
    str = set(str)

    if str == alphabet:
        print(True)
    else:
        print(False)

# ispanagram('The quick brown fox jumps over the lazy dog')
