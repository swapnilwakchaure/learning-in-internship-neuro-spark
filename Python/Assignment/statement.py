# 1. Use for, .split() and if to create a statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
# print([letter for letter in st.split() if letter[0] == 's']) # by using list comprehension

for word in st.split():
    if word[0] == 's':
        # print(word)
        pass

# 2. Use range() to print all the even numbers from 0 to 10.
# print(list(range(0, 11, 2)))

# 3. Use a List Comprehension to create a list of all numbers between 1 to 50 that are divisible by 3.
# print([num for num in range(1, 50) if num%3==0])

# 4. Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2==0:
        # print(f'{word} --- > has an even lenght')
        pass


# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# for num in range(1,100):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)


# 6. Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

# print([letter[0] for letter in st.split()])


mylist = [('smith', 300), ('john', 330), ('neil', 420), ('max', 120)]


def employee_of_the_year(mylist):
      employee_name = ''
      employee_hour = 0
      for name,hour in mylist:
            if  hour > employee_hour:
                   employee_hour = hour
                   employee_name = name
            else:
                   pass
      return employee_name

name = employee_of_the_year(mylist)
print(name)