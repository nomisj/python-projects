# Printing in Python vs JS
print("hello world")

#########################

# VARIABLES
x = 5

#Re-declaring a variable
x = "Hello there!"

#########################

# LISTS

pets = ["Bolo", "Appa"]

# How to add and remove from the List above
pets.append("Squirt") # adds to a List
pets.insert(2, "Jamal") # the number says where to put it and then what
# pets.pop() # removes from a List
pets.remove("Jamal") # needs the value of what you want removed

#########################

# DICTIONARIES
owner = {"name": "Nomi", "age": 24, "location": "Monterey, CA"}

# Print "Nomi is 24 years old and lives in Monterey, CA"
print(f"{owner['name']} is {owner['age']} years old and lives in {owner['location']}.")

# Printing the length of a Dictionary
print("The length of the dictionary is:", len(owner))

# How to print the entire Dictionary
print("The entire dictionary is", owner)

#########################

# IF STATEMENTS

# if x is = 10 create an if statement to print true if x is less than 5 and false if greater

x = 10
if x < 5:
    print(True)
else:
    print(False)

x = 5
if x <= 5: # less than or equal to
    print(True)
else:
    print(False)
