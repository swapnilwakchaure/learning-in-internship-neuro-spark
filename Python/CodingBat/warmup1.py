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


