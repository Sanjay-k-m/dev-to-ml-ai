val = "hello "

print(val.capitalize())
print(val.title())
print(val.upper())
print(val.lower())
print(val.swapcase())
print(val.replace("l", "L"))
print(val.count("l"))
print(val.find("l"))
print(val.find("L"))
print(val.find("ll"))  # returns the first occurrence of the substring
print(val.index("l"))  # returns the index of the first occurrence of the substring, raises ValueError if substring is not found
print(val)
