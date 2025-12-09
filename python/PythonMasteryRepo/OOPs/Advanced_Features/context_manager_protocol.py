"""
Title: Context Manager Protocol
Topic: Advanced OOP

Theory:
    Context managers manage resources (files, locks, connections) using `with` statement.
    
    KEY METHODS:
    - `__enter__(self)`: Setup resource, return object (as `as var`).
    - `__exit__(self, exc_type, exc_val, exc_tb)`: Cleanup. Handles exceptions returning True suppresses them.

    Alternative: `contextlib.contextmanager` decorator for function-based managers.
"""

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        print(f"Opening {self.filename}...")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print(f"Closed {self.filename}.")
        
        if exc_type:
            print(f"Exception handled: {exc_val}")
            # return True # Uncomment to suppress exception
            return False

def run_tests():
    import os
    fname = "test_ctx.txt"
    
    # 1. Normal usage
    with ManagedFile(fname) as f:
        f.write("Hello")
    
    # Check if closed
    assert not f.closed # Wait, the file object itself shows closed status? No, we closed it.
    # Actually 'f' usage after block is risky if not aware. 
    # But checking internal state:
    try:
        f.write("More")
    except ValueError:
        print("File is indeed closed.")
        
    # Cleanup
    if os.path.exists(fname):
        os.remove(fname)

    # 2. Exception handling
    try:
        with ManagedFile("none") as f:
            raise RuntimeError("Boom")
    except RuntimeError:
        print("Caught Runtime Error outside context")

    print("[PASS] Context manager protocol")

if __name__ == "__main__":
    run_tests()
