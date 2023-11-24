import math

# # print(help(math))

# print(round(4.5)) # 4
# print(round(5.5)) # 6
# print(round(6.5)) # 6
# print(round(7.5)) # 8

# print(math.pi)
# print(math.e)
# print(math.inf)
# print(math.nan)
# print(math.log(math.e))
# print(math.sin(90))
# print(math.degrees(math.pi/2))
# print(math.radians(180))


import random
# it generates random integers from start to stop
# print(random.randint(0, 100))

# but by using .seed() method, it can gives same random numbers at every run
# print(random.seed(100))
# print(random.randint(0, 100))
# print(random.randint(0, 100))
# print(random.randint(0, 100))
# print(random.randint(0, 100))
# print(random.randint(0, 100))


mylist = list(range(0, 20))

# print(mylist)
print(random.choice(mylist))

# by using population, we can get multiple random numbers in at one go, (k = 10) means, number of random numbers you want

# SAMPLE WITH REPLACEMENT (with duplicates)
print(random.choices(population=mylist, k=10))

# SAMPLE WITHOUT REPLACEMENT (without duplicates)
print(random.sample(population=mylist, k=10))

random.shuffle(mylist)

print(mylist)

print(random.uniform(a=0, b=100))

print(random.gauss(mu=0, sigma=1))