# Standard Library Examples

## Example 1: Configuration File Parser
```python
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Read values
db_host = config['database']['host']
db_port = config.getint('database', 'port')
```

## Example 2: CSV Processing
```python
import csv
from collections import Counter

def analyze_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        ages = [int(row['age']) for row in reader]
    
    return {
        'count': len(ages),
        'average': sum(ages) / len(ages),
        'min': min(ages),
        'max': max(ages)
    }
```

## Example 3: Web Scraping
```python
from urllib.request import urlopen
import json

def fetch_data(url):
    with urlopen(url) as response:
        data = response.read()
    return json.loads(data)
```

## Example 4: Temporary Files
```python
import tempfile

# Temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write("Temporary data")
    temp_path = f.name

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    # Use tmpdir
    pass
```

## Example 5: Command Execution
```python
import subprocess

# Run command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```
