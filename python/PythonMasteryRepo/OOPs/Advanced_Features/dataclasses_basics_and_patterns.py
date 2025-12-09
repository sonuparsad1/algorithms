"""
Title: Dataclasses
Topic: Advanced OOP

Theory:
    Introduced in Python 3.7.
    Decorator `@dataclass` automatically generates:
    - `__init__`
    - `__repr__`
    - `__eq__`
    
    Advanced features:
    - `frozen=True` (Immutability)
    - `order=True` (Comparison methods)
    - `field(default_factory=...)` for mutable defaults.
    - `__post_init__` for post-creation logic.
"""

from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class InventoryItem:
    name: str = field(compare=False)
    unit_price: float
    quantity_on_hand: int = 0
    
    # Computed list, mutable default must use factory
    tags: List[str] = field(default_factory=list, repr=False)

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
    def __post_init__(self):
        """Called after __init__"""
        if self.unit_price < 0:
            raise ValueError("Price cannot be negative")

def run_tests():
    item1 = InventoryItem("Widget", 10.0, 5)
    item2 = InventoryItem("Gadget", 20.0, 2)
    
    # 1. Ordering (by unit_price because it is first field with compare=True default? 
    # Actually fields are ordered by definition. name has compare=False, so price is first sort key.
    # unit_price(10) < unit_price(20)
    assert item1 < item2 
    
    # 2. Defaults
    assert item1.tags == []
    item1.tags.append("New")
    item3 = InventoryItem("Copy", 10.0)
    assert item3.tags == [] # Safety check
    
    # 3. Post Init
    try:
        InventoryItem("Test", -5.0)
    except ValueError:
        print("Caught validation error")
        
    print(f"Repr: {item1}") # Should not show tags
    
    print("[PASS] Dataclasses patterns")

if __name__ == "__main__":
    run_tests()
