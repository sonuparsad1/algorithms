"""
Title: Instance vs Class Variables
Topic: OOP Basics

Theory:
    - Class Variables: Shared by all instances of a class. Defined directly in the class body.
      Any change affects all instances *unless shadowed*.
    - Instance Variables: Unique to each instance. Defined inside methods (usually `__init__`) using `self`.

    Scope Resolution:
    When accessing `obj.attr`, Python looks up:
    1. Instance namespace (`obj.__dict__`)
    2. Class namespace (`type(obj).__dict__`)
    3. Base classes.

Pitfalls:
    - Shadowing: Assigning to `self.class_var` creates a new instance variable, masking the class variable for that instance,
      but not changing the class variable itself.
"""

# ==========================================
# 1. Basic Comparison
# ==========================================

class Employee:
    # Class Variable
    company_name = "TechCorp"
    employee_count = 0  # To track total employees

    def __init__(self, name: str):
        # Instance Variable
        self.name = name
        
        # Modifying class variable needs class reference
        Employee.employee_count += 1

    def change_company(self, new_name):
        # This shadows the class variable for THIS instance only!
        self.company_name = new_name 


# ==========================================
# 2. Demonstration of Shadowing
# ==========================================

def demonstration():
    print("--- Class vs Instance Vars ---")
    e1 = Employee("Alice")
    e2 = Employee("Bob")

    print(f"Start: e1 company: {e1.company_name}, e2 company: {e2.company_name}")
    assert e1.company_name == "TechCorp"

    # Modifying Class Variable properly
    Employee.company_name = "GlobalTech"
    print(f"After Class Change: e1: {e1.company_name}, e2: {e2.company_name}")
    assert e1.company_name == "GlobalTech"
    assert e2.company_name == "GlobalTech"

    # Accidental Shadowing
    print("\n--- Shadowing Pitfall ---")
    e1.company_name = "StartupInc" # Creates e1.company_name, leaves Employee.company_name alone
    
    print(f"e1: {e1.company_name}")         # StartupInc
    print(f"e2: {e2.company_name}")         # GlobalTech
    print(f"Class: {Employee.company_name}") # GlobalTech

    # accessing via __dict__
    print(f"e1 dict: {e1.__dict__}")
    print(f"e2 dict: {e2.__dict__}")


# ==========================================
# 3. Practical Usage: Counters and Configs
# ==========================================

class ServerConfig:
    DEFAULT_PORT = 8080 # Class var as constant reference
    
    def __init__(self, port=None):
        self.port = port or self.DEFAULT_PORT

# ==========================================
# Tests
# ==========================================

if __name__ == "__main__":
    demonstration()
    
    c = ServerConfig()
    assert c.port == 8080
    
    c2 = ServerConfig(9000)
    assert c2.port == 9000
    
    print("\n[PASS] Instance vs Class variable demo finished.")
