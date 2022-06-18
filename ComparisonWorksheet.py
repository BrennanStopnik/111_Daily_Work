#Practice with Comparison Operators:

#Operators we've covered so far
    # > greater than
    # < less than 
    # >= greater than or equal to
    # <= less than or equal to
    # == equal

# Comparison Operators results in Bollean values

sample1 = 4 > 9
sample2 = 2 < 4

print(sample1)
print(sample2)

#Practice logical operators:

solution = False and False

print(solution) 

#if you ever see False in an AND statement, it's False. Only all True can result in True


#practicing with Control flow or If Statements

#step 1: write the keyt word If
#step 2: Follow that with parenthese
#step 3: Put a colon at the end
#steo 4: Have to put the condition in the Parentheses
    #if you put True or False in the pareentheses, it makes everythong below it whatever you hard codeed

if(True):
    name = "Brennan"
    print("Hello World,")
    print("How are you today?")
    print("I'M FINE".lower())
    print(name)

expression1 = 23 > 3
expression2 = 98 > 200
expression3 = "Brennan" < "Everyone else"


if(expression1): 
    print("Elon Musk messed up")
#worked because ex1 is a true statement

if(expression2): 
    print("Elon Musk messed up")
#did not work because ex2 is false

if(expression3):
    print("You're right")
#worked because ex3 is true

if(expression1):
    print("YAY")
else: 
    print("Bummer")
#printed "YAY" besause the statement was true

if(expression2):
    print("YAY")
else:
    print("Bummer")
#printed "Bummer" because the staement above was false


#working with Cheained conditionals

ex1 = 7 == 9
ex2 = 7 != 7
ex3 = False
ex4 = "Brennan" == "GOD"
ex5 = "Brennan" <= "GOD"

if(ex2):
    print("in the if statement")
elif(ex1):
    print("in the elif statement")
elif(ex3):
    print("hahahahaha")
elif(ex5):
    print("So Good!")
else:
    print("in the else statement")

#we can use as many Elif statements as necessary
#should always contain a else statement becasue thats good codee

#shorthand if statement -- "if a > b: print("A is greater")

a = 10
b = 25
if a > b: print("A is greater") 
else: print("b is greater")

#below is an example of a Nested if/elif/else statement
    #it's going to print the first true statement when it goes down the line

if(True):
    print("Hi")
    if(True):
        print("What's up?")
    else: 
        print("What's good")
else:
    if (True):
        print("Bye")
    else:
        print("Laters")

