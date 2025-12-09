# Decorator Patterns

## Parameterized Decorators
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" 3 times
```

## Class Decorators
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def greet():
    print("Hello!")

greet()  # Call 1, Hello!
greet()  # Call 2, Hello!
```

## Stacking Decorators
```python
@decorator1
@decorator2
def func():
    pass

# Equivalent to:
func = decorator1(decorator2(func))
```

## Built-in Decorators
```python
class MyClass:
    @staticmethod
    def static_method():
        pass
    
    @classmethod
    def class_method(cls):
        pass
    
    @property
    def my_property(self):
        return self._value
```
