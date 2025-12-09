"""
Title: Protocols (Structural Subtyping)
Topic: Polymorphism

Theory:
    Introduced in Python 3.8 (`typing.Protocol`).
    Allows "Static Duck Typing".
    
    If a class implements the methods defined in the Protocol, it is considered a subtype of that Protocol,
    even if it doesn't explicitly inherit from it.
"""

from typing import Protocol, List

# ==========================================
# 1. Define Protocol
# ==========================================

class Drawable(Protocol):
    def draw(self) -> str:
        """Any class with this method satisfies Drawable."""
        ...

# ==========================================
# 2. Implementations (No inheritance needed!)
# ==========================================

class Circle:
    def draw(self) -> str:
        return "Drawing Circle"

class Square:
    def draw(self) -> str:
        return "Drawing Square"

class User:
    def save(self):
        return "Saving"
    # Does NOT implement draw

# ==========================================
# 3. Usage
# ==========================================

def render(shapes: List[Drawable]):
    output = []
    for s in shapes:
        output.append(s.draw())
    return output

# ==========================================
# Tests
# ==========================================

def run_tests():
    c = Circle()
    s = Square()
    u = User()

    # Valid Usage
    results = render([c, s])
    assert results == ["Drawing Circle", "Drawing Square"]
    
    # Static Analysis would catch 'u' passed to render, 
    # but runtime python just crashes if we try to call .draw() on u
    try:
        render([u]) # type: ignore
    except AttributeError:
        print("Caught expected error for non-conforming type")

    print("[PASS] Protocols (Structural Subtyping)")

if __name__ == "__main__":
    run_tests()
