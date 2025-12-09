"""
Title: Composition over Inheritance
Topic: Advanced OOP

Theory:
    "Has-a" relationship (Composition) is often more flexible than "Is-a" (Inheritance).
    
    Inheritance: Tight coupling. Subclass depends on Base internals.
    Composition: Loose coupling. Object holds reference to another object and delegates tasks.
    
    Guideline: Prefer Composition for code reuse. Use Inheritance for polymorphism (Is-a).
"""

# ==========================================
# 1. Inheritance (Rigid)
# ==========================================

class Engine:
    def start(self): return "Vroom"

class CarWithInheritance(Engine):
    # Car IS-A Engine? No. Bad design.
    def drive(self):
        return f"{self.start()} and go"

# ==========================================
# 2. Composition (Flexible)
# ==========================================

class ElectricEngine:
    def start(self): return "Silent hum"

class CarWithComposition:
    def __init__(self, engine):
        self.engine = engine # Has-a Engine
    
    def drive(self):
        return f"{self.engine.start()} and go"

def run_tests():
    # Inheritance
    c1 = CarWithInheritance()
    assert c1.drive() == "Vroom and go"
    
    # Composition - Easy to swap behavior
    v8 = Engine()
    tesla_motor = ElectricEngine()
    
    c_gas = CarWithComposition(v8)
    c_ev = CarWithComposition(tesla_motor)
    
    assert c_gas.drive() == "Vroom and go"
    assert c_ev.drive() == "Silent hum and go"
    
    print("[PASS] Composition over Inheritance")

if __name__ == "__main__":
    run_tests()
