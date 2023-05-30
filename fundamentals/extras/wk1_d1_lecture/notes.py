# Printing in Python vs JS
print("hello world")

#########################

# Variables
x = 5

#Re-declaring a variable
x = "Hello there!"

#########################

# Lists

pets = ["Bolo", "Appa"]

# How to add and remove from the list above
pets.append("Squirt") # adds to a list
pets.insert(2, "Jamal") # the number says where to put it and then what
# pets.pop() # removes from a list
pets.remove("Jamal") # needs the value of what you want removed

#########################

# Dictionary
owner = {"name": "Nomi", "age": 24, "location": "Monterey, CA"}

# Print "Nomi is 24 years old and lives in Monterey, CA"
print(f"{owner['name']} is {owner['age']} years old and lives in {owner['location']}.")
