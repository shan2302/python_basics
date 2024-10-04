#Review:
#Create a function called greet().
def greet():
    #Write 3 print statements inside the function.
    print("Hello Shantanu")
    print("How do you Shantanu?")
    print("Isn't the weather nice today?")

#Call the greet() function and run your code.
greet()

#Function that allows for input\

def greet_with_name(Name):
    print(f"Hello {Name}")
    print(f"How do you do {Name}")

greet_with_name("Shantanu")

#functions with more than 1 input

def greet_with_more_than_1_input(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with_more_than_1_input("Shantanu", "Muzaffarpur,Bihar")
greet_with_more_than_1_input(name="Siddharth",location="Muzaffarpur,Bihar")