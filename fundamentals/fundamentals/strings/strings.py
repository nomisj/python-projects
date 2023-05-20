#STRING LITERALS
# Strings are any sequence of charecters (letters, numerals, (/\#, etc)) enclosed in single or double quotes.
print("this is a sample string")

#CONCATENATING STRINGS & VARIBALES W/ THE PRINT FUCTION
# One of the first ways is by adding a comma after the string, followed by the variable. Note that the comma is outside the closing quotation mark of the string.
name = "Nomi"
print("May name is", name)
#The second way is by concatenating the contents into a new string, with the help of a +.
name = "Nomi"
print("My name is" + name)

#TYPE CASTING OR EXPLICIT TYPE CONVERSION
# If wanting to change a value's data type from one type to another, python does not know how to add a string and a number, but it can add two strings together. If we cast the number as a string, we will then be able to add the two values together.
print("Hello " + 42) # output: TypeError
print("Hello " + str(42)) # output: Hello 42
# Another example:
total = 35
user_val = "26"
total = total + user_val # output: TypeError
total = total + int(user_val) # total will be 61

# STRING INTERPOLATION
# We can also inject variables into our strings, which is known as string interpolation. There a few diffrent ways this can be done...
# F-STRINGS (Literal String Interpolation) - To construct a f-string, place an f right beofre the opening quatation. Then within the string, place any variables within curly brackets.
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

