#type - You can use this fuction to view the object type of any object.
print(type(24))
print(type(3.9))
print(type(3j))

#conversion - All Python objects have data type methods we can use to convert number types from one to another.
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#random number - Python does not have a built in random number generator, use the random module instead.
import random
print(random.randint(2,5)) # provides a random number between 2 and 5
