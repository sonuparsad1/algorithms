"""
Title: Fractional Knapsack
Topic: Greedy Algorithms

Theory:
    Given weights and values, put items in knapsack of capacity W.
    We CAN break items (take fraction).
    
    Greedy Strategy: Sort by Ratio (Value/Weight) Descending.
    
    Complexity: O(N log N).
"""

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(W, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_val = 0.0
    current_weight = 0
    
    for item in items:
        if current_weight + item.weight <= W:
            current_weight += item.weight
            total_val += item.value
        else:
            remain = W - current_weight
            total_val += item.value * (remain / item.weight)
            break
            
    return total_val

def run_tests():
    W = 50
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    # Ratios: 6, 5, 4.
    # Take Item 1 (60, 10). W left 40. Val 60.
    # Take Item 2 (100, 20). W left 20. Val 160.
    # Take 20/30 of Item 3. Val 160 + 120*(2/3) = 160+80 = 240.
    
    assert fractional_knapsack(W, items) == 240.0
    print("[PASS] Fractional Knapsack")

if __name__ == "__main__":
    run_tests()
