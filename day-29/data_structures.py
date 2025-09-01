# ########################################
# Python Collections: List, Tuple, Set, Dictionary
# ########################################


###########################
# 1. LIST
###########################

# Lists are ordered, mutable (changeable), and allow duplicate values.
# Syntax: val = [elements]

val = [1, 2, 3, 'python', 2.34, 5, True, [1, 2, 4, 3, 2], {3, 4}, {3:2, 1234:234}, (2, 1, 4, 3)]

# Accessing elements
print(val[1])             # Indexing (Output: 2)
print(val[-1][-2])        # Nested indexing (2nd last from tuple at end)
print(len(val))           # Length of list
print(val[:4])            # Slicing (first 4 elements)
print(val[-3:-1])         # Slicing from end
print(val[2:-2:2])        # Slicing with step
print(val[::-1])          # Reverse using slicing

# Reversing a list in place
val.reverse()
print(val)

# Adding elements
val.append("sanjay")                     # Append a single element
print(val)

# Adding multiple elements from input as set
# val.append(set(input("Enter comma-separated values: ").split(',')))
# print(val)

# Removing elements
val = [1, 2, 3, 4, 'h1', 23]
del val[::2]                             # Delete every second element (0,2,4...)
print(val)

val.pop(2)                               # Removes element at index 2
print(val)

val.clear()                              # Clears all elements
print(val)

# Sorting a list (with numbers)
val = [2, 1, 3, 4, 5, 334, 2, 1, 23, 2, 4, 3, 21]
print("Original:", val)
val.sort()
print("Ascending:", val)
val.sort(reverse=True)
print("Descending:", val)

# Sorting a list of strings
val = ['apple', 'df', 'python', '10', 'sanjay', 'ab']
print(val, "raw value")

val.sort()                                # Sort by ASCII/lexicographical order
print(val, "sorted by ASCII")

val.sort(key=len)                         # Sort by length of string
print(val, "sorted by length")

# Common List Methods Summary
"""
val.append(x)        → Adds an item to the end
val.extend(iterable) → Adds all elements of an iterable
val.insert(i, x)     → Inserts an item at index i
val.remove(x)        → Removes first occurrence of x
val.pop([i])         → Removes and returns item at index i (last if not specified)
val.clear()          → Removes all items
val.index(x)         → Returns index of first occurrence of x
val.count(x)         → Counts occurrences of x
val.sort()           → Sorts the list in ascending order
val.reverse()        → Reverses the list
"""



###########################
# 2. TUPLE
###########################

# Tuples are ordered, immutable, and allow duplicates.
# Syntax: tup = (elements,)

tup = (1, 2, 3, 'hello', 3.4, True, [1, 2], (4, 5))

print(tup[3])            # Access element
print(tup[-1][1])        # Nested indexing
print(len(tup))          # Length

# Tuple methods
print(tup.count(3))      # Count of value 3
print(tup.index('hello'))  # Index of 'hello'

# Tuples are immutable; you can't change or append elements directly.

"""
Tuple Methods Summary:
tup.count(x)     → Returns count of x
tup.index(x)     → Returns first index of x
"""



###########################
# 3. SET
###########################

# Sets are unordered, mutable, and do not allow duplicates.
# Syntax: s = {elements}

s = {1, 2, 3, 4, 2, 3, 5}
print(s)                # Duplicate values removed

# Adding elements
s.add(6)
print(s)

# Updating multiple elements
s.update([7, 8, 9])
print(s)

# Removing elements
s.remove(4)             # Removes 4, raises KeyError if not found
s.discard(100)          # Removes 100 if present; no error if not
print(s)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))             # Union
print(a.intersection(b))      # Intersection
print(a.difference(b))        # a - b
print(a.symmetric_difference(b))  # Elements in a or b but not both

# Set methods
"""
s.add(x)                   → Add element x
s.update(iterable)         → Add multiple elements
s.remove(x)                → Remove x (raises error if not found)
s.discard(x)               → Remove x (no error if not found)
s.pop()                    → Remove arbitrary element
s.clear()                  → Clear all elements
s.union(s2), s | s2        → Union
s.intersection(s2), s & s2 → Intersection
s.difference(s2), s - s2   → Difference
s.symmetric_difference(s2) → Symmetric Difference
"""



###########################
# 4. DICTIONARY
###########################

# Dictionaries are unordered (as of Python 3.6+, they maintain insertion order), mutable, and store key-value pairs.
# Syntax: d = {key: value}

d = {'name': 'Sanjay', 'age': 25, 'lang': 'Python'}
print(d['name'])                  # Accessing value by key

# Adding/updating values
d['city'] = 'New York'
d['age'] = 26
print(d)

# Removing elements
d.pop('lang')                    # Removes key 'lang'
print(d)

del d['city']                    # Delete by key
print(d)

# Accessing keys, values, items
print(d.keys())
print(d.values())
print(d.items())

# Looping through dict
for key, value in d.items():
    print(f"{key}: {value}")

# Using get() to avoid KeyError
print(d.get('name'))
print(d.get('gender', 'Not Found'))   # Default value if key not found

# Dictionary methods
"""
d.keys()             → Returns all keys
d.values()           → Returns all values
d.items()            → Returns all (key, value) pairs
d.get(k[, default])  → Returns value for key k, or default if not found
d.pop(k)             → Removes key and returns its value
d.update(other_dict) → Updates dictionary with key-value pairs from other_dict
d.clear()            → Removes all items
"""

# | Type       | Ordered | Mutable | Allows Duplicates      | Syntax Example     |
# | ---------- | ------- | ------- | ------------------     | ------------------ |
# | List       | ✅       | ✅       | ✅                   | `[1, 2, 3]`        |
# | Tuple      | ✅       | ❌       | ✅                   | `(1, 2, 3)`        |
# | Set        | ❌       | ✅       | ❌                   | `{1, 2, 3}`        |
# | Dictionary | ✅       | ✅       | Keys: ❌, Values: ✅ | `{'a': 1, 'b': 2}` |
