"""
Title: Point and Line Basics
Topic: Geometry Algorithms

Theory:
    Point: (x, y).
    Line: ax + by + c = 0.
    Distance: sqrt((x2-x1)^2 + (y2-y1)^2).
    Orientation: (p, q, r). 0=Collinear, 1=Clockwise, 2=CounterClockwise.
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def orientation(p, q, r):
    """
    Returns:
    0: Collinear
    1: Clockwise
    2: Counterclockwise
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0: return 0
    return 1 if val > 0 else 2

def run_tests():
    p1 = Point(0, 0)
    p2 = Point(4, 4)
    p3 = Point(4, 0)
    
    # Distance
    assert p1.dist(p3) == 4.0
    
    # Orientation 0,0 -> 4,4 -> 4,0 (Right turn) = Clockwise (1)
    # (4-0)*(4-4) - (4-0)*(0-4) = 0 - (-16) = 16 > 0 -> 1
    assert orientation(p1, p2, p3) == 1
    
    print("[PASS] Geometry Basics")

if __name__ == "__main__":
    run_tests()
