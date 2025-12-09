"""
Title: Exceptions Hierarchy and Custom Exceptions
Topic: Error Handling

Theory:
    All exceptions inherit from `BaseException`.
    Standard exceptions inherit from `Exception`.
    
    Structure:
    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- Exception
          +-- .... (ValueError, TypeError, etc)

    Best Practice:
    - Inherit from `Exception` for custom errors.
    - Don't catch `BaseException` unless intended (catches exit signals!).
"""

class MyAppError(Exception):
    """Base class for all app errors."""
    pass

class ValidationError(MyAppError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Invalid {field}: {message}")

class NetworkError(MyAppError):
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("age", "Must be positive")

def run_tests():
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"Caught: {e}")
        assert e.field == "age"
    except MyAppError:
        print("Caught generic app error")
    except Exception:
        print("Caught generic exception")

    print("[PASS] Custom Exceptions")

if __name__ == "__main__":
    run_tests()
