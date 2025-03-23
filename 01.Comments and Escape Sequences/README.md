<div align="center">
  <img src="https://github.com/Vibhav1207/Python-Course/blob/main/assets/comments-escape.png?raw=true">
</div>

---

## 📚 Table of Contents

- [Comments](#-comments)
- [Escape Sequences](#-escape-sequences)
- [Print Statement](#-print-statement)

# 💭 Comments

A comment is a part of the coding file that the programmer does not want to execute. It is used to:
- Explain a block of code
- Avoid execution of specific code while testing

## Single-Line Comments
To write a comment just add a '#' at the start of the line.

```python
# This is a 'Single-Line Comment'
print("This is a print statement.")

print("Hello World !!!") # Printing Hello World

print("Python Program")
# print("Python Program") # This line won't execute
```

## Multi-Line Comments
You can use '#' at each line or use multiline strings (""")

```python
# It will execute a block of code if a specified condition is true.
# If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

# Using multiline strings
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
```

# 🔄 Escape Sequences

Escape sequences are special characters that can't be directly used in a string. They start with a backslash (\) followed by the character you want to insert.

```python
# This will cause an error:
# print("This doesnt "execute")

# This will work:
print("This will \" execute")
```

# 🖨️ Print Statement

The print statement in Python has several parameters that control its output:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

## Parameters

- **object(s)**: Any object(s) to print (will be converted to string)
- **sep='separator'**: Separator between objects (default is space)
- **end='end'**: What to print at the end (default is '\n')
- **file**: Object with write method (default is sys.stdout)
- **flush**: Whether to forcibly flush the stream