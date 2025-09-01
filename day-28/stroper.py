val ="my name is sanjay km"

print(val.index('na'))
# print(val.index('na', 5))  # Start searching from index 5
# print(val.index('na', 5, 15))  # Search between index 5 and 15

print(val.find('na'))
print(val.find('na', 5))  # Start searching from index 5
print(val.find('na',5,15))

val ="abc"
print (val.isalpha())
val = "1232"
print(val.isdigit())
val = "asdfasdf"
print(val.isalnum())
val = "12345.234"
print(val.isnumeric())
val = "23324"
print(val.isdecimal())

val = "sanjay km  asap"
print(val.replace("s","a"))
print(val.replace("s","a",1))  # Replace only the first occurrence

print(val.count("a",4))
print(val.count("sa",5))