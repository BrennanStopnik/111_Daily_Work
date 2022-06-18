# Mini Exercises for User inputs

    # Create a function called sum. This function takes in NO parameters. Instead, ask the user for two nmbers, add those two numbers and return their sum.

# Need to make sure the input is in the Function

'''
def sum():
    num1 = input("Input a number: ")
    num2 = input("Input another number: ")

    # Casting the input to an int below. Needs to be done or you end up with the input 
    sol1 = int(num1)
    sol2 = int(num2)
    final = sol1 + sol2
    print(final)
    return final

sum()


# Alternate, more efficient flow

def sum():
    num1 = int(input("Input a number: "))
    num2 = int(input("Input another number: "))
    print(num1 + num2)
    return num1 + num2

print(sum())

# semi colon for shortcut
def sum():
    num1 = int(input("Input a number: ")) ; num2 = int(input("Input another number: "))
    print(num1 + num2)
    return num1 + num2

print(sum())


'''

# How to get in done in one input
'''
def sum():
    (num1, num2)  = ( (int(input("Input a number: "))) , (int(input("Input another number: "))) )
    return num1 + num2

print(sum())
'''
# Night club. Everyone need to be over 21. Write input function where over 21 is True and under 21 is False
'''
def enter():
    age = int(input("How old are you?: "))

    if(age >= 21):
        return True
    else:
        return False
    
print(enter())
'''


# Python 3.4 and above Core Module: Statistics
    # Helps to calculate mathmatical statistics

import statistics

# list = [19, 38, 42, 44, 62, 13, 63, 14,]


'''
# Let's calculate the mean of the list
    # stats comes with a ".mean()"

mean = statistics.mean(list)
print(f"The mean of the data set is {mean}.")
print(type(mean))

# Another thing people can do with nemeric sets in stats in they get the "median" value
    # If it's a an even amount of numbers, it takes the 2 middle numbers and gives you the median of those number. 

median = statistics.median(list)
print(f"The median of the data set is {median}.")
print(type(median))

# High median is the hogher of the 2 numbers in the middle of an odd amount of numbers in the data set

hMedian = statistics.median_high(list)
print(f"This is the high median: {hMedian}")
print(type(hMedian))

# Low median is the lower of the 2 numbers in the middle of an odd amount of numbers in the data set

lMedian = statistics.median_low(list)
print(f"This is the high median: {lMedian}")
print(type(lMedian))

# Standard deviation

numbers = [100, 45, 22, 55, 94, 77, 89]

dev = statistics.stdev(numbers)
print(f"Original number were: {numbers}")
print(f"This is the standard deviation: {dev}")

'''

