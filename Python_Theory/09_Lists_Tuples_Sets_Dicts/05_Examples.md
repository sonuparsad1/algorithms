# Data Structure Examples

## Example 1: Shopping Cart (List)
```python
cart = []
cart.append({"item": "Apple", "price": 1.50, "qty": 3})
cart.append({"item": "Banana", "price": 0.75, "qty": 6})

total = sum(item["price"] * item["qty"] for item in cart)
print(f"Total: ${total:.2f}")
```

## Example 2: Phone Book (Dictionary)
```python
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}

# Add contact
phonebook["Charlie"] = "555-9012"

# Lookup
print(phonebook.get("Alice", "Not found"))
```

## Example 3: Remove Duplicates (Set)
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5]
```

## Example 4: Word Frequency (Dictionary)
```python
text = "the quick brown fox jumps over the lazy dog"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)  # {'the': 2, 'quick': 1, ...}
```

## Example 5: Matrix Operations (Nested Lists)
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose
transposed = [[row[i] for row in matrix] for i in range(3)]
```
