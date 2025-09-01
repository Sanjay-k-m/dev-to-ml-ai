# String Methods Demonstration
# This file includes examples for various Python string methods with edge cases and explanations

# ============================================
# 🔍 index() vs find() – substring searching
# ============================================

val = "my name is sanjay km"
print(val.index('na'))              # 3 → First occurrence
print(val.index('na', 5))           # 11
print(val.index('na', 5, 15))       # 11

try:
    print(val.index('NA'))          # Raises ValueError: substring not found
except ValueError as e:
    print(f"index error: {e}")

# Edge case: Empty string
val_empty = ""
try:
    print(val_empty.index("a"))     # Raises ValueError: substring not found
except ValueError as e:
    print(f"index error: {e}")

# Overlapping substrings
val = "banana"
print(val.index("ana"))             # 1 (first occurrence)
print(val.index("ana", 2))          # 3 (first occurrence after index 2)

print(val.find('na'))               # 3
print(val.find('na', 5))            # -1 (not found after index 5)
print(val.find('na', 1, 4))         # 1
print(val.find('xyz'))              # -1 → not found

# Edge case: Empty string
print(val_empty.find("a"))          # -1 (not found)

# Case sensitivity
print(val.find("NA"))               # -1 (not found, case-sensitive)

# ============================================
# ✅ isalpha() – only letters (no digits, no space, no punctuation)
# ============================================

val = "Python"
print(val.isalpha())                # True

val = "Python3"
print(val.isalpha())                # False → digit included

val = "Data Science"
print(val.isalpha())                # False → contains space

val = ""
print(val.isalpha())                # False → empty string

# Unicode letters
val = "héllo"                       # Unicode accented letters
print(val.isalpha())                # True

# Mixed scripts
val = "αβγPython"                   # Greek letters + ASCII
print(val.isalpha())                # True

# Non-alphabetic Unicode
val = "½"                           # Fraction symbol
print(val.isalpha())                # False

# Single character
val = "a"
print(val.isalpha())                # True

# ============================================
# ✅ isdigit() – only digits (0-9)
# ============================================

val = "123456"
print(val.isdigit())                # True

val = "12 34"
print(val.isdigit())                # False → space included

val = "12.34"
print(val.isdigit())                # False → dot included

val = ""
print(val.isdigit())                # False

# Edge case: Unicode digits
val = "٠١٢"                        # Arabic-Indic digits
print(val.isdigit())                # True

# Single digit
val = "5"
print(val.isdigit())                # True

# ============================================
# ✅ isnumeric() – digits or Unicode numeric characters
# ============================================

val = "123"
print(val.isnumeric())              # True

val = "Ⅻ"                          # Roman numeral
print(val.isnumeric())              # True

val = "12.34"
print(val.isnumeric())              # False

val = "ten"
print(val.isnumeric())              # False

# Unicode numeric characters
val = "१२३"                        # Devanagari digits
print(val.isnumeric())              # True

val = "½"                           # Fraction
print(val.isnumeric())              # True

# Empty string
val = ""
print(val.isnumeric())              # False

# ============================================
# ✅ isdecimal() – only base-10 digits (0-9)
# ============================================

val = "45678"
print(val.isdecimal())              # True

val = "②③"                         # Unicode circled digits
print(val.isdecimal())              # False

val = "123.0"
print(val.isdecimal())              # False

# Unicode digits
val = "٠١٢"                        # Arabic-Indic digits
print(val.isdecimal())              # True

# Roman numerals
val = "Ⅻ"
print(val.isdecimal())              # False

# Single digit
val = "0"
print(val.isdecimal())              # True

# ============================================
# ✅ isalnum() – letters and digits only
# ============================================

val = "abc123"
print(val.isalnum())                # True

val = "abc 123"
print(val.isalnum())                # False → space included

val = "@abc123"
print(val.isalnum())                # False → symbol included

val = ""
print(val.isalnum())                # False

# Unicode alphanumeric
val = "αβ123"                       # Greek letters + digits
print(val.isalnum())                # True

val = "héllo123"                    # Accented letters + digits
print(val.isalnum())                # True

# ============================================
# ✅ isspace() – only whitespace (spaces, tabs, newlines)
# ============================================

val = "   "
print(val.isspace())                # True

val = "\t\n"
print(val.isspace())                # True

val = " a "
print(val.isspace())                # False → includes letter

val = ""
print(val.isspace())                # False

# Unicode whitespace
val = "\u2003"                      # Em space
print(val.isspace())                # True

# Mixed whitespace
val = " \t\n\r"
print(val.isspace())                # True

# ============================================
# ✅ isupper() – all cased letters are uppercase
# ============================================

val = "HELLO"
print(val.isupper())                # True

val = "HELLO123"
print(val.isupper())                # True → digits allowed

val = "HELlo"
print(val.isupper())                # False → 'lo' is lowercase

val = "12345"
print(val.isupper())                # False → no letters

# Unicode uppercase
val = "ÄÖÜ"
print(val.isupper())                # True

# Mixed case
val = "HÉllo"
print(val.isupper())                # False

# ============================================
# ✅ islower() – all cased letters are lowercase
# ============================================

val = "python"
print(val.islower())                # True

val = "python123"
print(val.islower())                # True

val = "pyThon"
print(val.islower())                # False → 'T' is uppercase

val = "123"
print(val.islower())                # False → no letters

# Unicode lowercase
val = "äöü"
print(val.islower())                # True

# Mixed case
val = "héLLO"
print(val.islower())                # False

