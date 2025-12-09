# Comprehension Examples

## Example 1: FizzBuzz
```python
result = ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x 
          for x in range(1, 101)]
```

## Example 2: Word Lengths
```python
sentence = "The quick brown fox jumps"
word_lengths = {word: len(word) for word in sentence.split()}
# {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumps': 5}
```

## Example 3: Flatten Nested List
```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
# [1, 2, 3, 4, 5, 6]
```

## Example 4: Prime Numbers
```python
primes = [x for x in range(2, 100) 
          if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
```

## Example 5: File Processing
```python
# Read and process lines
with open('data.txt') as f:
    lines = [line.strip().upper() for line in f if line.strip()]
```

## Example 6: Matrix Operations
```python
# Create identity matrix
n = 3
identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

## Example 7: Group By
```python
from itertools import groupby

data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
grouped = {k: [v for _, v in g] for k, g in groupby(data, key=lambda x: x[0])}
# {'a': [1, 2], 'b': [3, 4]}
```
