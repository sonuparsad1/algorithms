# Python Data Structures

## Overview

Python has 4 built-in data structures for storing collections:

### 1. List `[]`
- **Ordered**, **mutable**, allows **duplicates**
- Use when: You need an ordered collection that can change

### 2. Tuple `()`
- **Ordered**, **immutable**, allows **duplicates**
- Use when: You need an ordered collection that won't change

### 3. Set `{}`
- **Unordered**, **mutable**, **no duplicates**
- Use when: You need unique items and don't care about order

### 4. Dictionary `{key: value}`
- **Ordered** (Python 3.7+), **mutable**, keys must be **unique**
- Use when: You need key-value pairs for fast lookups

## Comparison Table

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{'a': 1}` |
| Ordered | ✓ | ✓ | ✗ | ✓ (3.7+) |
| Mutable | ✓ | ✗ | ✓ | ✓ |
| Duplicates | ✓ | ✓ | ✗ | Keys: ✗ |
| Indexing | ✓ | ✓ | ✗ | By key |
