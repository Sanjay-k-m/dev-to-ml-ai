# sets_demo_with_output.py

# ---------------------------
# 1. Creating Sets
# ---------------------------
# Using curly braces
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)  
# Output: Initial set: {1, 2, 3, 4, 5}  (unordered collection of unique elements)

# Using the set() constructor
another_set = set([4, 5, 6, 7])
print("Another set:", another_set)  
# Output: Another set: {4, 5, 6, 7}

# Empty set
empty_set = set()
print("Empty set:", empty_set)  
# Output: Empty set: set()

# ---------------------------
# 2. Adding Elements
# ---------------------------
my_set.add(6)  # Add single element
print("After adding 6:", my_set)  
# Output: After adding 6: {1, 2, 3, 4, 5, 6}

my_set.update([7, 8, 9])  # Add multiple elements
print("After updating with [7, 8, 9]:", my_set)  
# Output: After updating with [7, 8, 9]: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ---------------------------
# 3. Removing Elements
# ---------------------------
my_set.remove(9)  # Remove element (KeyError if not found)
print("After removing 9:", my_set)  
# Output: After removing 9: {1, 2, 3, 4, 5, 6, 7, 8}

my_set.discard(10)  # Remove element (no error if not found)
print("After discarding 10:", my_set)  
# Output: After discarding 10: {1, 2, 3, 4, 5, 6, 7, 8}

removed_element = my_set.pop()  # Remove and return arbitrary element
print("Popped element:", removed_element)  
# Output: Popped element: 1 (could be any element)
print("Set after pop:", my_set)  
# Output: Set after pop: {2, 3, 4, 5, 6, 7, 8}

my_set.clear()  # Remove all elements
print("After clearing:", my_set)  
# Output: After clearing: set()

# ---------------------------
# 4. Set Operations
# ---------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)  
# Output: A: {1, 2, 3, 4}
print("B:", B)  
# Output: B: {3, 4, 5, 6}

# Union
print("A | B (union):", A | B)  
# Output: A | B (union): {1, 2, 3, 4, 5, 6}

# Intersection
print("A & B (intersection):", A & B)  
# Output: A & B (intersection): {3, 4}

# Difference
print("A - B (difference):", A - B)  
# Output: A - B (difference): {1, 2}

# Symmetric Difference
print("A ^ B (symmetric difference):", A ^ B)  
# Output: A ^ B (symmetric difference): {1, 2, 5, 6}

# ---------------------------
# 5. Subset / Superset / Disjoint
# ---------------------------
C = {1, 2}
print("C:", C)  
# Output: C: {1, 2}

print("C <= A (C is subset of A):", C <= A)  
# Output: True
print("A >= C (A is superset of C):", A >= C)  
# Output: True
print("A.isdisjoint(B) (no common elements):", A.isdisjoint(B))  
# Output: False

# ---------------------------
# 6. Iterating Over a Set
# ---------------------------
for item in A:
    print("Item in A:", item)
# Output:
# Item in A: 1
# Item in A: 2
# Item in A: 3
# Item in A: 4

# ---------------------------
# 7. Other Useful Operations
# ---------------------------
# Length of set
print("Length of A:", len(A))  
# Output: 4

# Check membership
print("3 in A:", 3 in A)  
# Output: True
print("10 not in A:", 10 not in A)  
# Output: True

# Copying sets
D = A.copy()
print("Copy of A:", D)  
# Output: {1, 2, 3, 4}

# ---------------------------
# 8. Frozenset (immutable set)
# ---------------------------
frozen = frozenset([1, 2, 3])
print("Frozenset:", frozen)  
# Output: frozenset({1, 2, 3})
# frozen.add(4)  # This would raise an error

# ---------------------------
# 9. Set comprehension
# ---------------------------
squared_set = {x**2 for x in range(1, 6)}
print("Squared set:", squared_set)  
# Output: {1, 4, 9, 16, 25}
