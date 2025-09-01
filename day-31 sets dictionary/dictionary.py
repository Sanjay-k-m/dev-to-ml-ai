# dict_demo_with_output.py

# ---------------------------
# 1. Creating Dictionaries
# ---------------------------
# Using curly braces
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Initial dictionary:", my_dict)  
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Using dict() constructor
another_dict = dict(country='USA', language='English')
print("Another dictionary:", another_dict)  
# Output: {'country': 'USA', 'language': 'English'}

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)  
# Output: {}

# ---------------------------
# 2. Accessing Values
# ---------------------------
print("Name:", my_dict['name'])  
# Output: Alice

# Using get() (does not raise KeyError)
print("Salary:", my_dict.get('salary'))  
# Output: None
print("Salary with default:", my_dict.get('salary', 50000))  
# Output: 50000

# ---------------------------
# 3. Adding / Updating Items
# ---------------------------
my_dict['email'] = 'alice@example.com'  # Add new key
print("After adding email:", my_dict)  
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

my_dict['age'] = 26  # Update existing key
print("After updating age:", my_dict)  
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Using update() method
my_dict.update({'city': 'Boston', 'country': 'USA'})
print("After update:", my_dict)  
# Output: {'name': 'Alice', 'age': 26, 'city': 'Boston', 'email': 'alice@example.com', 'country': 'USA'}

# ---------------------------
# 4. Removing Items
# ---------------------------
removed_value = my_dict.pop('email')  # Remove key and return value
print("Removed value:", removed_value)  
# Output: alice@example.com
print("After pop:", my_dict)  
# Output: {'name': 'Alice', 'age': 26, 'city': 'Boston', 'country': 'USA'}

last_item = my_dict.popitem()  # Remove last inserted item (Python 3.7+)
print("Popped item:", last_item)  
# Output: ('country', 'USA')
print("After popitem:", my_dict)  
# Output: {'name': 'Alice', 'age': 26, 'city': 'Boston'}

# Delete using del
del my_dict['city']
print("After deleting city:", my_dict)  
# Output: {'name': 'Alice', 'age': 26}

# Clear dictionary
my_dict.clear()
print("After clearing:", my_dict)  
# Output: {}

# ---------------------------
# 5. Dictionary Operations
# ---------------------------
D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'b': 20, 'c': 3, 'd': 4}

# Keys, Values, Items
print("Keys:", D1.keys())  
# Output: dict_keys(['a', 'b', 'c'])
print("Values:", D1.values())  
# Output: dict_values([1, 2, 3])
print("Items:", D1.items())  
# Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Membership checks
print("'a' in D1:", 'a' in D1)  
# Output: True
print("1 in D1.values():", 1 in D1.values())  
# Output: True

# Merge dictionaries (Python 3.9+)
merged = D1 | D2
print("Merged dictionary:", merged)  
# Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}

# ---------------------------
# 6. Iterating Dictionaries
# ---------------------------
for key in D1:
    print("Key:", key, "Value:", D1[key])
# Output:
# Key: a Value: 1
# Key: b Value: 2
# Key: c Value: 3

for key, value in D1.items():
    print(f"{key} -> {value}")
# Output:
# a -> 1
# b -> 2
# c -> 3

# ---------------------------
# 7. Dictionary Comprehension
# ---------------------------
squared_dict = {x: x**2 for x in range(1, 6)}
print("Squared dictionary:", squared_dict)  
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional comprehension
even_squared = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print("Even squared dictionary:", even_squared)  
# Output: {2: 4, 4: 16}
