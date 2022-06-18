#Whenever you're solvig a programming problem, think about IPO
    #Input, Process Output
        #Ask what am I given - Input
        #Ask what needs to be done - Process
        #Ask what meeds to be given back - Output

def sortThree(num1 = 9, num2 = 2, num3 = 89):
    smallestNum = 0
    middleNum = 0
    greatestNum = 0
    
    if(num1 < num3 and num1 < num3):
        smallestNum = num1
    elif(num1 > num2 and num1 > num3):
        greatestNum = num1
    else:
        middleNum = num1

    if(num2 < num1 and num2 < num3):
        smallestNum = num2
    elif(num2 > num1 and num2 > num3):
        greatestNum = num2
    else:
        middleNum = num2
    
    if(num3 < num1 and num3 < num2):
        smallestNum = num3
    elif(num3 > num1 and num3 > num2):
        greatestNum = num3
    else:
        middleNum = num3
    
    solution = (smallestNum, middleNum, greatestNum)

    print(type(solution))
    print(solution)
    return solution


print(sortThree) 






