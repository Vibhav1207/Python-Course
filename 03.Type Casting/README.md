<div align="center">
  <img src="https://github.com/Vibhav1207/Python-Course/blob/main/assets/typecasting.png?raw=true">
</div>

---
## 📚 Table of Contents

- [Type Casting](#-type-casting)
- [Explicit Type Casting](#-explicit-type-casting)
- [Implicit Type Casting](#-implicit-type-casting)

## 🔄 Type Casting

Type Casting is the conversion of one data type into another data type. Python provides various built-in functions for type conversion, such as `int()`, `float()`, `str()`, `ord()`, `hex()`, `oct()`, `tuple()`, `set()`, `list()`, and `dict()`.

There are two types of Type Casting in Python:
1. Explicit Type Casting (Manual Conversion)
2. Implicit Type Casting (Automatic Conversion)

## 🎯 Explicit Type Casting

Explicit Type Casting, also known as Type Conversion, is performed manually by the programmer using Python's built-in functions. This is done when you want to specifically convert one data type to another.

### Common Type Conversion Functions

```python
# Converting string to integer
string_num = "15"
number = int(string_num)    # number = 15

# Converting integer to float
int_num = 7
float_num = float(int_num)  # float_num = 7.0

# Converting number to string
num = 123
string = str(num)           # string = "123"
```

### Example of Explicit Type Casting

```python
# Adding string number with integer
string = "15"
number = 7
string_number = int(string)  # Converting string to integer
sum = number + string_number
print("The Sum of both the numbers is:", sum)  # Output: The Sum of both the numbers is 22
```

## 🔄 Implicit Type Casting

Implicit Type Casting is automatically performed by Python interpreter when:
1. We perform operations between different data types
2. Python needs to convert a smaller data type to a higher data type to prevent data loss

### Data Type Hierarchy
Python follows a hierarchy in data types where some types are "higher" than others:
- Boolean → Integer → Float → Complex

### Example of Implicit Type Casting

```python
# Integer and Float addition
a = 7        # Integer
print(type(a))    # Output: <class 'int'>

b = 3.0      # Float
print(type(b))    # Output: <class 'float'>

# Python automatically converts result to float
c = a + b    # Integer + Float = Float
print(c)          # Output: 10.0
print(type(c))    # Output: <class 'float'>
```

### Common Implicit Type Casting Scenarios

```python
# Integer and Float
result1 = 5 + 3.14    # Result is float (8.14)

# Integer and Complex
result2 = 10 + 2j     # Result is complex (10+2j)

# Boolean and Integer
result3 = True + 1    # Result is integer (2)
```

## 🔄 Collection Type Casting

Python allows type casting between different collection types (list, tuple, set, dict). Here are some common scenarios:

```python
# Converting between lists and tuples
my_list = [1, 2, 3]
my_tuple = tuple(my_list)    # (1, 2, 3)
back_to_list = list(my_tuple) # [1, 2, 3]

# Converting to set (removes duplicates)
duplicates_list = [1, 2, 2, 3, 3, 4]
unique_set = set(duplicates_list)  # {1, 2, 3, 4}

# Converting dictionary keys/values to list
my_dict = {"a": 1, "b": 2}
keys_list = list(my_dict.keys())    # ["a", "b"]
values_list = list(my_dict.values()) # [1, 2]
```

## 🌟 Real-World Applications

### 1. Data Processing
```python
# Converting CSV data to appropriate types
user_id = "1001"  # From CSV as string
age = "25"        # From CSV as string

# Converting to proper types for processing
processed_id = int(user_id)
processed_age = int(age)
```

### 2. API Response Handling
```python
# Converting JSON response data
api_response = {"temperature": "24.5", "is_sunny": "true"}

# Converting to appropriate types
temp = float(api_response["temperature"])
is_sunny = api_response["is_sunny"].lower() == "true"
```

## ⚡ Performance Considerations

1. **Memory Usage**:
   - Converting large collections can consume significant memory
   - Consider using generators for large datasets

2. **Processing Time**:
   - Implicit casting is generally faster than explicit casting
   - Avoid unnecessary type conversions in loops

```python
# Less efficient (type conversion in loop)
for i in range(1000):
    str_num = str(i)    # Unnecessary conversion
    process(str_num)

# More efficient (convert once)
str_nums = [str(i) for i in range(1000)]
for num in str_nums:
    process(num)
```

## 🚨 Important Notes

1. Not all type conversions can be done implicitly. Python will raise a TypeError if the conversion is not possible.
2. Explicit type casting gives you more control but can raise errors if the conversion is not valid.
3. When working with numeric types, Python automatically converts to the type that can best preserve the information.
4. String to number conversion must always be done explicitly using `int()` or `float()`.
5. Always validate data before type casting to handle potential errors gracefully.
6. Consider using specialized libraries (like `numpy`) for efficient numerical type conversions.
7. Be cautious when converting floating-point numbers to integers as it may lead to data loss.