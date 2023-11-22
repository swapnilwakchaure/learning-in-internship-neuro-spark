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


# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

def common_end(list1, list2):
    print(list1 == list2)

common_end([1, 2, 3], [7, 3]) # → True
common_end([1, 2, 3], [7, 3, 2]) # → False
common_end([1, 2, 3], [1, 3]) # → True
common_end([1, 2, 3], [1, 2, 3]) # → True


