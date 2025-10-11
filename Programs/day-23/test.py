# testing the f-string formatting
a = 10
b = 10
c = 20
d = 10

# printing the values in decimal
print(f'{a=}, {b=}, {c=}, {d=}')

# printing the values in hexadecimal
print(f'{a=:#x}, {b=:#x}, {c=:#x}, {d=:#x}')

# changing the value of d
d = 11

# printing the values in decimal
print(f'{a=}, {b=}, {c=}, {d=}')

# printing the values in hexadecimal
print(f'{a=:#x}, {b=:#x}, {c=:#x}, {d=:#x}')
