"""
Title: Serialization (Pickle, JSON, Dataclasses)
Topic: Architecture/Persistence

Theory:
    Serialization: Converting objects to byte/string stream.
    
    1. Pickle: Python specific, supports almost anything. WARNING: Unsecure (RCE risk).
    2. JSON: Text-based, cross-language. Safe. 
    3. Dataclasses: `asdict` helper makes JSON conversion easy.
"""

import pickle
import json
import dataclasses
from dataclasses import dataclass

@dataclass
class Config:
    theme: str
    volume: int

def run_tests():
    c = Config("Dark", 80)
    
    # 1. Pickle
    serialized_bytes = pickle.dumps(c)
    print(f"Pickle: {serialized_bytes}")
    c_restored = pickle.loads(serialized_bytes)
    assert c == c_restored

    # 2. JSON via asdict
    d = dataclasses.asdict(c)
    json_str = json.dumps(d)
    print(f"JSON: {json_str}")
    
    # Restore
    data = json.loads(json_str)
    c_json = Config(**data)
    assert c == c_json
    
    print("[PASS] Serialization")

if __name__ == "__main__":
    run_tests()
