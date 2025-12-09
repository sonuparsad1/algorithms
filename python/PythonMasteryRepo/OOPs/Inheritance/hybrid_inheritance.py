"""
Title: Hybrid Inheritance
Topic: Inheritance

Theory:
    Hybrid Inheritance is a mix of two or more types (e.g., Single + Multiple).
    Typically results in the "Diamond Problem" structure.
    
    Python handles this purely via MRO. No special keyword.
    
    Complexity:
    High human cognitive load. Avoid deep hybrid graphs if possible.
"""

class Device:
    def __init__(self, name):
        self.name = name

class Phone(Device): # Single
    def call(self):
        return "Calling"

class Camera(Device): # Single
    def snap(self):
        return "Snapping"

class SmartPhone(Phone, Camera): # Multiple (creating Hybrid overall)
    def __init__(self, name):
        # We need to initialize carefully.
        # Since Device is not cooperative (didn't use super presumably, or is simple),
        # we might just direct init if it's the same base.
        # But correctly, we should use super() if base is shared.
        super().__init__(name)

    def feature(self):
        return f"{self.name}: {self.call()} and {self.snap()}"

def run_test():
    s = SmartPhone("iPhone")
    assert s.call() == "Calling"
    assert s.snap() == "Snapping"
    assert s.name == "iPhone"
    
    print("[PASS] Hybrid structure valid")

if __name__ == "__main__":
    run_test()
