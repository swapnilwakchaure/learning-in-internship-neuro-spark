import pdb

x = [1, 2, 3]
y = 2
z = 3

result_one = y + z
pdb.set_trace()
result_two = x + result_one

print(result_one)
print(result_two)