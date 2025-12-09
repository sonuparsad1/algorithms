# Data Types Overview

## Definition
Variables can store data of different types, and different types can do different things.
Python has the following standard built-in data types:

## Taxonomy of Data Types
It is crucial to understand which types are **Mutable** (changeable) and **Immutable** (unchangeable).

### 1. Immutable Types
Once created, their value cannot be changed. If you "modify" them, Python actually creates a new object.
- **Numeric**: `int`, `float`, `complex`
- **Text**: `str`
- **Boolean**: `bool`
- **Sequence**: `tuple` (contains immutable or mutable items, but the tuple structure itself is immutable)
- **Special**: `NoneType`

### 2. Mutable Types
You can change the content without changing the identity (memory address) of the object.
- **Sequence**: `list`
- **Mapping**: `dict`
- **Set Types**: `set`
- **Binary**: `bytearray`

## Getting the Type
Use the `type()` function to check the type of any object.

```python
x = 5
print(type(x))  # <class 'int'>

y = "Hello"
print(type(y))  # <class 'str'>
```

## Summary Table

| Category | Type Name | Example | Mutable? |
| :--- | :--- | :--- | :--- |
| Text | `str` | `"Hello"` | No |
| Numeric | `int` | `20` | No |
| Numeric | `float` | `20.5` | No |
| Numeric | `complex` | `1j` | No |
| Sequence | `list` | `["apple", "banana"]` | **Yes** |
| Sequence | `tuple` | `("apple", "banana")` | No |
| Sequence | `range` | `range(6)` | No |
| Mapping | `dict` | `{"name": "John", "age": 36}` | **Yes** |
| Set | `set` | `{"apple", "banana"}` | **Yes** |
| Set | `frozenset` | `frozenset({"apple", "banana"})` | No |
| Boolean | `bool` | `True` | No |
| Binary | `bytes` | `b"Hello"` | No |
| None | `NoneType` | `None` | No |
