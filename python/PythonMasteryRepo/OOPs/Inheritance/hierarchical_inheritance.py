"""
Title: Hierarchical Inheritance
Topic: Inheritance

Theory:
    Multiple classes inherit from a single Base class.
    One Parent -> Many Children.
"""

class Shape:
    def describe(self):
        return "I am a shape"

class Circle(Shape):
    def roll(self):
        return "Rolling"

class Square(Shape):
    def stack(self):
        return "Stacking"

def run_test():
    c = Circle()
    s = Square()
    
    # Both share Parent method
    assert c.describe() == "I am a shape"
    assert s.describe() == "I am a shape"
    
    # But disjoint sibling methods
    assert hasattr(c, 'roll')
    assert not hasattr(s, 'roll')
    
    print("[PASS] Hierarchical inheritance")

if __name__ == "__main__":
    run_test()
