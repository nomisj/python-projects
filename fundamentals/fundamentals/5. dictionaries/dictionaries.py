# Creating Dictionaries
# There are 3 types of sets in Python. Lists enclosed by [], tuples enclosed by (), and dictionaries enclosed by {}.
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
# Above we created two dictionaries. Using literal notation, the key-value pairs are enclosed by curly brackets. The pairs are seperated by commas. The "Sun" string is a key and the "Sunday" string is a value.
# Also by creating an empty dictionary and adding some values.
# Each key in a dictionary must be unique. 

# Accessing Values
print(weekend["Sun"])
print(capitals["svk"])

# Removing Values - Two diffrent ways
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

# Nested Dictionaries
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

