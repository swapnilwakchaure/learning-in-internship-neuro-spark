# Errors and Exceptions Homework

# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

# for i in ['a','b','c']:
    # print(i**2)

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print('It shows type error in your code')
except:
    print('An error occurs')

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
# 
# x = 5
# y = 0
# 
# z = x/y

x = 5
y = 0

try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print('It shows zero division error')
except:
    print('Mathematical error')
finally:
    print('All Done')

# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            number = int(input('Enter Your Number: '))
        except:
            print('Woops! Wrong Input')
            continue
        else:
            print(f'Square of a number {number} is {number**2}')
            break
        finally:
            print('All Done')

ask()