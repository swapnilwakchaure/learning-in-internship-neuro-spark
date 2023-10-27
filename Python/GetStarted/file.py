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
print(str)