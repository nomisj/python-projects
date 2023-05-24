#LISTS

# A list, also known as an Array in other languages, is a data type that allows you to hold groups of values.
# Lists are created with values inside of square brackets [], where each value is sepearted by a comma. After a list is created, it can still be updated by adding values and/or by deleting values.
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

# In python, the elements of a list do not have to be of the same data type. Can be a mixture. Example below:
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# Accessing Values
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

# Manupulating Lists
x = [1,2,3,4,5]
x.append(99)
print(x)
#the output would be [1,2,3,4,5,99]

x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];
