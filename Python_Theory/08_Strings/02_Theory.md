# String Indexing and Slicing

## Indexing
```python
text = "Python"
print(text[0])   # 'P' (first character)
print(text[-1])  # 'n' (last character)
print(text[-2])  # 'o' (second from end)
```

## Slicing
Syntax: `string[start:end:step]`

```python
text = "Python Programming"

print(text[0:6])    # "Python" (index 0 to 5)
print(text[:6])     # "Python" (start defaults to 0)
print(text[7:])     # "Programming" (end defaults to length)
print(text[::2])    # "Pto rgamn" (every 2nd character)
print(text[::-1])   # "gnimmargorP nohtyP" (reverse)
```

## String Concatenation and Repetition
```python
s1 = "Hello"
s2 = "World"

# Concatenation
result = s1 + " " + s2  # "Hello World"

# Repetition
repeat = "Ha" * 3  # "HaHaHa"
```
