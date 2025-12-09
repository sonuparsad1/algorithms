"""
Title: Layering and Package Structure
Topic: Architecture

Theory:
    Separation of Concerns is key.
    Typical Layers:
    1. Presentation / API Layer (Routes, CLI)
    2. Service / Business Logic Layer (Orchestration)
    3. Data Access Layer (Repositories, DB)
    4. Domain / Model Layer (Pure Python Objects)

    Dependency Rule: Inner layers (Domain) should NOT depend on outer layers (DB/Web).
"""

# ==========================================
# Domain Layer (Pure)
# ==========================================
class User:
    def __init__(self, name):
        self.name = name

# ==========================================
# Data Layer (Infrastructure)
# ==========================================
class UserRepo:
    def save(self, user):
        print(f"DB: INSERT INTO users ({user.name})")

# ==========================================
# Service Layer (Business Logic)
# ==========================================
class UserService:
    def __init__(self, repo):
        self.repo = repo
    
    def register(self, name):
        if len(name) < 3:
            raise ValueError("Name too short")
        u = User(name)
        self.repo.save(u)
        return u

# ==========================================
# Presentation Layer (e.g., Controller)
# ==========================================
def register_controller(name):
    # Wiring dependencies
    repo = UserRepo()
    svc = UserService(repo)
    try:
        svc.register(name)
        print("HTTP 201 Created")
    except ValueError as e:
        print(f"HTTP 400 Bad Request: {e}")

if __name__ == "__main__":
    print("--- Layering Demo ---")
    register_controller("Al")
    register_controller("Alice")
