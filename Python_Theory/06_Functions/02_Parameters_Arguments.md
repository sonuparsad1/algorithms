# Parameters and Arguments

## Definition
- **Parameter**: The variable listed inside the parentheses in the function definition.
- **Argument**: The value that is sent to the function when it is called.

## Types of Arguments

### 1. Positional Arguments
The most common type. Arguments must be passed in the correct order.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("hamster", "Harry")
```

### 2. Keyword Arguments
You specify the parameter name when calling the function. Order doesn't matter.

```python
describe_pet(pet_name="Harry", animal_type="hamster")
```

### 3. Default Arguments
Parameters can have default values. If the argument is omitted, the default is used.

```python
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Willie")         # Uses default "dog"
describe_pet("Harry", "cat")   # Overrides default
```

### 4. Arbitrary Arguments (`*args`)
Used when you don't know how many arguments will be passed. Receiving a tuple of arguments.

```python
def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")
```

### 5. Arbitrary Keyword Arguments (`**kwargs`)
Used when you don't know how many keyword arguments will be passed. Receives a dictionary.

```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
```
