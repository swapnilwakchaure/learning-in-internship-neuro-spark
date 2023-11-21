import math

# 1. Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(str):
    print(f'Hello {str}!')

# hello_name('Bob') # → 'Hello Bob!'
# hello_name('Alice') # → 'Hello Alice!'
# hello_name('X') # → 'Hello X!'


# 2. Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a, b):
    print(a+b+b+a)

# make_abba('Hi', 'Bye') # → 'HiByeByeHi'
# make_abba('Yo', 'Alice') # → 'YoAliceAliceYo'
# make_abba('What', 'Up') # → 'WhatUpUpWhat'


# 3. The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
    print(f'<{tag}>{word}</{tag}>')

# make_tags('i', 'Yay') # → '<i>Yay</i>'
# make_tags('i', 'Hello') # → '<i>Hello</i>'
# make_tags('cite', 'Yay') # → '<cite>Yay</cite>'


# 4. Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
    result = ''
    for i in range(len(out)):
        if i == 2:
            result = result + word + out[i]
        else:
            result = result + out[i]
    print(result)

# make_out_word('<<>>', 'Yay') # → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') # → '<<WooHoo>>'
# make_out_word('[[]]', 'word') # → '[[word]]'


# 5. Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(str):
    st = str[len(str)-2:]
    print(st*3)

# extra_end('Hello') # → 'lololo'
# extra_end('ab') # → 'ababab'
# extra_end('Hi') # → 'HiHiHi'



# 6. Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
    if len(str) < 3:
        print(str)
    else:
        print(str[:2])

# first_two('Hello') # → 'He'
# first_two('abcdefg') # → 'ab'
# first_two('ab') # → 'ab'


# 7. Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    length = math.floor(len(str)/2)
    print(str[:length])

# first_half('WooHoo') # → 'Woo'
# first_half('HelloThere') # → 'Hello'
# first_half('abcdef') # → 'abc'


# 8. Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end(str):
    print(str[1:len(str)-1])

# without_end('Hello') # → 'ell'
# without_end('java') # → 'av'
# without_end('coding') # → 'odin'


# 9. Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

def combo_string(str1, str2):
    short = min(len(str1), len(str2))
    long = max(len(str1), len(str2))

    if short == len(str1):
        short = str1
        long = str2
    else:
        short = str2
        long = str1
    
    print(short+long+short)

# combo_string('Hello', 'hi') # → 'hiHellohi'
# combo_string('hi', 'Hello') # → 'hiHellohi'
# combo_string('aaa', 'b') # → 'baaab'


# 10. Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(str1, str2):
    print(str1[1:]+str2[1:])

# non_start('Hello', 'There') # → 'ellohere'
# non_start('java', 'code') # → 'avaode'
# non_start('shotl', 'java') # → 'hotlava'


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
    result = ''
    if len(str) <=2:
        print(str)
    else:
        result = result + str[2:] + str[:2]
        print(result)

left2('Hello') # → 'lloHe'
left2('java') # → 'vaja'
left2('Hi') # → 'Hi'