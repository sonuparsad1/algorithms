# Common Data Structure Errors

## 1. List Index Out of Range
```python
lst = [1, 2, 3]
# print(lst[5])  # IndexError

# CORRECT
if len(lst) > 5:
    print(lst[5])
```

## 2. KeyError in Dictionary
```python
d = {"a": 1}
# print(d["b"])  # KeyError

# CORRECT
print(d.get("b", "Not found"))
```

## 3. Modifying List While Iterating
```python
# WRONG
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Skips elements!

# CORRECT
numbers = [num for num in numbers if num % 2 != 0]
```

## 4. Mutable Default Arguments
```python
# WRONG
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# CORRECT
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## 5. Shallow vs Deep Copy
```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999  # Modifies original too!

# CORRECT - Use deep copy
import copy
deep = copy.deepcopy(original)
```
