# Comprehension Syntax

## List Comprehension Syntax
```python
[expression for item in iterable if condition]

# Multiple for clauses
[expression for item1 in iter1 for item2 in iter2]

# Nested comprehension
[[expression for item in iterable] for outer_item in outer_iterable]
```

## Dictionary Comprehension Syntax
```python
{key_expr: value_expr for item in iterable if condition}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
```

## Set Comprehension Syntax
```python
{expression for item in iterable if condition}
```

## Generator Expression Syntax
```python
(expression for item in iterable if condition)

# Note: Use () not []
```

## Comparison
```python
# List - Creates list immediately
list_comp = [x**2 for x in range(10)]

# Generator - Lazy evaluation
gen_exp = (x**2 for x in range(10))

# Set - Unique elements
set_comp = {x**2 for x in range(10)}

# Dict - Key-value pairs
dict_comp = {x: x**2 for x in range(10)}
```
