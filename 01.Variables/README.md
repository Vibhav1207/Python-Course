<div align="center">
  <img src="https://github.com/Vibhav1207/Python-Course/blob/main/assets/variables-datatype.png?raw=true">
</div>

---
## 📚 Table of Contents

- [Variables](#-variables)
- [Datatype](#-data-type)
- [String Dataype](#-string-datatype)
- [Float Dataype](#-float-datatype)
- [Integer Dataype](#-integer-datatype)
- [Boolean Dataype](#-boolean-datatype)
## 📚 Variables

Variables are containers for storing data values. In Python, you don't need to declare the type of a variable, as Python is dynamically typed. This means you can assign different types of values to the same variable.

```python 
a = 1
b = True
c = "Vibhav"
d = None
```
- These are four variables of different data types.
--- 
## 📊 Data Type
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:
```python
a = 1
print(type(a))
b = "1"
print(type(b))
```

## 📜 String Datatype

- A string  is used to store text data. In Python, you can create a string variable by enclosing text in single quotes (`'`) or double quotes (`"`). Strings are immutable, meaning that once a string is created, it cannot be changed.

### Creating String Datatype

- You can create a string  by assigning a string to a variable name.

```python
# Example of creating string variables
name = "Vibhav Patel"
greeting = 'Hello, World!'
print(name)         # Output: Vibhav Patel
print(greeting)     # Output: Hello, World!
```

### String Concatenation 

- String concatenation is the process of joining two or more strings together. You can use the (`+`) operator to concatenate strings.

```python 
# Example of string concatenation
first_name = "Vibhav"
last_name = "Patel"
full_name = first_name + " " + last_name
print(full_name)    # Output: Vibhav Patel
```

### String Slicing

- String slicing allows you to extract a part of a string by specifying a range of indices. The syntax for slicing is (`string[start:end]`).

```python 
# Example of string slicing
full_name = "Vibhav Patel"
first_name = full_name[0:4]
last_name = full_name[5:8]
print(first_name)   # Output: Vibhav
print(last_name)    # Output: Patel
```
### String Methods

Python provides several built-in methods that you can use to manipulate strings. Here are some common string methods:

- `upper()`: Converts all characters in the string to uppercase.
- `lower()`: Converts all characters in the string to lowercase.
- `replace(old, new)`: Replaces occurrences of a substring with another substring.
- `split(separator)`: Splits the string into a list of substrings based on the specified separator.

```python 
# Example of string methods
greeting = "Hello, World!"
print(greeting.upper())         # Output: HELLO, WORLD!
print(greeting.lower())         # Output: hello, world!
print(greeting.replace("World", "Python"))  # Output: Hello, Python!
print(greeting.split(", "))     # Output: ['Hello', 'World!']
```

# 🔬 Float Datatype

- A float  is used to store numbers with a decimal point. Floats are useful when you need precision for calculations involving fractions or when you need to represent real numbers.

### Creating Float Datatype

- You can create a float  by assigning a number with a decimal point to a variable name.

```python
# Example of creating float variables
pi = 3.14159
temperature = 98.6
print(pi)           # Output: 3.14159
print(temperature)  # Output: 98.6
```

### Arithmetic Operations with Floats

- You can perform various arithmetic operations on floats, such as addition, subtraction, multiplication, division, and more.

```python
# Arithmetic operations with floats
a = 5.5
b = 2.0

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
exponentiation = a ** b

print(addition)         # Output: 7.5
print(subtraction)      # Output: 3.5
print(multiplication)   # Output: 11.0
print(division)         # Output: 2.75
print(exponentiation)   # Output: 30.25
```

### Rounding Floats

- You can round float values to a specified number of decimal places using the (`round()`) function.

```python 
# Rounding floats
value = 3.14159
rounded_value = round(value, 2)
print(rounded_value)    # Output: 3.14
```

### Common Float Methods

Python provides several built-in functions that you can use with float variables. Here are some common ones:

- `abs()`: Returns the absolute value of a float.
- `math.ceil()`: Rounds a float up to the nearest integer.
- `math.floor()`: Rounds a float down to the nearest integer.

```python
import math #in-built module

# Common float methods
negative_value = -7.5
absolute_value = abs(negative_value)
ceiling_value = math.ceil(pi)
floor_value = math.floor(pi)

print(absolute_value)   # Output: 7.5
print(ceiling_value)    # Output: 4
print(floor_value)      # Output: 3
```

# 🔢 Integer Datatype

An integer  is used to store whole numbers (without a decimal point). Integers can be both positive and negative. They are commonly used for counting and indexing.

### Creating Integer Datatype

- You can create an integer variable by assigning a whole number to a variable name.

```python
# Example of creating integer variables
age = 14
year = 2021
print(age)          # Output: 14
print(year)         # Output: 2021
```
### Arithmetic Operations with Integers

- You can perform various arithmetic operations on integers, such as addition, subtraction, multiplication, division, and more.

```python 
# Arithmetic operations with integers
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print(addition)         # Output: 13
print(subtraction)      # Output: 7
print(multiplication)   # Output: 30
print(division)         # Output: 3.3333333333333335
print(floor_division)   # Output: 3
print(modulus)          # Output: 1
print(exponentiation)   # Output: 1000 
```

### Built-in Functions for Integers

Python provides several built-in functions that you can use with integer variables. Here are some common ones:

- `abs()`: Returns the absolute value of an integer.
- `max()`: Returns the largest of the input values.
- `min()`: Returns the smallest of the input values.

```python 
# Common integer methods
negative_value = -10
absolute_value = abs(negative_value)
max_value = max(1, 2, 3, 4, 5)
min_value = min(1, 2, 3, 4, 5)

print(absolute_value)   # Output: 10
print(max_value)        # Output: 5
print(min_value)        # Output: 1
```

### Converting Strings to Integers

- You can convert a string representation of a number to an integer using the `int()` function.

```python 
# Converting strings to integers
string_number = "123"
integer_number = int(string_number)
print(integer_number)   # Output: 123
```
# ✅ Boolean Datatype

A boolean is used to store one of two values: `True` or `False`. Booleans are often used in conditional statements and loops to control the flow of a program.

### Creating Boolean Datatype

- You can create a boolean  by assigning `True` or `False` to a variable name.

```python
# Example of creating boolean variables
is_student = True
has_passed = False
print(is_student)   # Output: True
print(has_passed)   # Output: False
```

### Logical Operations with Booleans

- You can perform various logical operations with booleans, such as `and`, `or`,`not`.

```python 
# Logical operations with booleans
a = True
b = False

and_operation = a and b
or_operation = a or b
not_operation = not a

print(and_operation)    # Output: False
print(or_operation)     # Output: True
print(not_operation)    # Output: False
```

### Comparison Operators

Comparison operators are used to compare values. They return a boolean value (True or False). Common comparison operators include:

- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

```python 
# Comparison operations
x = 10
y = 20

equal = x == y
not_equal = x != y
greater_than = x > y
less_than = x < y
greater_than_or_equal = x >= y
less_than_or_equal = x <= y

print(equal)                # Output: False
print(not_equal)            # Output: True
print(greater_than)         # Output: False
print(less_than)            # Output: True
print(greater_than_or_equal) # Output: False
print(less_than_or_equal)   # Output: True
```

### Boolean Methods

Python provides several built-in functions that return boolean values. Here are some common ones:

- `bool()`: Converts a value to a boolean.
- `isinstance()`: Checks if an object is an instance of a specific class or type.

```python 
# Boolean methods
value = 5
boolean_value = bool(value)
is_integer = isinstance(value, int)

print(boolean_value)    # Output: True
print(is_integer)       # Output: True
```