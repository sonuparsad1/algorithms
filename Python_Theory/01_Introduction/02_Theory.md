# Python: Theoretical Foundations

## 1. The Interpreter Model

### How Python Executes Code
1. **Source Code** (`.py` file) → Written by programmer.
2. **Bytecode** (`.pyc` file) → Compiled by Python to an intermediate representation.
3. **Python Virtual Machine (PVM)** → Executes bytecode.

```
Source Code (.py) → Bytecode (.pyc) → PVM → Output
```

### Compilation vs Interpretation
- **Compiled Languages** (C, C++): Source → Machine Code → Execution.
  - Faster execution, platform-specific binaries.
- **Interpreted Languages** (Python, JavaScript): Source → Interpreter → Execution.
  - Slower execution, but portable and flexible.

Python is technically **both**: It compiles to bytecode, then interprets it.

## 2. Memory Management

### Automatic Memory Management
- **Garbage Collection**: Python automatically frees memory when objects are no longer referenced.
- **Reference Counting**: Tracks how many references point to an object.

### Everything is an Object
In Python, **everything** is an object:
- Numbers: `5` is an object of class `int`.
- Functions: Functions are objects that can be passed around.
- Classes: Even classes themselves are objects (of type `type`).

## 3. Name Binding (Variables as References)

Python variables are **names** that refer to objects, not containers holding values.

```python
a = [1, 2, 3]
b = a  # b refers to the SAME list object as a
b.append(4)
print(a)  # [1, 2, 3, 4] - a is also modified!
```

## 4. The Global Interpreter Lock (GIL)

- **GIL**: A mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode at once.
- **Impact**: Limits true parallelism in CPU-bound multi-threaded programs.
- **Workaround**: Use `multiprocessing` (separate processes) instead of `threading` for CPU-intensive tasks.

## 5. Duck Typing

> "If it walks like a duck and quacks like a duck, it's a duck."

Python doesn't check types explicitly. It checks if an object has the required methods/attributes.

```python
def make_sound(animal):
    animal.quack()  # Doesn't care what type 'animal' is

class Duck:
    def quack(self): print("Quack!")

class Person:
    def quack(self): print("I'm imitating a duck!")

make_sound(Duck())    # Works
make_sound(Person())  # Also works!
```
