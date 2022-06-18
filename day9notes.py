#Loops
    #range()
        #first argument is inclusive and the second argument is exclusive

    #For Loop reintroution
        #you can perform loops in a sequence/colection oblect directly or you can run a for lioiop ona range



#Steps to writinga for loop. 
    #1: Initialazation - to indicate where to start your counter and what represents the starting point 
        # "The 0 is the starting point but it can be any starting piont" and "counter is the method"
    #2: Condition - indicate wheather  or not to re-execute the startemet within a loop 
        # "its the range and the numbers"
    #3 ncrementiation/decrementation - indicate how much yo would like to increase or d3crease your counter by at each loop interation
        # "thats how it goes up" and can be 1, 2, or 3 arguments

    #the range(): handles the start, condition and increment

    #having a third argument tell python how to count. If you put (0,10,2) it counts every other nunmber, if the third argument is a 5 then it gowes up by 5

    #if you on;y have 1 argument python thinks you want tp start at 0, end when you tell it(the only argumnet) and that you want to go up by 1

#For loop tyoe 1: The range function

# #2 arguments
for counter in range(0,10):
    print(f"Brennan is currently at iteration number: {counter}")

# #1 argument
for counter in range(5):
    print(f"this is fun times: {counter}")

# #3 arguments
for counter in range(0,15,3):
    print(f"What is happening: {counter}")

# #count down
for counter in range(10,-1,-1):
    print(f"count down: {counter}")




myPeople = ["Arin", "Wolfie", "Soren"]

# #using the object itself - 
for counter in myPeople:
    print(f"Brennan loves {counter}")

# #using the range you need to call the item and the index
length = len(myPeople)
for counter in range(0, length):
    print(f"Brennan loves {myPeople[counter]}")


#Nested loops
    #create a loop inside another loop.
        #for loops 

# We have worked with data tyoes and vartiable  that can be stored as data
    #name = "Brennan"

#We have witked woith coeelection tyoes as well 
myList = ["Brennan", "Arin", "Wolfie"]
myDict = {"name": "Brennan", "age": 41}
myTuple = ("Brennan", "Arin", "Wolfie")

# #We can creatre a list inside of a list

myList2 = ["Brennan", ["Wolfie", "Soren", "Kaleb", ["friend", "daughter"]], "Arin"]

print(myList2[1][2])

print(myList2[1][3][0])


# #how to change something in the multi dimensional list above then print
#     # 1: extract the value ( where is it? how can I access it so it can ve modifueds)

friend = myList2[1][3][0]

friend = "son"

print(friend)

name = "todd"

todd = myList2[1][3][1]

todd = "todd"
print(todd)

Here = myList2[1][2]
Here = "Not Here"

print(Here)


newList = ["Brennan", ["shit husband", "shit father", "self centered"], "narcissist"]

for i in newList:
    print(i)
    print(type(i))
    for j in newList[1]:
        print(j)
        print(tyoe(i))

#Goal, print out all values in the list, even if it is in this specific list multi-dimensional
# 

#Loop control statements 
    #They alter the regulat flow of the loop
    #You can use keywords
        #Break
            #will transfer to the statement right after the loop
        #Continue
            #skips the statement following it and returns control to the beginning of the loops

#Modulus Operator
    #mod opreerateor is similaur to add, sutract, divide, and multiply in that it returns a number
    #the mod symbol is denoted with a %
    # it's the reminder after its gone into the other number
        #divide the left by the right 
            #if it comes back with a 0, it's a clean cut
    #4 % 2 => 0
    #9 % 2 => 1
    #7 % 3 => 3

print(7 % 4)                #3

example1 = 10 % 5           #clean cut
example2 = 23 % 16          #7
example3 = 98 % 76          #22
example4 = 978 % 4          #2
example5 = 128 % 244        #128 because it can't go in at all. Give back the left number if the right is too big

print(example3)