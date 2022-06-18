# # Everything in Python is an Object
#     # Examples
#         # strings
#         # Numbers
#         # Booleans
#         # Lists
#         # dictionaries
#         # Tuples
#         # Random
#         # Statisics

# # Every object has
#     # Properties - Metedata
#     # Methods - the work

# # Strings
#     # .upper()
#     # .lower()
#     # .swapcase()
#     # len()

# # Random:
#     #radrange()
#     # randint()

# # Statistics
#     # stdeb)()
#     # mean()
#     # median()
#     # hmedain()
#     # lmediaon()

# # How to create an object.
#     # First you have to create an class
#         # A class is a blusprint of an object
#             # A class contains the properties and methods that the object is to have
#                 # The difference is that you're defining it yourself

# # When creating a function in the class, you need to add self in the ()

# # All classes contain a Constructor Method. If yo do not supply one one will be made for you by default with only the argument self
#     # A constrictor methid job is to initialize a instance of your class
#     # It is the finction that runs when you initialize 
#         # This constructor has a name: def __init__():


#     # Properties
#         # shape
#         # species
#         # color
#         # ag3
#         # height
#         # gender
        
#     # Behaviors
#         # Speak
#         # Eat
#         # Sleep


class Animal:
    shape = ""
    species = ""
    color = ""
    age = 0
    height = 0.0
    gender = ""
    volume = 0.0
    sound = ""

# This takes the place of all the function we made   
    

    def speak(self):
        print("Noise...")

    def eat(self):
        print("Chomp")

    def sleep(self):
        print("Zzzz...")

# How to do the setter method

    def set_shape(self, shape):
        self.shape = shape
    
    def set_gender(self, gender):
        self.gender = gender

    def set_color(self, color):
        self.color = color
    
    def set_height(self, height):
        self.height = height

    def set_age(self, age):
        self.age = age
    
    def set_volume(self, volume):
        self.volume = volume

    def set_sound(self, sound):
        self.sound = sound
    
    def set_species(self, species):
        self.species = species

# # This takes the place of all the function we made   
#     def __init__(self, shape, gender, species, age, height, volume, color, sound):
#         self.shape = shape
#         self.gender = gender
#         self.species = species
#         self.age = age 
#         self.height = height
#         self.volume = volume
#         self.color = color
#         self.sound = sound

# animal1 = Animal()
# animal1.set_shape("circle")
# print(f"Your animals shape is: {animal1.shape}")
    
# animal2 = Animal()
# animal3 = Animal()
# animal4 = Animal()
    
# animal2.set_species("Dog")
# animal3.set_species("Cat")
# animal4.set_species("Bird")

# animal2.set_height(4)
# animal3.set_height(1)
# animal4.set_height(.2)

# animal2.set_sound("Sadness")
# animal3.set_sound("Meow bitch")
# animal4.set_sound("I said chirp mother fucker!")

# print(animal2.species)
# print(animal3.species)
# print(animal4.species)

# print(animal2.height)
# print(animal3.height)
# print(animal4.height)

# print(animal2.sound)
# print(animal3.sound)
# print(animal4.sound)

def __init__(self, age, sound):
        self.age = age 
        self.sound = sound
    
# animal2 = Animal(7, "ruff")
# animal3 = Animal(9, "Meow")
# animal4 = Animal(4, "Chirp")

# print(animal2)
# print(animal3)
# print(animal4)


# Another feature of an OOP    
    # This feature is known as "inheritence"

# You can inherit all of "Class A" properties and methods by extending it to "Class B"

# The way we do this in Python is
class Dog(Animal):
    breed = ""
    has_fur = False
    fur_color = ""
    has_floppy_ears = False
    

    def fetch():
        pass
    
    def zoomies():
        pass

    def chewing():
        pass

    def drool():
        pass

    def wagging_tail():
        pass

class Lion(Animal):
    

obj1 = Dog(9, "woof")
print(obj1)



    

