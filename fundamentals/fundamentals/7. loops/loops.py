# For Loops through Strings
for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

#############################################
# For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

#############################################
# For Loops through Dictionaries - the iterator (k) is each of the keys of the dictionary
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

#############################################
# WHILE LOOPS
# Another way of looping while a certain condition is true.

# for loop i.e:
for count in range(0,5):
    print("looping =", count)

# You can rewrite it as a while loop
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

# The basic syntax for a while loop looks like:
# while <expression>: do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#############################################
# ELSE LOOPS
# There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? We can then use an else statement with our while loop. Yes, that is right, else in a loop.
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
