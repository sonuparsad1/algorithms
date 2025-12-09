"""
Title: Line Intersection
Topic: Geometry Algorithms

Theory:
    Two lines (p1,q1) and (p2,q2) intersect if:
    (p1, q1, p2) and (p1, q1, q2) have different orientations AND
    (p2, q2, p1) and (p2, q2, q1) have different orientations.
    
    Special case: Collinear segments.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def on_segment(p, q, r):
    return (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
            q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y))

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0: return 0
    return 1 if val > 0 else 2

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    # General Case
    if o1 != o2 and o3 != o4:
        return True
        
    # Special Cases
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True
    
    return False

def run_tests():
    p1 = Point(1, 1)
    q1 = Point(10, 1)
    p2 = Point(1, 2)
    q2 = Point(10, 2)
    
    assert do_intersect(p1, q1, p2, q2) == False # Parallel
    
    p3 = Point(5, 5)
    q3 = Point(5, 0) # Vertical crossing both horizontal
    assert do_intersect(p1, q1, p3, q3) == True
    
    print("[PASS] Line Intersection")

if __name__ == "__main__":
    run_tests()
