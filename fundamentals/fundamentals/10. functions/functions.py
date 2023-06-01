# Basic example of a function

def add(a,b):  # function name: 'add', parameters: a and b
    x = a + b  # process
    return x  # return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

##############################

# Parameters and Arguments

def say_hi(name): # we have defined the say_hi function with one parameter called name.
    print("Hi, " + name)
    # invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# Let's modify our original say_hi function and observe the differences:
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output: >>>[2,4,10,16]




