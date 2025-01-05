<div align="center">
  <img src="https://github.com/Vibhav1207/Python-Course/blob/main/assets/variables.png?raw=true">
</div>

---
# 🐍 Python Variables

Welcome to the Python Variables section! In this section, you'll learn about the different types of variables you can use in Python. Variables are used to store data, and Python supports several types of variables.

## 📚 Table of Contents

- [Introduction](#-introduction)
- [String Variables](#-string-variables)
- [Float Variables](#-float-variables)
- [Integer Variables](#integer-variables)
- [Boolean Variables](#boolean-variables)
- [Summary](#summary)

## 📚 Introduction

Variables are containers for storing data values. In Python, you don't need to declare the type of a variable, as Python is dynamically typed. This means you can assign different types of values to the same variable.

## 📜 String Variables

- In this section, you'll learn about string variables in Python, including how to create them, perform operations like concatenation, slicing, and more.

### What is a String Variable?

- A string variable is used to store text data. In Python, you can create a string variable by enclosing text in single quotes (`'`) or double quotes (`"`). Strings are immutable, meaning that once a string is created, it cannot be changed.

### Creating String Variables

- You can create a string variable by assigning a string to a variable name.

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

- (`upper()`): Converts all characters in the string to uppercase.
- (`lower()`): Converts all characters in the string to lowercase.
- (`replace(old, new)`): Replaces occurrences of a substring with another substring.
- (`split(separator)`): Splits the string into a list of substrings based on the specified separator.

```python 
# Example of string methods
greeting = "Hello, World!"
print(greeting.upper())         # Output: HELLO, WORLD!
print(greeting.lower())         # Output: hello, world!
print(greeting.replace("World", "Python"))  # Output: Hello, Python!
print(greeting.split(", "))     # Output: ['Hello', 'World!']
```

# 🔬 Float Variables

- A float variable is used to store numbers with a decimal point. Floats are useful when you need precision for calculations involving fractions or when you need to represent real numbers.

### Creating Float Variables

- You can create a float variable by assigning a number with a decimal point to a variable name.

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

- (`abs()`): Returns the absolute value of a float.
- (`math.ceil()`): Rounds a float up to the nearest integer.
- (`math.floor()`): Rounds a float down to the nearest integer.

```python
import math # in-built module

# Common float methods
negative_value = -7.5
absolute_value = abs(negative_value)
ceiling_value = math.ceil(pi)
floor_value = math.floor(pi)

print(absolute_value)   # Output: 7.5
print(ceiling_value)    # Output: 4
print(floor_value)      # Output: 3
```