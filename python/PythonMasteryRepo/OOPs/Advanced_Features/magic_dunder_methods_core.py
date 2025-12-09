"""
Title: Core Magic Methods (Dunders)
Topic: Advanced OOP

Theory:
    "Dunder" stands for Double Underscore. These methods define how objects behave with operators and built-ins.
    
    KEY METHODS:
    - Initialization: `__init__`, `__new__`, `__del__`
    - Representation: `__str__` (user), `__repr__` (debugging)
    - Comparison: `__eq__`, `__lt__`, `__le__`, etc.
    - Hashing: `__hash__` (required for sets/dict keys)
    - Boolean: `__bool__`

Pitfalls:
    - Implementing `__eq__` without `__hash__` makes objects unhashable.
    - `__del__` is tricky; don't rely on it for critical cleanup (use Context Managers).
"""

class Person:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    # 1. Representation
    def __repr__(self):
        return f"Person(name='{self.name}', id_num={self.id_num})"

    def __str__(self):
        return f"{self.name} (#{self.id_num})"

    # 2. Equality
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.id_num == other.id_num

    # 3. Hashing (Must be immutable based on Eq)
    def __hash__(self):
        return hash(self.id_num)

    # 4. Ordering (Privacy of sorting)
    def __lt__(self, other):
        return self.id_num < other.id_num
    
    # 5. Truthiness
    def __bool__(self):
        return self.id_num > 0 # False if ID is 0

def run_tests():
    p1 = Person("Alice", 1)
    p2 = Person("Alice", 1)
    p3 = Person("Bob", 2)

    # __eq__
    assert p1 == p2
    assert p1 != p3

    # __lt__
    assert p1 < p3

    # __hash__ (allows set usage)
    s = {p1, p2, p3}
    assert len(s) == 2 # p1 and p2 de-duplicated

    # __str__ and __repr__
    print(f"Str: {str(p1)}")   # Alice (#1)
    print(f"Repr: {repr(p1)}") # Person(name='Alice', id_num=1)

    print("[PASS] Core Magic/Dunder methods verified")

if __name__ == "__main__":
    run_tests()
