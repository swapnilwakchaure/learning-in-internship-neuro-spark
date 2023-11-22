# def hello():
#     print('hello function')

# greet = hello

# # print(greet())


# def hello1(name="Jose"):
#     print('the hello1() function will be executed!')

#     def greet():
#         return '\t this is greet() function inside hello1()'
    
#     def welcome():
#         return '\t this is welcome() function inside hello1()'
    
#     # print(greet())
#     # print(welcome())
#     print('this is the end of the hello1() function')

#     if name == "Jose":
#         return greet
#     else:
#         return welcome

# myfunc = hello1()

# print(myfunc())


def param_func(other_func):
    print('Other function code run here')
    print(other_func())
    print('decorator function done')

# def decorator():
#     print('it is decorator function')

# param_func(decorator)

@param_func
def decorator_func():
    print('decorator function')

