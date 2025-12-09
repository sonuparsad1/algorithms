"""
Title: Registry Pattern
Topic: Design Patterns

Theory:
    Global or scoped central place to store and retrieve objects/classes.
    Often used for Plugin systems (seen in Metaclasses example too).
"""

class Registry:
    _objects = {}

    @classmethod
    def register(cls, name, obj):
        cls._objects[name] = obj

    @classmethod
    def get(cls, name):
        return cls._objects.get(name)

# Decorator based registration
def register_service(name):
    def wrapper(cls):
        Registry.register(name, cls)
        return cls
    return wrapper

@register_service("auth")
class AuthService:
    def login(self): return "Logged in"

def run_tests():
    svc_cls = Registry.get("auth")
    assert svc_cls is AuthService
    
    svc = svc_cls()
    assert svc.login() == "Logged in"
    
    print("[PASS] Registry Pattern")

if __name__ == "__main__":
    run_tests()
