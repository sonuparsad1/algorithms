# Strings in Python

## Definition
A **string** is a sequence of characters enclosed in quotes. Strings are **immutable** - once created, they cannot be changed.

## Creating Strings
```python
# Single quotes
s1 = 'Hello'

# Double quotes
s2 = "World"

# Triple quotes (multiline)
s3 = """This is
a multiline
string"""

# Raw strings (ignore escape sequences)
s4 = r"C:\new\path"
```

## String Immutability
```python
text = "Hello"
# text[0] = 'h'  # TypeError: 'str' object does not support item assignment

# Must create new string
text = 'h' + text[1:]  # "hello"
```

## String as Sequence
Strings are sequences, supporting indexing and slicing like lists.
