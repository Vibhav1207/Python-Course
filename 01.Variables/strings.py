# Creating string variables
name = "Vibhav Patel"
greeting = 'Hello, World!'
print(name)         # Output: Vibhav Patel
print(greeting)     # Output: Hello, World!

# String concatenation
first_name = "Vibahv"
last_name = "Patel"
full_name = first_name + " " + last_name
print(full_name)    # Output: Vibhav Patel

# String slicing
full_name = "Vibhav Patel"
first_name = full_name[0:4]
last_name = full_name[5:8]
print(first_name)   # Output: Vibahv
print(last_name)    # Output: Patel

# String methods
greeting = "Hello, World!"
print(greeting.upper())         # Output: HELLO, WORLD!
print(greeting.lower())         # Output: hello, world!
print(greeting.replace("World", "Python"))  # Output: Hello, Python!
print(greeting.split(", "))     # Output: ['Hello', 'World!']