# Practice Questions - Comprehensions

## Questions

### Q1: Square Even Numbers
Create a list of squares of even numbers from 0 to 20.

### Q2: Word Lengths Dictionary
Create a dictionary mapping words to their lengths from a sentence.

### Q3: Flatten and Filter
Flatten a nested list and keep only positive numbers.

### Q4: Cartesian Product
Create all pairs (x, y) where x is from [1, 2, 3] and y is from ['a', 'b'].

### Q5: Prime Checker
Use comprehension to find all primes between 2 and 50.

---

## Solutions

### A1: Square Even Numbers
```python
squares = [x**2 for x in range(21) if x % 2 == 0]
print(squares)
# [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

### A2: Word Lengths Dictionary
```python
sentence = "Python is an amazing programming language"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)
# {'Python': 6, 'is': 2, 'an': 2, 'amazing': 7, 'programming': 11, 'language': 8}
```

### A3: Flatten and Filter
```python
nested = [[1, -2, 3], [-4, 5], [6, -7, 8]]
positive = [num for sublist in nested for num in sublist if num > 0]
print(positive)
# [1, 3, 5, 6, 8]
```

### A4: Cartesian Product
```python
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs)
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

### A5: Prime Checker
```python
primes = [x for x in range(2, 51) 
          if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

## Bonus: Advanced Challenges

### Matrix Transpose
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Group by First Letter
```python
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = {word[0]: [w for w in words if w[0] == word[0]] for word in words}
print(grouped)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```
