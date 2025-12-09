"""
Title: Closest Pair of Points
Topic: Geometry Algorithms

Theory:
    Find pair of points with minimum distance.
    Divide and Conquer O(N log N).
    
    Base case: Brute force for small N.
    Merge step: Check strip around dividing line.
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            val = dist(P[i], P[j])
            if val < min_val:
                min_val = val
    return min_val

def strip_closest(strip, size, d):
    min_val = d
    strip.sort(key=lambda p: p.y)
    
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) >= min_val:
                break
            d_val = dist(strip[i], strip[j])
            if d_val < min_val:
                min_val = d_val
    return min_val

def closest_util(P, n):
    if n <= 3:
        return brute_force(P, n)
        
    mid = n // 2
    mid_point = P[mid]
    
    dl = closest_util(P[:mid], mid)
    dr = closest_util(P[mid:], n - mid)
    d = min(dl, dr)
    
    strip = []
    for i in range(n):
        if abs(P[i].x - mid_point.x) < d:
            strip.append(P[i])
            
    return min(d, strip_closest(strip, len(strip), d))

def closest(P, n):
    P.sort(key=lambda p: p.x)
    return closest_util(P, n)

def run_tests():
    P = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
    # Closest: (2,3) and (3,4) dist ~1.414 OR (2,3) and (5,1) dist ~3.6
    # Actually (2,3) and (3,4) is smallest.
    
    d = closest(P, len(P))
    # dist((2,3), (3,4)) = sqrt(1+1) = 1.414
    assert abs(d - 1.414213) < 0.001
    print("[PASS] Closest Pair")

if __name__ == "__main__":
    run_tests()
