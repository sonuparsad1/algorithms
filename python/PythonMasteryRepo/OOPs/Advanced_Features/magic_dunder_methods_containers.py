"""
Title: Container Magic Methods
Topic: Advanced OOP

Theory:
    Make your object act like a list, dict, or set.
    
    KEY METHODS:
    - `__len__`: for `len(obj)`
    - `__getitem__`: for `obj[key]`
    - `__setitem__`: for `obj[key] = value`
    - `__delitem__`: for `del obj[key]`
    - `__iter__`: for `for x in obj`
    - `__contains__`: for `item in obj`

    Complexity:
    - Implementing these allows usage with `random.choice`, slicing, unpacking, etc.
"""

class CustomList:
    """A wrapper around list that logs operations."""
    def __init__(self, *args):
        self._items = list(args)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return self._items[index]

    def __setitem__(self, index, value):
        print(f"Setting index {index} to {value}")
        self._items[index] = value

    def __delitem__(self, index):
        print(f"Deleting index {index}")
        del self._items[index]

    def __iter__(self):
        return iter(self._items)

    def __contains__(self, item):
        return item in self._items

def run_tests():
    c = CustomList(1, 2, 3, 4)
    
    # Test len
    assert len(c) == 4
    
    # Test getitem
    assert c[0] == 1
    
    # Test setitem
    c[0] = 100
    assert c[0] == 100
    
    # Test contains
    assert 100 in c
    assert 99 not in c
    
    # Test iter
    assert list(c) == [100, 2, 3, 4]
    
    print("[PASS] Container Magic methods verified")

if __name__ == "__main__":
    run_tests()
