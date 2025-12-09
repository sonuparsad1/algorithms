"""
Title: Polygon Area (Shoelace Formula)
Topic: Geometry Algorithms

Theory:
    Area = 0.5 * |sum(x_i * y_{i+1} - x_{i+1} * y_i)|
"""

def polygon_area(X, Y, n):
    area = 0.0
    j = n - 1
    
    for i in range(n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
        
    return abs(area / 2.0)

# Note: Formula above is a variation (Trapezoid formula), equivalent to Shoelace.
# Shoelace: (x1y2 + x2y3 ...) - (y1x2 + y2x3 ...)

def run_tests():
    # Square (0,0), (4,0), (4,4), (0,4) -> Area 16
    X = [0, 4, 4, 0]
    Y = [0, 0, 4, 4]
    
    assert polygon_area(X, Y, 4) == 16.0
    print("[PASS] Polygon Area")

if __name__ == "__main__":
    run_tests()
