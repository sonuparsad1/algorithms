"""
Title: Creational Patterns (Singleton, Factory, Builder)
Topic: Design Patterns

Theory:
    Focus on object creation mechanisms.
    
    1. Singleton: Ensure a class has only one instance.
    2. Factory: Delegate object creation to a factory class/method.
    3. Builder: Construct complex objects step-by-step.
"""

# ==========================================
# 1. Singleton (Decorator approach)
# ==========================================

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

# ==========================================
# 2. Factory Method
# ==========================================

class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof"

class Cat(Animal):
    def speak(self): return "Meow"

class AnimalFactory:
    @staticmethod
    def create_animal(kind):
        if kind == "dog": return Dog()
        if kind == "cat": return Cat()
        raise ValueError("Unknown animal")

# ==========================================
# 3. Builder
# ==========================================

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
    
    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, GPU: {self.gpu}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def add_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def add_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def build(self):
        return self.computer

def run_tests():
    # Singleton
    d1 = Database()
    d2 = Database()
    assert d1 is d2
    
    # Factory
    dog = AnimalFactory.create_animal("dog")
    assert dog.speak() == "Woof"
    
    # Builder (Fluent API)
    pc = ComputerBuilder().add_cpu("M1").add_ram("16GB").build()
    assert pc.cpu == "M1"
    assert pc.gpu is None # Optional
    
    print("[PASS] Creational Patterns")

if __name__ == "__main__":
    run_tests()
