# Iterator and Generator Examples

## Example 1: File Chunker
```python
def read_in_chunks(filename, chunk_size=1024):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_in_chunks("large_file.bin"):
    process(chunk)
```

## Example 2: Batch Iterator
```python
def batch(iterable, batch_size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

data = range(10)
for b in batch(data, 3):
    print(b)  # [0, 1, 2], [3, 4, 5], [6, 7, 8], [9]
```

## Example 3: Prime Number Generator
```python
def primes():
    yield 2
    primes_list = [2]
    candidate = 3
    while True:
        is_prime = True
        for p in primes_list:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(candidate)
            yield candidate
        candidate += 2

# Get first 10 primes
prime_gen = primes()
first_10 = [next(prime_gen) for _ in range(10)]
```

## Example 4: Tree Traversal
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

tree = Node(2, Node(1), Node(3))
print(list(tree))  # [1, 2, 3]
```
