# Python Study Repo - Style Guide

## General Convention
- **Naming**: `snake_case` for variables and functions. `PascalCase` for classes.
- **Type Hints**: Use `python 3.9+` style hints (e.g., `list[int]`, `dict[str, Any]`).
- **Docstrings**: Google style or simple one-liners for obvious functions.
- **Line Length**: Soft limit 100 characters.

## File Structure
Every file must start with a header comment block:
```python
"""
Title: [Concept Name]
Topic: [Category]

Theory:
    [Explanation]

Complexity:
    Time: O(...)
    Space: O(...)
"""
```

## Testing Protocol
- Include a `if __name__ == "__main__":` block.
- Use `assert` statements for simple verifications.
- Print clear success messages, e.g., `print("[PASS] Quick Sort tests passed")`.
- Avoid external testing dependencies for individual files (keep them self-contained).

## Pitfalls & Variations
- Explicitly comment on *why* a certain approach is taken if it's not the most obvious one.
- Show "Bad" vs "Good" code comparisons if relevant.
