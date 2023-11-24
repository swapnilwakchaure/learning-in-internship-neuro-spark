# Convert the list of numbers into list of strings
# by doing this, there are multiple ways to do solve this problem

def string_one(n):
    return list(str(num) for num in range(n))

def string_two(n):
    return list(map(str, range(n)))

# string_one(10)
# string_two(10)




import time
# by using that we can calculate how many time required for functions to run the code


# CURRENT TIME BEFORE
start_time = time.time()
# RUN CODE
func1 = string_one(1000000)
# func2 = string_two(1000000)
# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time

# print(elapsed_time)
# for string_one() it takes 0.2323770523071289 seconds
# for string_two() it takes 0.2433478832244873 seconds




import timeit
# by using this built-in function, we get the actual faster function

stmt = '''
string_one(100)
'''

setup = '''
def string_one(n):
    return [str(num) for num in range(n)]
'''

func_one = timeit.timeit(stmt, setup, number=100000)
# print(func_one) # 1.786628199974075 second





