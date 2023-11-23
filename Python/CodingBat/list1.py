# 1. Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
    if (nums[0] == 6 or nums[len(nums)-1] == 6):
        print(True)
    else:
        print(False)

# first_last6([1, 2, 6]) # → True
# first_last6([6, 1, 2, 3]) # → True
# first_last6([13, 6, 1, 2, 3]) # → False


# 2. Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
    print(len(nums) >= 1 and nums[0] == nums[-1])

# same_first_last([1, 2, 3]) # → False
# same_first_last([1, 2, 3, 1]) # → True
# same_first_last([1, 2, 1]) # → True


# 3. Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

def common_end(list1, list2):
    if list1[0] == list2[0] or list1[-1] == list2[-1]:
        print(True)
    else:
        print(False)

# common_end([1, 2, 3], [7, 3]) # → True
# common_end([1, 2, 3], [7, 3, 2]) # → False
# common_end([1, 2, 3], [1, 3]) # → True


# 4. Given an array of ints length 3, return the sum of all the elements.

from functools import reduce

def sum3(nums):
    print(reduce(lambda x,y: x+y, nums))

# sum3([1, 2, 3]) # → 6
# sum3([5, 11, 2]) # → 18
# sum3([7, 0, 0]) # → 7


# 5. Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
    print(nums[1:] + [nums[0]])

# rotate_left3([1, 2, 3]) # → [2, 3, 1]
# rotate_left3([5, 11, 9]) # → [11, 9, 5]
# rotate_left3([7, 0, 0]) # → [0, 0, 7]


# 6. Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
    print(nums[::-1])

# reverse3([1, 2, 3]) # → [3, 2, 1]
# reverse3([5, 11, 9]) # → [9, 11, 5]
# reverse3([7, 0, 0]) # → [0, 0, 7]


# 7. Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
    result = lambda nums: [max(nums[0], nums[-1])] * len(nums)
    print(result(nums))

# max_end3([1, 2, 3]) # → [3, 3, 3]
# max_end3([11, 5, 9]) # → [11, 11, 11]
# max_end3([2, 11, 3]) # → [3, 3, 3]


# 8. Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
    if len(nums) > 1:
        print(sum((nums[0], nums[1])))
    elif len(nums) == 0:
        print(0)
    else:
        print(nums[0])

# sum2([1, 2, 3]) #→ 3
# sum2([1, 1]) #→ 2
# sum2([1, 1, 1, 1]) # → 2


# 9. Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(list1, list2):
    print([list1[1], list2[1]])

# middle_way([1, 2, 3], [4, 5, 6]) # → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) # → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) # → [2, 4]


# 10. Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
    if 2 in nums or 3 in nums:
        print(True)
    else:
        print(False)

# has23([2, 5]) # → True
# has23([4, 3]) # → True
# has23([4, 5]) # → False

