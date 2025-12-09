# String Examples

## Example 1: Palindrome Checker
```python
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("racecar"))      # True
print(is_palindrome("A man a plan a canal Panama"))  # True
```

## Example 2: Word Counter
```python
text = "Python is awesome. Python is powerful."

words = text.lower().split()
word_count = {}

for word in words:
    word = word.strip(".,!?")
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'python': 2, 'is': 2, 'awesome': 1, 'powerful': 1}
```

## Example 3: Email Validator
```python
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))     # False
```

## Example 4: Title Case Converter
```python
text = "the quick brown fox"
title = text.title()
print(title)  # "The Quick Brown Fox"
```

## Example 5: Remove Duplicates
```python
text = "hello"
unique = "".join(sorted(set(text), key=text.index))
print(unique)  # "helo"
```
