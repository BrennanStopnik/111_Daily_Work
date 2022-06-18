'''

Input and output files
    We have worked with a bunch of different things like subtrcating and adding or any type of arithamtic.
    python has different one liners
    These one liners come at a price. THere is a lot going on in the backend. To the naked eye it can feel like magic
    These aare only god when you understam what is really happening in the language.

Expressions ate one liners that evaluate to some value or data type and those data types as opposed to statements can be stored in a variable or passed into anouther function
    Expressoins == 
    x = brennan
    num = 9

Not an expression but a statement

if(x == num):
    print(x)
else:
    print(num)

Not and expression but a function

def add(x,y):
    return x + y

The real question is can we turn a statement or function into an expression? We can!

Bouncer function
'''



# You don't need the def():. You can do this fucntion without this. Look Below
def bouncer():
    userInput = int(input("Enter you age as a number, please: "))
    if(userInput >= 21):
        print("You're good to go.")
    else:
        print("You're not good!")

bouncer()

userInput = int(input("Enter you age as a number, please: "))
    if(userInput >= 21):
        print("You're good to go.")
    else:
        print("You're not good!")



# Doing the same thing from above without the extra shit
# This conditional statement expression is known as a Ternary
# userInput = int(input("Enter you age as a number, please: "))

# This is the one liner for an "If and Else" statement


canDrink = "You're good to go" if userInput >= 21 else "You're not good"

print(type(canDrink))
print(canDrink)


# Just like Ternary statements can turn if?else statemenets into one liners. Lambda does the came thing for functions
    # In other languages they're called anonynous functions

    # you can see this when you don't want to us a fumction twixe in a program. 

def add(x,y):
    return x + y

# Good but not a one liner. Also can't really store that value in as a variable or pass it in an argument to anouther function.


add = lambda x,y : x + y

print(add(3,4))

# other way to do it
sub = lambda x,y : x - y

solution = sub(4,2)
print(solution)


# The ways to change things into a TERNARY

# Full function

def specialAdd(x,y):
    if((x + y) > 21):
        return True
    else:
        return False

# Funbction with Ternary      

def specialAdd(x,y): 
    return True if ((x + y) > 21) else False

print(specialAdd(12,10))

# Function with Ternary and Lambda

specialAdd = lambda x,y : True if ((x + y) > 21) else False

print(specialAdd(14,13))

# Mapping. We take an object (scollection or sequence). and you call the method .map()
    # collectionOblect.map(some_function())  takes in a function aws an argument. and maps that function to the obkect


'''
- In python 3.4+ they introduced this shorthand notation of creating a list. It's not recommended if you're working wothj a Junior. They can be hard to understand.
- Many time in this course we have generated Lists, Tuples andor Dictionaries tin order to colve out problems.
- We have had to rely on the methods on the oblect

'''

originalList = [1, 2, 3, 4, 5]

newList = []
for i in range(len(originalList)):
    newList.append(originalList[i] ** 2)

print(originalList)
print(newList)

# There's something that's even easier than the last expression
    # It's called list comprehension and it interprets things the same way.

'''

            1st arg     2nd arg         3rd arg
newList = [ expression for item in iterable/sequence/collection]

1st = 
2nd
3rd - list, tuple, dict

What's inportant ot understand is that these one liners come at a price for a new developer and that it utilizes a bunch of fundementals in one expression that it can be tough to interpret

'''

originalList = [1, 2, 3, 4, 5]

newList2 = [x**3 for x in originalList]
newList3 = [num+5 for num in originalList]

print(originalList)
print(newList2)
print(newList3)

# To be more clear
    # 1. x**3 is the expression
    # 2. x within the "fpr x in" after the expression represents each item in your list
    # 3. originalList is the origia=nal iteravble/sequence/collection that you are referring to

li = []
for i in range(10):
    li.append(i)

print(li)

newList = [li for li in range(10)]

print(newList)

# Change ranmge of number in range function

newList = [li for li in range(1,11)]

print(newList)

# Change range to above 1 by adding 1 to the list in li

newList = [li + 1 for li in range(10)]

print(newList)

# In list Comp, we can add a 4th argument in that expression as a conditional

# Create a function called evenNums that takes in a list of numveres as a parameter and returns a new list with only the even numbers.
    # Use anything we know.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNums = [en for en in li if en % 2==0]

print(evenNums)


# Things we learned yesterday
#     List comprehension - Let's you create a list by using an expression or one-liner
#     Ternary Operators - Turned If/Else statements to Expressions
#     Lambda - An Expression that represents a function in one liner

# What is an expression
#     It's a line of codt that evaluates to some data or value
#         That data and / or value can be stored as a variable or passed in as an argument into a function

example = [2, 3, 4, 5, 6]


# Notes on Web Development
#     WHen you think of mapping, something you use is a DOM. The whole purpose of the DOM is to pair/join a function. with some component of your sebsite to make it "interactive".

#     With the map funmction, the map() method will map a fumction to a list/collevtion/sequence

squared = []
for i in range(len(example)):
    squared.append(example[i] **2)

