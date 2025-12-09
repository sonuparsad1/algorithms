"""
Title: Contextlib and Safe Resource Cleanup
Topic: Error Handling

Theory:
    `contextlib` provides utilities for common context manager tasks.
    - `@contextmanager`: Generator to context manager.
    - `closing()`: Auto-close objects not supporting context proto.
    - `suppress()`: Ignore specific exceptions.
"""

from contextlib import contextmanager, suppress

@contextmanager
def temporary_file(name):
    print(f"Creating temp file {name}...")
    try:
        yield name
    finally:
        print(f"Deleting temp file {name}...")

def run_tests():
    # 1. Generator CM
    with temporary_file("test.txt") as f:
        print(f"Working with {f}")
    
    # 2. Suppress
    with suppress(FileNotFoundError):
        open("non_existent_file.txt")
    print("Continued execution after suppress")
    
    print("[PASS] Contextlib tools")

if __name__ == "__main__":
    run_tests()
