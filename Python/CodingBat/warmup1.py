# 1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        print(True)
    else:
        print(False)

# sleep_in(False, False)
# sleep_in(True, False)
# sleep_in(False, True)

# 2. We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        print(True)
    elif not a_smile and not b_smile:
        print(True)
    else:
        print(False)

# monkey_trouble(True, True)
# monkey_trouble(False, False)
# monkey_trouble(True, False)

# 3. Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        print(sum((a,b))*2)
    else:
        print(sum((a,b)))

# sum_double(1, 2)
# sum_double(3, 2)
# sum_double(2, 2)

# 4. Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
    if n > 21:
        print((n-21)*2)
    else:
        print(21-n)

# diff21(19)
# diff21(10)
# diff21(21)

# 5. We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        print(True)
    else:
        print(False)

# parrot_trouble(True, 6)
# parrot_trouble(True, 7)
# parrot_trouble(False, 6)

# 6. Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundread(n):
    if (abs((100-n)) <= 10 or abs((200-n)) <= 10):
        print(True)
    else:
        print(False)

# near_hundread(93)
# near_hundread(90)
# near_hundread(89)

# 7. Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a,b):
    if 10 in [a,b] or sum((a,b)) == 10:
        print(True)
    else:
        print(False)

# makes10(9, 10)
# makes10(9, 9)
# makes10(1, 9)

# 8. Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    if negative:
        print(a < 0 and b < 0)
    else:
        print((a < 0 and b > 0) or (a > 0 and b < 0))

# pos_neg(1, -1, False)
# pos_neg(-1, 1, False)
# pos_neg(-4, -5, True)

# 9. Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    if str[:3] == 'not':
        print(str)
    else:
        print('not ' + str);

# not_string('candy')
# not_string('x')
# not_string('not bad')

# 10. Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    str = str[:n] + str[n+1:]
    print(str)

# missing_char('kitten', 1)
# missing_char('kitten', 0)
# missing_char('kitten', 4)

# 11. Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) > 1:
        str = str[len(str)-1] + str[1:len(str)-1] + str[0]
        print(str)
    else:
        print(str)

# front_back('code')
# front_back('a')
# front_back('ab')

# 12. Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
    if len(str) >= 3:
        print(str[:3]*3)
    else:
        print(str*3)

front3('Java')
front3('Chocolate')
front3('abc')

13.