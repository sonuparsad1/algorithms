"""
Title: Duck Typing and EAFP
Topic: Polymorphism

Theory:
    Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck."
    We check for behaviors (methods presence) rather than type.

    EAFP: Easier to Ask for Forgiveness than Permission.
    Try doing the operation, and catch the exception if it fails.
    Contrast with LBYL (Look Before You Leap).
"""

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

class Car:
    def honk(self):
        print("Beep")

# ==========================================
# 1. Duck Typing
# ==========================================

def make_it_quack(obj):
    # Doesn't care if it's a Duck or Person, as long as it has .quack()
    try:
        obj.quack()
        return True
    except AttributeError:
        print("This object cannot quack")
        return False

# ==========================================
# 2. EAFP vs LBYL
# ==========================================

def get_value_eafp(data, key):
    try:
        return data[key]
    except KeyError:
        return None

def get_value_lbyl(data, key):
    if key in data:
        return data[key]
    return None

# ==========================================
# Tests
# ==========================================

def run_tests():
    d = Duck()
    p = Person()
    c = Car()

    assert make_it_quack(d) == True
    assert make_it_quack(p) == True
    assert make_it_quack(c) == False
    
    print("[PASS] Duck typing verification")

if __name__ == "__main__":
    run_tests()
