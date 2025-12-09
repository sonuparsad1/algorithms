# Indentation and Comments

## Definition
**Indentation** refers to the spaces at the beginning of a code line. In Python, it is not just for readability but is a **syntactic requirement** to define blocks of code.
**Comments** are text ignored by the interpreter, used to explain code or leave notes.

## Theory
- **Indentation**: Most languages (C++, Java) use braces `{}` to define scope. Python uses whitespace. This enforces readability ("readability counts").
- **Comments**: Critical for collaboration. Python supports single-line comments and docstrings (documentation strings) for modules, classes, and functions.

## Syntax and Rules

### Indentation
- **Standard**: 4 spaces per level (PEP 8 recommendation).
- **Rule**: All statements in the same block must have the same indentation level.
- **Tabs vs Spaces**: Do not mix them. Using spaces is the preferred method.

### Comments
- **Single-line**: Starts with `#`.
- **Multi-line (Docstrings)**: Enclosed in `"""` or `'''`. While technically string literals, when placed at the start of a function/module, they act as documentation.

## Examples

```python
# This is a single-line comment

def example_function():
    """
    This is a docstring.
    It explains the function.
    """
    if True:
        # This block is indented
        print("Indentation matters!")
    # End of if block
# End of function
```

## Common Errors
1.  **IndentationError: unexpected indent**: Adding spaces where they aren't needed.
2.  **IndentationError: unindent does not match any outer indentation level**: Messy structure.
3.  **TabError**: Mixing tabs and spaces.
