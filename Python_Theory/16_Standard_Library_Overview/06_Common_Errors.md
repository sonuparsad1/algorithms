# Common Standard Library Errors

## 1. Import Errors
```python
# WRONG - Incorrect module name
import Collections  # ModuleNotFoundError

# CORRECT
import collections
```

## 2. datetime Timezone Issues
```python
# WRONG - Naive datetime
from datetime import datetime
now = datetime.now()  # No timezone info

# CORRECT
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
```

## 3. json Serialization Errors
```python
# WRONG - Can't serialize datetime
import json
from datetime import datetime
json.dumps({'time': datetime.now()})  # TypeError

# CORRECT
json.dumps({'time': datetime.now().isoformat()})
```

## 4. pathlib vs os.path Mixing
```python
# WRONG - Mixing types
from pathlib import Path
import os
path = Path('file.txt')
os.path.join(path, 'other')  # TypeError

# CORRECT - Use one or the other
path = Path('file.txt') / 'other'
```

## 5. Regular Expression Errors
```python
# WRONG - Unescaped special characters
import re
re.search('.', 'test')  # Matches any character!

# CORRECT
re.search(r'\.', 'test')  # Matches literal dot
```
