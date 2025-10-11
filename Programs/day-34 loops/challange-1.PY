# with the given list [12,24,35,24,88,120,155,88,120,155]
# write a program to print this list after removing all 
# duplicate value with original value deserved.



og_val = [12,24,35,24,88,120,155,88,120,155]

e_array = []

for v in og_val:
    if v not in e_array:
        e_array.append(v)
print(e_array)