# Tuples, Sets, and Dictionaries

## Tuples - Immutable Sequences
```python
# Creating tuples
coords = (10, 20)
single = (1,)  # Note the comma for single-element tuple

# Tuple unpacking
x, y = coords

# Tuples are immutable
# coords[0] = 15  # TypeError
```

## Sets - Unique Elements
```python
# Creating sets
numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4} (duplicates removed)
empty_set = set()  # Note: {} creates a dict, not a set

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2         # {1, 2, 3, 4, 5}
intersection = set1 & set2  # {3}
difference = set1 - set2    # {1, 2}

# Set methods
set1.add(4)
set1.remove(2)  # Raises KeyError if not found
set1.discard(2) # No error if not found
```

## Dictionaries - Key-Value Pairs
```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])        # "Alice"
print(person.get("age"))     # 30
print(person.get("job", "Unknown"))  # "Unknown" (default)

# Adding/Updating
person["job"] = "Engineer"
person.update({"age": 31, "country": "USA"})

# Removing
del person["city"]
age = person.pop("age")

# Iterating
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Methods
```python
d = {"a": 1, "b": 2}

keys = d.keys()      # dict_keys(['a', 'b'])
values = d.values()  # dict_values([1, 2])
items = d.items()    # dict_items([('a', 1), ('b', 2)])
```