# ============================================
# ✅ istitle() – first letter of each word is uppercase
# ============================================

val = "Hello World"
print(val.istitle())                # True

val = "Hello world"
print(val.istitle())                # False

val = "HELLO WORLD"
print(val.istitle())                # False → all caps

val = "Hello  World"                # double space still works
print(val.istitle())                # True

# Unicode title case
val = "Héllo Wörld"
print(val.istitle())                # True

# Non-standard separators
val = "Hello-World"
print(val.istitle())                # False → hyphen not considered word boundary

# Single word
val = "Hello"
print(val.istitle())                # True

# ============================================
# ✅ startswith() / endswith()
# ============================================

val = "machine learning"
print(val.startswith("mach"))       # True
print(val.startswith("Mach"))       # False → case-sensitive

print(val.endswith("learning"))     # True
print(val.endswith("Learning"))     # False

# With positions
print(val.startswith("hine", 3))    # True → 'hine' starts at index 3

# Empty string
val = ""
print(val.startswith(""))           # True
print(val.endswith(""))             # True

# Unicode prefix/suffix
val = "αβγ Python"
print(val.startswith("αβ"))         # True
print(val.endswith("Python"))       # True

# ============================================
# ✅ replace() and count()
# ============================================

val = "banana"
print(val.replace("a", "@"))        # b@n@n@
print(val.replace("a", "@", 1))     # b@nana

print(val.count("a"))               # 3
print(val.count("na"))              # 2
print(val.count("na", 3))           # 1

# Empty string
val = ""
print(val.replace("", "@"))         # @ (replaces at start and end)
print(val.count(""))                # 1 (empty string has one empty match)

# Unicode replace
val = "café café"
print(val.replace("é", "e"))        # cafe cafe

# Case sensitivity
print(val.count("Café"))            # 0 (case-sensitive)

# ============================================
# ✅ split() and join()
# ============================================

val = "apple,banana,grape"
print(val.split(","))               # ['apple', 'banana', 'grape']

val = "   apple   orange   "
print(val.split())                  # ['apple', 'orange'] → splits on whitespace

words = ["Python", "is", "fun"]
print(" ".join(words))              # Python is fun

chars = ["a", "b", "c"]
print("-".join(chars))              # a-b-c

# Split with maxsplit
val = "a,b,c,d"
print(val.split(",", 2))            # ['a', 'b', 'c,d']

# Empty string split
val = ""
print(val.split())                  # [] (empty list)
print(val.split(","))               # ['']

# Join with Unicode
chars = ["α", "β", "γ"]
print("•".join(chars))              # α•β•γ

# ============================================
# ✅ strip(), lstrip(), rstrip()
# ============================================

val = "  hello world  "
print(val.strip())                  # 'hello world'
print(val.lstrip())                 # 'hello world  '
print(val.rstrip())                 # '  hello world'

# Custom strip characters
val = "***hello***"
print(val.strip("*"))               # 'hello'
print(val.lstrip("*"))              # 'hello***'
print(val.rstrip("*"))              # '***hello'

# Unicode whitespace
val = "\u2003hello\u2003"
print(val.strip())                  # 'hello'

# Empty string
val = ""
print(val.strip())                  # ''

# ============================================
# ✅ Membership test: `in`, `not in`
# ============================================

val = "welcome to python"
print("python" in val)              # True
print("java" in val)                # False
print("welcome" not in val)         # False

# Unicode membership
val = "welcome to αβγ"
print("αβ" in val)                  # True
print("ΑΒ" in val)                  # False (case-sensitive)

# Empty string
val = ""
print("" in val)                    # True
print("a" in val)                   # False

# ============================================
# ✅ isidentifier() – valid variable name
# ============================================

val = "my_var"
print(val.isidentifier())           # True

val = "3data"
print(val.isidentifier())           # False → can't start with number

val = "for"
print(val.isidentifier())           # True → keyword, but still valid identifier

val = "data-science"
print(val.isidentifier())           # False → contains hyphen

# Unicode identifiers
val = "αβγ"
print(val.isidentifier())           # True

val = "_private"
print(val.isidentifier())           # True

# Invalid characters
val = "data@science"
print(val.isidentifier())           # False → contains @

# ============================================
# ✅ len() – length of string
# ============================================

val = "python"
print(len(val))                     # 6

val = ""
print(len(val))                     # 0

# Unicode length
val = "café"
print(len(val))                     # 4 (counts code points)

val = "😊👍"
print(len(val))                     # 2 (each emoji is one code point)



# String Slicing Examples
val = "Python Programming"

# Basic slicing: [start:stop:step]
print(val[0:6])          # 'Python' (start at 0, stop before 6)
print(val[7:])           # 'Programming' (start at 7, go to end)
print(val[:6])           # 'Python' (start at 0, stop before 6)
print(val[::2])          # 'Pto rgamn' (every second character)
print(val[::-1])         # 'gnimmargorP nohtyP' (reverse string)

# Negative indices
print(val[-11:-1])       # 'Programmin' (from 11th last to 2nd last)
print(val[-1:])          # 'g' (last character)
print(val[:-1])          # 'Python Programmin' (all except last character)

# Edge cases
print(val[5:5])          # '' (empty string, start equals stop)
print(val[10:5])         # '' (empty string, start > stop)
print(val[0:10:0])       # Raises ValueError: slice step cannot be zero

# Unicode string slicing
val = "café😊"
print(val[0:3])          # 'caf' (slices by code points)
print(val[-1:])          # '😊' (last emoji)
print(val[::-1])         # '😊éfac' (reversed Unicode string)