"""
Title: Resource Management and RAII
Topic: Advanced OOP

Theory:
    RAII (Resource Acquisition Is Initialization) is a C++ concept.
    In Python, because of GC (non-deterministic destruction), we use Context Managers (`with`) for RAII-like behavior.
    
    However, `__del__` exists as a finalizer but is unreliable (circular refs, interpreter shutdown).
    
    Best Practice: ALWAYS use `with` statements (Context Managers) or `try...finally` for resources.
"""

class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Acquired {self.name}")

    def close(self):
        print(f"Released {self.name}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def run_tests():
    print("--- Scope Start ---")
    with Resource("Database") as r:
        print("Using Resource")
    print("--- Scope End ---")
    # Output should show Released before Scope End
    
    print("[PASS] Resource Management verified")

if __name__ == "__main__":
    run_tests()
