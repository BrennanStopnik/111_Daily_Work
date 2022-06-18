# A service in AWS called cloud trail. That services' job it to tell the developer about what everyone is doing at all times. 


#Modules
    #When yo import a function, you are essentiall using a module.
    # a Module is a Python file with a .py extension

# Using modules
    # You can import a module using:
        # import <module-name>
    # You can access the content in the module using:
        # <module-name>.<entity-name>
    # You can also import a mosule using
        # from <module-name> impoort <entity-name>
    #
        # import <module-name>
        # <alias> = <module-name>.<entity-name>

# Core Modules: Comes with Python
import datetime
import random


# Custonm Module: Made it yourself
# import example

'''
1 A module is a file that contains a set of finction to incliuse in you r application. 
    Just like we were able tocreate our own sutom module/python_file
2 There are CORE puthon Modules, modules that you can install usingf PIP
    2a. oDjango is a tyoe of muodule to help with web framswork
    2b. There is Nujpy and Pande for data science
    2c. There is scikit-learn and tensorFlow for Machine learning

Bonus-- There's a distribution package thats dedicated to data scinece and machine learning that is called Anaconda

'''


# Core Modules = datetime
# today = datetime.date.today()
# print(today)

# PIP module -- camelcase
    # What is camecasing? it's when you don't use spaces to seperate words, you capitalize the first letter of every word but the first one


# Some CORE Modules
    # Math
    # Random
    # Calendar
    # Statistics

# PIP Modules
    # Python Install Package


# SUDO -- Super User Do

# Recall: <module>.<module_method>

import camelcase

# camelObj = camelcase.CamelCase()

# sentence = "brennan is the worst husband"
# sentence = camelObj.hump(sentence)
# print(sentence)

# Don't forget Py is OOP
    # Objects have :
        #1. Properties -- Variables and Data types/collection obects
        #2. Behaviors -- Methods / functions that operate on those properties

# working with the Random CORE module
    # The random mod is a set of methods that we are workingf with

        # we need to call the object
            #<module>.>Module_Method>

    # We are going to use the method called getrandbits(). Give you from 0 up to how many you specify.


randNum = random.getrandbits(4)
#  the number above is the amount of bits you can work with. Like 8 bits is 255.
print(f"The random number this time is: {randNum}")