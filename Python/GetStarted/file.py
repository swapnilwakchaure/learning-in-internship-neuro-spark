# input/output basic files in python

# syntax for read or write file
# with open('filename.type', 'r/w') as file:
      # for write the content inside the file
#     file.write('this is a first line')
#     file.write('this is a second line')
#     file.write('this is a third line')
      # for read the content of file
#     file_content = file.read()
#     print(file_content)



# with open('myfile.txt', 'a') as file:
#     file.write('this is a fourth line')

# with open('myfile.txt', 'r') as file:
#     file_content = file.read()
#     print(file_content)


# with open('test.txt', 'w') as file:
#     file.write('hello world')

# with open('test.txt', 'r') as file:
#     print(file.read())

# file.close()


def mytuple(*args):
    print(args)

def mydict(**kwargs):
    print(kwargs)



# mytuple(1,2,3,4,5,8,3,2,1)
# mydict(fruit="apple")


def myfunc(*args, **kwargs):
    print('I like to eat {} {} !'.format(args[0],kwargs['food']))

# myfunc(10,20,30,fruit='veggie',food='eggs')

numb = '0 1 2 3 4 5 6 7 8 9 '
# na = 'A n t h r o p o m o r p h i s m'
name = 'Anthropomorphism'
# Output: 'aNtHrOpOmOrPhIsM'
# print(name.index('e'))

num = 0
str = ''

for letter in name:
    if num % 2 == 0:
        str = str + letter.lower()
    else:
        str = str + letter.upper()
    num = num + 1
# print(str)


# lambda expression, map and filter function
# 1. map function:

def square(num):
    return num**2

mylist = [1,2,3,4,5]
# print(list(map(square,mylist)))

name = ['Sally', 'Jelly', 'Andy']

def even_name(name):
    if len(name) % 2 == 0:
        return name
    else:
        return name[0]

# print(list(map(even_name,name)))

# 2. filter function

nums = [1,2,3,4,5,6,7,8,9,10]
def even_num(num):
    return num % 2 == 0

# print(list(filter(even_num, nums)))
# print(list(filter(even_num, range(1, 11))))

# 3. lambda expression
# start with the basic function
def square1(num):
    result = num**2
    return result

# by optimizing it one step
def square2(num):
    return num**2

# by converting above function into lambda expression
# lambda functions are anonymous function
square3 = lambda num: num ** 2
# print(square3(5))


# lambda expression using map function
# print(list(map(lambda num: num**2, range(1,11))))

# lambda expression using filter function

# print(list(filter(lambda num: num % 2 == 0, range(1, 11))))

# You have given names of list, grab the first letters of each name and write it in a list using lambda expression and map function
namelist = ['Sally', 'Jelly', 'Andy']
# print(list(map(lambda letter: letter[0], namelist)))


