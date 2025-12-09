# Python Mastery Repository

A comprehensive study repository for Python Object-Oriented Programming (OOP) and Algorithms. This repository is designed to be a complete resource for interview preparation and mastering Python internals.

## Structure

### 1. OOPs (`/OOPs`)
From the very basics of Classes and Objects to advanced topics like Metaclasses, Descriptors, and Design Patterns.
- **Basics**: Core concepts, `__init__`, class vs instance variables.
- **Encapsulation & Inheritance**: Access modifiers, MRO, `super()`.
- **Polymorphism & Abstraction**: Duck typing, ABCs, Protocols.
- **Advanced Features**: Magic methods (`dunders`), slots, decorators, context managers.
- **Design Patterns**: Singleton, Factory, Observer, etc.
- **Concurrency**: Threading, Multiprocessing in classes.
- **Testing**: Unit testing strategies for OOP.

### 2. Algorithms (`/Algorithms`)
A structured journey from Sorting/Searching to Advanced Graph Algorithms and Dynamic Programming.
- **Basics**: Sorting, Searching, Recursion.
- **Data Structures**: Linked Lists, Trees, Heaps, Hash Tables (with collision handling).
- **Graphs**: BFS/DFS, Dijkstra, Bellman-Ford, MST, Strongly Connected Components.
- **Dynamic Programming**: Classic problems, optimizations, digit DP.
- **Hard Topics**: Segment Trees, Fenwick Trees, Flow algorithms (if added), Geometry.

## How to use
Each `.py` file is self-contained and structured as follows:
1. **Theory Header**: Explanation of the concept, time/space complexity, and "gotchas".
2. **Implementation**: Clean, readable code with type hints.
3. **Tests/Usage**: A `if __name__ == "__main__":` block with assert statements or doctests demonstrating the usage.

Run any file directly:
```bash
python OOPs/Basics/classes_objects.py
python Algorithms/Basics/sorting_quick.py
```

## Suggested Study Path
1. **Python Syntax Refresh**: Ensure you know basic Python syntax.
2. **OOPs Basics -> Polymorphism**: Build your foundation in designing software.
3. **Algorithms Basics -> Intermediate DS**: Master the tools.
4. **OOPs Advanced**: Learn Python's "Magic" to write pythonic code.
5. **Algorithms Advanced**: Graphs, DP, and Bit manipulation for competitive programming/hard interviews.

## License
MIT License.
