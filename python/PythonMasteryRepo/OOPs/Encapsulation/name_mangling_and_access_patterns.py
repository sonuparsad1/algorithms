"""
Title: Name Mangling and Access Patterns
Topic: Encapsulation

Theory:
    Name mangling is triggered by double underscores prefix `__var`.
    Python rewrites `__var` to `_ClassName__var`.

    Purpose: 
    - Prevent accidental overriding of internal variables in subclasses.
    - NOT for security (it is easily reversible).

    Access Patterns check:
    - `obj.public`
    - `obj._protected` (Trust based)
    - `getattr(obj, 'name')` (Dynamic access)
"""

# ==========================================
# 1. Subclass Collision mechanics
# ==========================================

class Base:
    def __init__(self):
        self.public = "Base Public"
        self._protected = "Base Protected"
        self.__private = "Base Private" # Becomes _Base__private

    def get_private(self):
        return self.__private

class Child(Base):
    def __init__(self):
        super().__init__()
        self.public = "Child Public"       # Overrides
        self._protected = "Child Protected" # Overrides
        self.__private = "Child Private"    # DOES NOT Override Base.__private!
        # Because this becomes _Child__private

    def get_child_private(self):
        return self.__private

# ==========================================
# Demonstration
# ==========================================

def run_demo():
    print("--- Name Mangling Logic ---")
    b = Base()
    c = Child() 

    # 1. Standard overrides
    assert c.public == "Child Public"
    assert c._protected == "Child Protected"

    # 2. Private variables do NOT collide
    print(f"Base Method returns: {c.get_private()}")       # Returns "Base Private"
    print(f"Child Method returns: {c.get_child_private()}") # Returns "Child Private"

    # 3. Inspecting the dictionary
    print(f"\nObject Dict keys: {c.__dict__.keys()}")
    
    # We should see '_Base__private' AND '_Child__private'
    assert '_Base__private' in c.__dict__
    assert '_Child__private' in c.__dict__

    print("[PASS] Name mangling prevented collision.")

if __name__ == "__main__":
    run_demo()
