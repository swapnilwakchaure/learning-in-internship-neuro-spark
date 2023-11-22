from collections import Counter

# Counter helps to create a dictionary of items with its keys and values

mylist = [1,1,1,1,1,2,2,2,2,2,4,4,4,4]
mydict = Counter(mylist)
# print(mydict)

mystring = 'aaabbdcked'
mydict1 = Counter(mystring)
# print(mydict1)

sentence = 'How many times does each word show up this sentence with a word'
mydict2 = Counter(sentence.lower().split())
# print(mydict2)
# we can also able to convert it into tuples or tuple unpacking
# print(mydict2.most_common(3))
# we can also convert it into a list of individual items
# print(list(mydict2))


mydict3 = { 'key1': 'value1' }

# print(mydict3['key1'])
# print(mydict3['key2']) -> the key is not present and it shows error, and here the defaultdict
from collections import defaultdict

mydict3 = defaultdict(lambda: 0)

# print(mydict3['key2']) # this time is does not show any error, it gives default 0 values to the key2


# if in case we have a very large amount of data in tuples, then it is very difficult to get find the individual items
# in that case we use namedtuple to grab the items individually
from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(5, 'husky', 'sammy')

print(sammy)
