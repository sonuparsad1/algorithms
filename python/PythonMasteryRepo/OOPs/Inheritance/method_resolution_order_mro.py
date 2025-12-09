"""
Title: Method Resolution Order (MRO)
Topic: Inheritance

Theory:
    Python uses the C3 Linearization Algorithm (since 2.3) to determine the MRO.
    It ensures:
    - Children are visited before parents.
    - Parent order is preserved (Left to Right).
    - Monotonicity (subclassing doesn't change valid orderings).

    You can view it via `ClassName.__mro__` or `ClassName.mro()`.
"""

class A:
    def process(self):
        return "A"

class B(A):
    def process(self):
        return "B"

class C(A):
    def process(self):
        return "C"

# Diamond Inheritance
class D(B, C):
    """
      A
     / \\
    B   C
     \\ /
      D
    
    MRO should be: D -> B -> C -> A -> object
    """
    pass

def run_analysis():
    print("--- MRO Analysis ---")
    
    mro = [x.__name__ for x in D.mro()]
    print(f"D MRO: {mro}")
    
    assert mro == ['D', 'B', 'C', 'A', 'object']
    
    d = D()
    # It calls B's process because B is first after D
    assert d.process() == "B" 
    
    print("[PASS] MRO logic verified")

if __name__ == "__main__":
    run_analysis()
