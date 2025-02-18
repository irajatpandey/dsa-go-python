my_str = "Hello World"
print(my_str) # Hello World

# Accessing characters in a string
print(my_str[0]) # H
print(my_str[1]) # e
print(my_str[-1]) # d

# String Concatenation
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2) # Hello World

# String Repetition
print(str1 * 3) # HelloHelloHello
print(str2 * 2) # WorldWorld

# Slice a string
print(my_str[0:5]) # Hello
print(my_str[6:]) # World
print(type(my_str[0:3])) # <class 'str'>

# String Length
print(len(my_str)) # 11

# String Membership
print('H' in my_str) # True
print('z' in my_str) # False

# String Iteration 
for s in my_str:
    print(s, end=" ") # H e l l o   W o r l d
print()

# String Comparison
str1 = "Hello"
str2 = "Hello"
str3 = "World"
print(str1 == str2) # True
print(str1 == str3) # False

# String Formatting
name = "Alice"
age = 25
print("Hello, my name is %s and I am %d years old." % (name, age)) # Hello, my name is Alice and I am 25 years old. 

# String Formatting using format method
print("Hello, my name is {} and I am {} years old.".format(name, age)) # Hello, my name is Alice and I am 25 years old.

# String Formatting using f-string
print(f"Hello, my name is {name} and I am {age} years old.") # Hello, my name is Alice and I am 25 years old.

# String Methods
my_str = "hello world"
print(my_str.capitalize()) # Hello world
print(my_str.upper()) # HELLO WORLD
print(my_str.lower()) # hello world
print(my_str.title()) # Hello World
print(my_str.swapcase()) # HELLO WORLD
print(my_str.count('l')) # 3
print(my_str.find('l')) # 2
print(my_str.find('z')) # -1
print(my_str.index('l')) # 2
# print(my_str.index('z')) # ValueError: substring not found
print(my_str.replace('world', 'Alice')) # hello Alice  
print(my_str.startswith('hello')) # True
print(my_str.endswith('world')) # True
print(my_str.split()) # ['hello', 'world']
print(my_str.split('l')) # ['he', '', 'o wor', 'd']
print(my_str.strip()) # hello world
print(my_str.lstrip()) # hello world
print(my_str.rstrip()) # hello world
print(my_str.isalnum()) # False
print(my_str.isalpha()) # False
print(my_str.isdigit()) # False
print(my_str.islower()) # True
print(my_str.isupper()) # False
print(my_str.isspace()) # False

# String Join
my_str = "Hello World"
print(" ".join(my_str)) # H e l l o   W o r l d
print("".join(reversed(my_str))) # dlroW olleH

# String Reverse
print(my_str[::-1]) # dlroW olleH
print("".join(reversed(my_str))) # dlroW olleH

# String Palindrome
str_1 = "madam"
print(str_1 == str_1[::-1]) # True

# String to Integer
num_str = "123"
print(int(num_str)) # 123
print(type(int(num_str))) # <class 'int'>

# Integer to String
num = 123
print(str(num)) # 123
print(type(str(num))) # <class 'str'>


# String to List
my_str = "hello"
print(list(my_str)) # ['h', 'e', 'l', 'l', 'o']

# List to String
l = ['h', 'e', 'l', 'l', 'o']
print("".join(l)) # hello

# String to Set
my_str = "hello"
print(set(my_str)) # {'o', 'e', 'h', 'l'}

# Set to String
s = {'o', 'e', 'h', 'l'}
print("".join(s)) # oehl

# String to Dictionary
my_str = "hello"
print(dict(enumerate(my_str))) # {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

# Dictionary to String
d = {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}
print("".join(d.values())) # hello

# String to Tuple
my_str = "hello"
print(tuple(my_str)) # ('h', 'e', 'l', 'l', 'o')

# Tuple to String
t = ('h', 'e', 'l', 'l', 'o')
print("".join(t)) # hello