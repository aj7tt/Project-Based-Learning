"""
Python3 part-01

fundamental 
control flow 
Functions 
data structure 
 

"""

# @Hello, World! Program
print("Hello, World!")

# @Variables and Literals
a = 5
print("a =", 5)
a = "High five"
print("a =", a)

# @Operators
x = 14
y = 4

# Add two operands
print('x + y =', x+y) # Output: x + y = 18

# Subtract right operand from the left
print('x - y =', x-y) # Output: x - y = 10

# Multiply two operands
print('x * y =', x*y) # Output: x * y = 56

# Divide left operand by the right one 
print('x / y =', x/y) # Output: x / y = 3.5

# Floor division (quotient)
print('x // y =', x//y) # Output: x // y = 3

# Remainder of the division of left operand by the right
print('x % y =', x%y) # Output: x % y = 2

# Left operand raised to the power of right (x^y)
print('x ** y =', x**y) # Output: x ** y = 38416


# @Get Input from User
# inputString = input('Enter a sentence:')

# @Type Conversion
### Implicit
num_int = 123     # integer type
num_flo = 1.23   # float type
num_new = num_int + num_flo
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))         #converted to float
 
### Explicit Conversion
num_int = 80  # int type
num_str = "120" # str type

# explicitly converted to int type[[[ int(), float(), str() ]]]
num_str = int(num_str) 
print(num_int+num_str)      #200


#@Python data Types

# Output: <class 'int'>
print(type(5))

# Output: <class 'float'>
print(type(5.0))

c = 5 + 3j
# Output: <class 'complex'>
print(type(c))



# @Python Data Structures
###Lists[]

my_list = []        #empty list
my_list = [1, 2, 3]     # list of integers
my_list = [1, "Hello", 3.4]     # list with mixed data types

language = ["French", "German", "English", "Polish"]
# Accessing first element
print(language[0])     # Output:French
# Accessing fourth element
print(language[-1])   #negative indexing Output: polish

"""
1. Tuple is similar to a list except you cannot change elements of a tuple once
it is defined. Whereas in a list, items can be modified.
2. Strings are immutable.
3. A set is an unordered collection of items where every 
element is unique (no duplicates).
4. Dictionary is an unordered collection of items. While other compound data types have 
only value as an element, a dictionary has a key: value pair.

"""


#@Tuple
language = ("French", "German", "English", "Polish")
print(language[-1]) # Output: Polish
del language        #del tuple 

#@ String

#declare and initializing strings
myString = "hello ajit"

#acess character from the string
print(myString[6])      

#slicing 
print(myString[2:-2])   #start from index2 to 2last

#@set
# set of mixed datatypes
mySet = {1.0,1, "Hello", (1, 2, 3)}
print(mySet)

#sets methods
mySet.add(7)
mySet.update([1, 2, 5])
mySet.remove("Hello")
print(mySet)


person = {'name':'ajit', 'age': 20, 'salary': 400000}
print(person['age']) # Output: 20

#method in dictionary
person['name'] ="aj7t"
person['age'] =21
del person['salary']
print(person) # Output: name & age


##range function

numbers = range(1, 10, 2)

print(list(numbers)) # Output: [1, 3, 5, 7, 9]
print(tuple(numbers)) # Output: (1, 3, 5, 7, 9)
print(set(numbers)) # Output: {1, 3, 5, 7, 9}

print(dict.fromkeys(numbers, 50))
# Output: {1: 50, 3: 50, 5: 50, 7: 50, 9: 50}


#@control flow in python 
num = 7 

if num>0:
    print("i am positive person")
elif num==0:
    print("i am neutral")
else:
    print("i am negative")



#@ loops (Finding summ till x)

##using while loop 
x=1  #iteration starts from 1
sum=0;
while x<=100:
    sum+=x
    x =x+1      

print(sum)


##using for loop 
numbers=[1, 3, 5, 7, 9,20]
sum1=0;
for i in numbers:
    sum1+=i
print(sum1)

## break, continue and  pass statements in loops

for val in "string":
    if val =="t":
        pass        #continue printing
    elif val == "r":
        continue        #continue printing except r 
    elif val=="n":
        break       #goes out of loop if condition meets 
    print(val)    

print("The end")



# @Functions in python 

def addNumber(a, b):      #define function
  sum = a + b
  print(sum)

addNumber(4, 5)       #call the function 
 
 # Recursive function to find the factorial of a number
def calc_factorial(x):

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))  

num = 6
print("The factorial of", num, "is", calc_factorial(num)) 

 # Output: The factorial of 6 is 720



 