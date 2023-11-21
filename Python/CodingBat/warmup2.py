
# 1. Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    print(str*n)

# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

# 2. Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
    if len(str) >= 3:
        print(str[:3]*n)
    else:
        print(str*n)

# front_times('Chocolate', 2) # → 'ChoCho'
# front_times('Chocolate', 3) # → 'ChoChoCho'
# front_times('Abc', 3) # → 'AbcAbcAbc'


# 3. Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    print(result)

# string_bits('Hello') # → 'Hlo'
# string_bits('Hi') # → 'H'
# string_bits('Heeololeo') # → 'Hello'

# 4. Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result = result + str[:i+1]
    print(result)

# string_splosion('Code') # → 'CCoCodCode'
# string_splosion('abc') # → 'aababc'
# string_splosion('ab') # → 'aab


# 5. Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    count = 0
    if len(str) < 2:
        count = 0
    else:
        last_two = str[len(str)-2:]
        for i in range(len(str)-2):
            if str[i:i+2] == last_two:
                count = count + 1
    print(count)


# last2('hixxhi') # → 1
# last2('xaxxaxaxx') # → 1
# last2('axxxaaxx') # → 2

# 7. Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    print(count)
    

# array_count9([1, 2, 9]) # → 1
# array_count9([1, 9, 9]) # → 2
# array_count9([1, 9, 9, 3, 9]) # → 3


# 8. Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
    if 9 in nums[0:4]:
        print(True)
    else:
        print(False)

# array_front9([1, 2, 9, 3, 4]) # → True
# array_front9([1, 2, 3, 4, 9]) # → False
# array_front9([1, 2, 3, 4, 5]) # → False


# 9. Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
    numbers = [1, 2, 3, 'x']

    for i in range(len(nums)):
        if nums[i] == numbers[0]:
            numbers.pop(0)
    
    if len(numbers) == 1:
        print(True)
    else:
        print(False)

# array123([1, 1, 2, 3, 1]) # → True
# array123([1, 1, 2, 4, 1]) # → False
# array123([1, 1, 2, 1, 2, 3]) # → True


# 10. Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(str1, str2):
    count = 0

    for i in range(len(min(str1, str2))-1):
        if str1[i:i+2] == str2[i:i+2]:
            count = count + 1

    print(count)

string_match('xxcaazz', 'xxbaaz') # → 3
string_match('abc', 'abc') # → 2
string_match('abc', 'axc') # → 0
