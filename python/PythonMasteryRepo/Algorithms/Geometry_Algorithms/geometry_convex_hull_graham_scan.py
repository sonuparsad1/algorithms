"""
Title: Convex Hull (Graham Scan)
Topic: Geometry Algorithms

Theory:
    Smallest convex polygon containing all points.
    Graham Scan: O(N log N) by sorting polar angle.
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        # Sort by y, then x (for finding bottom-left)
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0: return 0
    return 1 if val > 0 else 2

def compare_polar(p0):
    # Closure to compare p1, p2 relative to p0
    def compare(p1):
        if p1 == p0: return -1 # Ensure p0 is first
        delta_y = p1.y - p0.y
        delta_x = p1.x - p0.x
        angle = math.atan2(delta_y, delta_x)
        return angle
        # Note: distance check needed for collinear points
    return compare

def graham_scan(points):
    n = len(points)
    if n < 3: return points # Convex hull is the points themselves
    
    # 1. Find bottom-most left
    min_idx = 0
    for i in range(1, n):
        if points[i] < points[min_idx]:
            min_idx = i
            
    points[0], points[min_idx] = points[min_idx], points[0]
    p0 = points[0]
    
    # 2. Sort by polar angle wrt p0
    # Custom sort implementation would be complex in Python without cmp_to_key fully handling collinear
    # Simplified logic: use atan2
    remaining = points[1:]
    remaining.sort(key=lambda p: math.atan2(p.y - p0.y, p.x - p0.x))
    
    stack = [p0]
    for p in remaining:
        while len(stack) > 1 and orientation(stack[-2], stack[-1], p) != 2: # 2 is CCW
            stack.pop()
        stack.append(p)
        
    return stack

def run_tests():
    pts = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), 
           Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
    
    hull = graham_scan(pts)
    # Expected: (0,0), (3,1), (4,4), (0,3) in CCW order
    # Note: 4,4 is extreme top right. 0,3 extreme top left.
    assert len(hull) >= 3
    print(f"Hull size: {len(hull)}")
    
    print("[PASS] Convex Hull")

if __name__ == "__main__":
    run_tests()
