# Practice Questions - Data Structures

## Questions

### Q1: Merge Two Lists
Merge two sorted lists into one sorted list.

### Q2: Find Common Elements
Find common elements between two lists.

### Q3: Group Anagrams
Group words that are anagrams of each other.

### Q4: Two Sum Problem
Find two numbers in a list that add up to a target.

### Q5: Nested Dictionary Access
Access a deeply nested value safely.

---

## Solutions

### A1: Merge Sorted Lists
```python
def merge_sorted(list1, list2):
    return sorted(list1 + list2)

# OR using merge algorithm
def merge(l1, l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result
```

### A2: Common Elements
```python
def find_common(list1, list2):
    return list(set(list1) & set(list2))

print(find_common([1, 2, 3], [2, 3, 4]))  # [2, 3]
```

### A3: Group Anagrams
```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### A4: Two Sum
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

### A5: Safe Nested Access
```python
def safe_get(d, *keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d

data = {"a": {"b": {"c": 123}}}
print(safe_get(data, "a", "b", "c"))  # 123
print(safe_get(data, "a", "x", "c"))  # None
```
