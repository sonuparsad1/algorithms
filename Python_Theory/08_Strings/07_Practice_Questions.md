# Practice Questions - Strings

## Questions

### Q1: Reverse a String
Write a function to reverse a string without using slicing.

### Q2: Count Vowels
Count the number of vowels in a string.

### Q3: Remove Whitespace
Remove all whitespace from a string.

### Q4: Anagram Checker
Check if two strings are anagrams.

### Q5: Caesar Cipher
Implement a Caesar cipher that shifts each letter by 3 positions.

---

## Solutions

### A1: Reverse String
```python
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("Python"))  # "nohtyP"
```

### A2: Count Vowels
```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # 3
```

### A3: Remove Whitespace
```python
def remove_whitespace(s):
    return s.replace(" ", "")

print(remove_whitespace("Hello World"))  # "HelloWorld"
```

### A4: Anagram Checker
```python
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```

### A5: Caesar Cipher
```python
def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - start + shift) % 26 + start)
            result += shifted
        else:
            result += char
    return result

print(caesar_cipher("Hello"))  # "Khoor"
```
