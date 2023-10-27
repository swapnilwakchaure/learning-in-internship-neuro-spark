# WARMUP SECTION:

# 1. LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a,b))
    else:
        print(max(a,b))

# lesser_of_two_evens(2,4)
# lesser_of_two_evens(2,5)


# 2. ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(name):
    letter = name.split()
    print(letter[0][0] == letter[1][0])

# animal_crackers('Levelheaded Llama')
# animal_crackers('Crazy Kangaroo')


# 3. MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# def makes_twenty(n1,n2):
#     print(n1 == 20 or n2 == 20 or n1+n2 == 20)

def makes_twenty(a,b):
    if 20 in [a,b] or sum((a,b)) == 20:
        print(True)
    else:
        print(False)

# makes_twenty(20,10)
# makes_twenty(12,8)
# makes_twenty(2,3)


# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    if len(name) > 3:
        print(name[:3].capitalize() + name[3:].capitalize())
    else:
        print('name is too short')

# old_macdonald('macdonald')


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(str):
    print(' '.join(str.split()[::-1]))

# master_yoda('I am home')
# master_yoda('We are ready')
# master_yoda('Hello Word')


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# NOTE: abs(num) returns the absolute value of a number

def almost_there(num):
    if (abs((100 - num) <= 10 or abs((200 - num) <= 10))):
        print(True)
    else:
        print(False)

# almost_there(90)
# almost_there(104)
# almost_there(150)
# almost_there(209)


# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(mylist):
    for i in range(0, len(mylist)-1):
        if mylist[i] == 3 and mylist[i+1] == 3:
            return True
    return False

# res1 = has_33([1, 3, 3])
# res2 = has_33([1, 3, 1, 3])
# res3 = has_33([3, 1, 3])

# print(res1)
# print(res2)
# print(res3)


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(str):
    word = ''
    for letter in str:
        word = word + letter*3
    print(word)

# paper_doll('Hello')



# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(n1, n2, n3):
    total = sum((n1, n2, n3))
    while ( 11 in [n1, n2, n3] and total > 21):
        total = total - 10
    if total <= 21:
        print(total)
    else:
        print('BUST')

# blackjack(5, 6, 7)
# blackjack(9, 9, 9)
# blackjack(9, 9, 11)



# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(mylist):
    total = 0
    add = True

    for num in mylist:
        while add:
            if num != 6:
                total = total + num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)

# summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 11])


# CHALLENGING PROBLEMS

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(mylist):
    code = [0, 0, 7, 'x']
    
    for num in mylist:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

res1 = spy_game([1,2,4,0,0,7,5])
res2 = spy_game([1,0,2,4,0,5,7])
res3 = spy_game([1,7,2,0,4,5,0])

# print(res1, res2, res3)


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.
import math

def checkPrime(num):
    root = math.floor(math.sqrt(num))

    for i in range(2, root+1):
        if num % i == 0:
            return False
    return True

def countPrime(num):
    primelist = []
    primecount = 0

    for i in range(2, num+1):
        if checkPrime(i):
            primelist.append(i)
            primecount+=1
    
    print(primelist)
    print(primecount)


# countPrime(100)
