# Modules and Packages

## Definition

### Module
A **module** is a file containing Python code (functions, classes, variables). Any `.py` file is a module.
- Purpose: Organize code into logical units.
- Reusability: Write once, import anywhere.

### Package
A **package** is a directory containing multiple modules and a special `__init__.py` file.
- Purpose: Organize related modules into a hierarchy.
- Example: `numpy`, `django` are packages.

## Why Use Modules?

1. **Code Organization**: Break large programs into smaller, manageable files.
2. **Reusability**: Import the same code in multiple projects.
3. **Namespace Management**: Avoid name conflicts.
4. **Maintainability**: Easier to debug and update specific functionality.

## Module vs Script

| Aspect | Module | Script |
|--------|--------|--------|
| Purpose | To be imported | To be executed |
| `__name__` | Module name | `"__main__"` |
| Usage | `import mymodule` | `python script.py` |
