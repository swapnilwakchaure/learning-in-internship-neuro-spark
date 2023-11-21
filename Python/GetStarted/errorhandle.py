# if, else condition

# number1 = 10
# number2 = 10

# if number1 + number2:
#     print(number1+number2)
# else:
#     print('Hey! you are path was wrong')



# try, except, else condition

# try:
    # result = number1 + number2
    # print(result)
# except:
    # print('hey! it looks like you are not adding correctly')
# if there is no error in your code then else block will execute
# else:
    # print('Adding correctly!')



# try, except, finally

# try:
    # f = open('testfile', 'w')
    # f.write('write the test line')
    # print('file writing successfully')
# except TypeError:
    # print('hey this shows type error')
# except OSError:
    # print('hey this shows os error')
# except:
    # print('all other exception!')
# finally:
    # print('I always run ')



# write a function which takes only numbers as a input otherwise it run until get a number

def ask_for_int():
    while True:
        try:
            number = int(input('Please provide a number: '))
        except:
            print('woops that is not a number')
            continue
        else:
            print(f'Number is: {number}')
            break
        finally:
            print('End of try/except/finally block')

# ask_for_int()


