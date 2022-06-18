# Given two int values, return their sum. Unless the two values are the same, then return the square their sum.

# sum_squared(1, 2) → 3
# sum_squared(3, 2) → 5
# sum_squared(2, 2) → 16

sum_squared = lambda a, b : ((a + b) * (a + b)) if a == b else (a + b)

print(sum_squared(1, 2)) 
print(sum_squared(3, 2)) 
print(sum_squared(2, 2))




# Using List Comprehension, write a function that given a list of numeric values will generate and return a new list of values with each item in the original list cubed (raised to the third power)

# Input: [0, 1, 2, 4] 
# Output: [0, 1, 8, 64]

originalList = [0, 1, 2, 4]

newList2 = [x**3 for x in originalList]

print(originalList)
print(newList2)




# Given an int array length 2, return True if it contains a 2 or a 3.

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

has23 = lambda nums : True if((nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3)) else False

print(has23([2, 5])) 
print(has23([4, 3])) 
print(has23([4, 5]))




# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] % 2 == 0):
            count = count +1
    return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))




# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c
    
print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))   