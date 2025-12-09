"""
Title: Metaclasses Practical Patterns
Topic: Advanced OOP

Patterns:
    1. Validation: Check if class defines required methods or follows conventions.
    2. Registration: Automatically register plugins/subclasses.
    3. Auto-Decoration: Apply decorators to all methods in a class.
"""

# ==========================================
# 1. Plugin Registry Pattern
# ==========================================

class PluginMeta(type):
    registry = {}
    
    def __init__(cls, name, bases, dct):
        if name != "PluginBase":
            print(f"Registering plugin: {name}")
            PluginMeta.registry[name] = cls
        super().__init__(name, bases, dct)

class PluginBase(metaclass=PluginMeta):
    pass

class AudioPlugin(PluginBase):
    pass

class VideoPlugin(PluginBase):
    pass


# ==========================================
# 2. Enforcement Pattern
# ==========================================

class EnforcerMeta(type):
    def __new__(mcs, name, bases, dct):
        if name != "EnforcedBase":
            if 'required_method' not in dct:
                raise TypeError(f"Class {name} missing 'required_method'")
        return super().__new__(mcs, name, bases, dct)

class EnforcedBase(metaclass=EnforcerMeta):
    pass

def run_tests():
    # 1. Registry
    keys = PluginMeta.registry.keys()
    assert "AudioPlugin" in keys
    assert "VideoPlugin" in keys
    assert "PluginBase" not in keys
    
    # 2. Enforcement
    try:
        class BrokenPlugin(EnforcedBase):
            pass
    except TypeError as e:
        print(f"Caught expected metaclass error: {e}")

    class GoodPlugin(EnforcedBase):
        def required_method(self): pass
    
    print("[PASS] Metaclass patterns")

if __name__ == "__main__":
    run_tests()
