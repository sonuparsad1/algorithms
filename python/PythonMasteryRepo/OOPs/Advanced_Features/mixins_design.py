"""
Title: Mixins Design Pattern
Topic: Advanced OOP

Theory:
    A Mixin is a class that provides methods to other classes but is not considered a "base class" in the hierarchy sense.
    It doesn't define state (ideally).
    
    Usage:
    `class MyClass(Mixin1, Mixin2, Base):`
    
    Mixins usually appear *before* the base class in inheritance list so their methods override/augment the base.
"""

import json

class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        # Assuming simple kwargs init
        return cls(**data)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class SerializableUser(JsonSerializableMixin, User):
    pass

def run_tests():
    u = SerializableUser(name="Alice", email="alice@example.com")
    
    # 1. Serialization
    j = u.to_json()
    print(f"JSON: {j}")
    assert '"name": "Alice"' in j
    
    # 2. Deserialization
    u2 = SerializableUser.from_json(j)
    assert u2.name == u.name
    assert u2.email == u.email
    assert isinstance(u2, SerializableUser)
    
    print("[PASS] Mixin usage verified")

if __name__ == "__main__":
    run_tests()
