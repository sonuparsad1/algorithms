# Exception Handling Examples

## Example 1: File Processing with Error Handling
```python
def read_config(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Config file {filename} not found, using defaults")
        return "{}"
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

config = read_config("config.json")
```

## Example 2: Input Validation
```python
def get_positive_number():
    while True:
        try:
            value = int(input("Enter a positive number: "))
            if value <= 0:
                raise ValueError("Number must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

number = get_positive_number()
```

## Example 3: API Request with Retry
```python
import time

def fetch_data(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            # Simulated API call
            response = make_request(url)
            return response
        except ConnectionError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            else:
                raise
```
