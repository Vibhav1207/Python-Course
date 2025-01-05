# Creating boolean variables
is_student = True
has_passed = False
print(is_student)   # Output: True
print(has_passed)   # Output: False

# Logical operations with booleans
a = True
b = False

and_operation = a and b
or_operation = a or b
not_operation = not a

print(and_operation)    # Output: False
print(or_operation)     # Output: True
print(not_operation)    # Output: False

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

# Boolean methods
value = 5
boolean_value = bool(value)
is_integer = isinstance(value, int)

print(boolean_value)    # Output: True
print(is_integer)       # Output: True