print(example)
print(squared)

# When mapping values, it's a value. When you want a list, cast it into a list ie. list()

# The map method takes two arguments
#     1. The funmction yo want it to run
#     2. The oblect/colleciton/sequence you're running the function on

def squared(x):
    return x ** 2

squared2 = list(map(squared, example))

# Creating the same function above where you define a function then write the argument in one line using Lambda

squared2 = list(map(lambda x : x ** 2, example))

print(example)
print(squared2)

# 1. Write a Python program to triple all numbers of a given list of integers.

li = [1, 2, 3, 4, 5, 6, 7, 8]

triple = list(map(lambda x : x * 3, li))

print(li)
print(triple)


# 2. Write a Python program to add three given lists using Python map and lambda

li1 = [1, 2, 3]
li2 = [4, 5, 6]
li3 = [7, 8, 9]

addItUp = list(map(lambda x,y,z : x + y + z, li1, li2, li3))

print(li1)
print(li2)
print(li3)
print(addItUp)

# 3. Write a Python program to listify the list of given strings individually using Python map

li = ["dog", "cat", "bird", "snake"]

list2 = list(map(list, li))

print(li)
print(list2)

# 5. Write a Python program to square the elements of a list using map() function.

nums = [5, 10, 15, 20, 25]

squared = list(map(lambda x : x **2, nums))

print(squared)

# 6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.

letters = ['a', 'A', 'b', 'g', 'R', 'e', 'F',]

def cases(i):
    return str(i).upper(), str(i).lower()
print(letters)

result = map(cases, letters)
print(set(result))

# We are going to cover the filter methods. Filter woekrks a lot like map, except

# Conclude List Conprehension
# Start Dictionary Comprehension

# How to check if a number is even.

userInput = int(input("Pick a number, any number: "))
if(userInput % 2 == 0):
    print("That's an even number")
else:
    print("That's an odd number")


# Can be for any multiple. This is for 7

userInput = int(input("Pick a number, any number: "))
if(userInput % 7 == 0):
    print("That's a multiple of 7")
else:
    print("That's not a multiple of 7 ")

def evenNumbers(dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]):
    evenNumsOnly = []
    for i in range(len(dataset)):
        if (dataset[i] % 2 == 0):
            evenNumsOnly.append(dataset[i])
    print(evenNumsOnly)
    return evenNumsOnly

evenNumbers()

# Using Filter
    # Using this to get 

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

evenNumbs = list(filter(lambda x : x % 2 == 0, dataset))

# Same thing using the list Comprehension instead of filters

evenNumbs2 = [en for en in dataset if en % 2==0]

# Ternary Expressions: These change the If/Else statement to expressions which can be evaluated in one line

print(evenNumbs)
print(evenNumbs2)


# Tuple Comprehension 
myTuple = (x for x in dataset)
myList = [x for x in dataset]

print(tuple(myTuple))
print(type(tuple(myTuple)))
print(myList)
print(type(myList))


# Dict Comprehension
    # myDict = {k:v for x in dataset}
    #     you need key value pairs, not just x for x.

    # Lists have append. 
    # Dicts you have to assign the value

myDict = {}

for i in range(10):
    if(i % 2 == 0):
        myDict[i] = i ** 2

print(myDict)

newDict = {x : x**2 for x in range(10) if  x%2==0}
print(newDict)

fahrenheit = {"t1": 23, "t2": 56, "t3": 98, "t4": 0}

# Values is the values set above
print(fahrenheit.values())
print(type(fahrenheit.values()))

# Keys tells me the keys above
print(fahrenheit.keys())
print(type(fahrenheit.keys()))

# As a function
def toCelsius(x):
    return float((5)/9) * (x-32)

print(toCelsius(77))

# As a dict comprehension

celsius = list(map(lambda x : (float(5)/9) * (x-32), fahrenheit.values()))

print(celsius)

# Zip()
    #Just like lists have map, dict has zip
    # It takes keys and values form whatever you have and makes what you want into a dict.

newDict = dict(zip(fahrenheit.keys(), celsius))

print(newDict)

# All the above stuff done in one line
    # Items is a way to get the whole dict as (key , values) in Individual tuples

fahrenheit = {"t1": 23, "t2": 56, "t3": 98, "t4": 0}
print(fahrenheit.items())

# k is for key
# v is for value
# The key will be the same but the value will be the equation in the v spot
newDict2 = {k:(float((5)/9) * (v-32)) for (k,v) in fahrenheit.items()}

# Doing the same thing but adding another parameter at the end.
newDict2 = {k:(float((5)/9) * (v-32)) for (k,v) in fahrenheit.items() if v < 25}

print(newDict2)


# Today's review
    #1. Mapping in Py  
    #2. Filter in Py
    #3. Completed List Comp using Conditionals
    #4. Dictionary Comp
    #5. Lambda Expression
    #6. Ternary Expression


# File Manipulation, File input and output
    # All things python are python_obj.python_method()
    # there is probably some object that represents the file.
    # There is probably some method that operates on that object.
