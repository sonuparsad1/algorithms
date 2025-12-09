"""
Title: Structural Patterns (Adapter, Decorator, Facade, Proxy)
Topic: Design Patterns

Theory:
    Focus on class and object composition.
    
    1. Adapter: Convert interface of a class into another client expects.
    2. Decorator: Add responsibility dynamically (covered in Advanced).
    3. Facade: Simplified interface to a complex system.
    4. Proxy: Placeholder for another object to control access.
"""

# ==========================================
# 1. Adapter
# ==========================================

class EuropeanSocket:
    def voltage(self): return 220

class USASocket:
    def voltage(self): return 110

class AdapterEUtoUSA:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        # Convert 220 -> 110
        return self.socket.voltage() / 2

# ==========================================
# 2. Facade
# ==========================================

class CPU:
    def freeze(self): print("CPU frozen")
    def execute(self): print("CPU Executing")

class Memory:
    def load(self): print("Memory loading")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.mem = Memory()
    
    def start(self):
        self.cpu.freeze()
        self.mem.load()
        self.cpu.execute()

# ==========================================
# 3. Proxy
# ==========================================

class RealImage:
    def display(self):
        return "Displaying Image"

class ProxyImage:
    def __init__(self):
        self.real_image = None
    
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage() # Lazy Load
        return self.real_image.display()

def run_tests():
    # Adapter
    eu = EuropeanSocket()
    adapter = AdapterEUtoUSA(eu)
    assert adapter.voltage() == 110
    
    # Facade
    print("--- Facade Start ---")
    ComputerFacade().start()
    
    # Proxy
    p = ProxyImage()
    assert p.real_image is None
    assert p.display() == "Displaying Image"
    assert p.real_image is not None
    
    print("[PASS] Structural Patterns")

if __name__ == "__main__":
    run_tests()
