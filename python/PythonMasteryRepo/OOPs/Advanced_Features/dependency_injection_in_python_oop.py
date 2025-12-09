"""
Title: Dependency Injection (DI)
Topic: Advanced OOP

Theory:
    DI is a technique where an object receives other objects that it depends on (dependencies).
    Instead of creating dependencies inside the object (`self.svc = Service()`), pass them in (`__init__(self, svc)`).
    
    Benefits:
    - Decoupling.
    - Testability (Easy to mock dependencies).
"""

class EmailService:
    def send(self, msg):
        return f"Real Email: {msg}"

class MockEmailService:
    def send(self, msg):
        return f"Mock Email: {msg}"

class NotificationManager:
    # Dependency is Injected
    def __init__(self, service):
        self.service = service
    
    def alert(self, msg):
        return self.service.send(msg)

def run_tests():
    # Production
    prod_svc = EmailService()
    prod_mgr = NotificationManager(prod_svc)
    assert prod_mgr.alert("Hi") == "Real Email: Hi"
    
    # Testing
    mock_svc = MockEmailService()
    test_mgr = NotificationManager(mock_svc)
    assert test_mgr.alert("Hi") == "Mock Email: Hi"
    
    print("[PASS] Dependency Injection")

if __name__ == "__main__":
    run_tests()
