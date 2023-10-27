# print('hello world');

i = 10;
# print(i);

# indexing
mystring = "hello world"
# print(mystring[4])
# output = o

# slicing
# print(mystring[2:])
# output = llo world

mystring = "abcdefhij"
# print(mystring[::])
# it prints all the string like print(mystring)

# print(mystring[start:end:step])

# reverse the string using slicing
# print(mystring[::-1])

# with open('myfile.txt', 'w') as file:
#     # write content to the file
#     file.write('this is a first line\n')
#     file.write('this is a second line\n')
#     file.write('this is a third line\n')

with open('myfile.txt', 'r') as file:
    file_content = file.read()
    # print(file_content)


# set datatype
mySet = {1,1,2,3}
# print(type(mySet))
    

# ternary operator

name = "John";
# print(f"welcome {name} to our house")


# for loop

mytuplelist = [(1,2),(3,4),(5,6),(7,8)]
# it is called tuples in list and also called tuple unpacking
# for loop with if, else condition
for a,b in mytuplelist:
    if a >= 3:
        print(a)
    else:
        print(b)


# USEFUL OPERATORS IN PYTHON
#  1. Range (start, stop, step)
print('list of even numbers using range')
print(list(range(0, 11, 2)))

#  2. Enumerate 
# it creates an index and gives output in tuple format
print('creates tuple using enumerate')
for item in enumerate('abcd'):
    print(item)

# importing random
import random
mylist = [1,2,3,4,5]
random.shuffle(mylist)
print('shuffle the whole list')
print(mylist)

print('randint gives random integer')
print(random.randint(0,30))


# create input box which run in the termial and gives output as in string format
name = input('Please enter your name: ')
print(f'Welcome {name} to our home')


# Convert given celsius temperature list to fahrenheit temperature list.

celsius = [0, 10, 20, 34.5, 38]
fahrenheit = [( (9/5)*temp + 32 ) for temp in celsius]
print('list comprehension')
print(fahrenheit)

# if, else statement inside the list comprehension
# lets create a list which prints if number is even print number otherwise print "odd"

evenOddList = [num if num%2==0 else "odd" for num in range(0, 11)]
print('even odd list using list comprehension')
print(evenOddList)


# nested for loops in list comprehension, create a list
print('nested for loops in list comprehension')
nestedList = [num1*num2 for num1 in [2,4,6] for num2 in [1,10,100]]
print(nestedList)
