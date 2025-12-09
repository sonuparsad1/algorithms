"""
Title: Interfaces via Protocols
Topic: Abstraction

Theory:
    Python doesn't have an `interface` keyword. 
    Traditionally, ABCs with ONLY abstract methods act as Interfaces.
    Modern approach: `typing.Protocol`, which allows for "Implicit Interfaces" (Go-style).

    Here we show ABC-as-Interface vs Protocol-as-Interface.
"""

from abc import ABC, abstractmethod
from typing import Protocol

# ==========================================
# 1. ABC as Interface (Explicit)
# ==========================================

class IRepository(ABC):
    @abstractmethod
    def save(self, obj): pass
    
    @abstractmethod
    def get(self, id): pass

class SQLRepo(IRepository):
    def save(self, obj): return "Saved SQL"
    def get(self, id): return "Got SQL"

# ==========================================
# 2. Protocol as Interface (Implicit)
# ==========================================

class Mailer(Protocol):
    def send(self, to: str, body: str) -> None:
        ...

class SmtpService:
    # No inheritance from Mailer needed
    def send(self, to: str, body: str) -> None:
        print(f"Sending email to {to}")

def trigger_email(service: Mailer):
    service.send("admin@test.com", "Alert")

# ==========================================
# Tests
# ==========================================

def run_tests():
    # ABC
    repo = SQLRepo()
    assert isinstance(repo, IRepository)
    
    # Protocol
    smtp = SmtpService()
    # Runtime check for protocol is messy without @runtime_checkable, 
    # but static type check works.
    trigger_email(smtp) # Works
    
    print("[PASS] Interface patterns")

if __name__ == "__main__":
    run_tests()
