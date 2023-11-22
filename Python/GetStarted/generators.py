def gen_cube_manual(n):
    cube_list = []
    for i in range(n):
        cube_list.append(i**3)
    return cube_list

# gen_cube_manual(10)

# for i in gen_cube_manual(10):
    # print(i)


# instead of writing this one, we use generator in python
# which can help to create a single entity with yield keyword

# by using generators, we do not need to store data (values) inside any data types (list)
# we can yeild it out.


def gen_cube_yield(n):
    for i in range(n):
        yield i**3

# for i in gen_cube_yield(10):
    # print(i)


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

# for i in gen_fibon(10):
    # print(i)

# fibonacci sequence: f(n) = f(n-1) + f(n-2)

def myfunc():
    for i in range(3):
        yield i

result = myfunc()
# print(next(result))
# print(next(result))
# print(next(result))

s = 'hello'

# for letter in s:
    # print(letter)

# but if we want to use next() function on it, it shows error
# we have iter() function there to help use next() to iterate a string

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

