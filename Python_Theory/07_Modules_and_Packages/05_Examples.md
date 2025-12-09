# Package Management with pip

## What is pip?

**pip** = "Pip Installs Packages"
- Python's package installer
- Installs packages from PyPI (Python Package Index)

## Basic Commands

### Install a Package
```bash
pip install package_name
pip install requests
```

### Install Specific Version
```bash
pip install package_name==1.2.3
pip install numpy==1.21.0
```

### Upgrade a Package
```bash
pip install --upgrade package_name
pip install -U numpy
```

### Uninstall a Package
```bash
pip uninstall package_name
```

### List Installed Packages
```bash
pip list
pip freeze  # Format suitable for requirements.txt
```

### Show Package Info
```bash
pip show package_name
```

## Requirements File

**requirements.txt**
```
numpy==1.21.0
pandas>=1.3.0
requests
```

### Install from requirements.txt
```bash
pip install -r requirements.txt
```

### Generate requirements.txt
```bash
pip freeze > requirements.txt
```

## Virtual Environments

### Why Use Virtual Environments?
- Isolate project dependencies
- Avoid version conflicts
- Reproducible environments

### Create Virtual Environment
```bash
# Using venv (built-in)
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Mac/Linux)
source myenv/bin/activate

# Deactivate
deactivate
```

### Using virtualenv
```bash
pip install virtualenv
virtualenv myenv
```

## Best Practices

1. **Always use virtual environments** for projects
2. **Pin versions** in requirements.txt for production
3. **Update regularly** but test thoroughly
4. **Use `pip list --outdated`** to check for updates
