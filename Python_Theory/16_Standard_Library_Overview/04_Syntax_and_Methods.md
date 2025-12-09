# Standard Library Methods and Tools

## `pathlib` - Modern Path Handling
```python
from pathlib import Path

# Create path
path = Path('folder') / 'file.txt'

# Check existence
if path.exists():
    content = path.read_text()

# Iterate directory
for file in Path('.').glob('*.py'):
    print(file)
```

## `argparse` - Command Line Arguments
```python
import argparse

parser = argparse.ArgumentParser(description='Process files')
parser.add_argument('filename', help='Input file')
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()
print(args.filename)
```

## `logging` - Logging Framework
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

## `unittest` - Testing Framework
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
    
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()
```
