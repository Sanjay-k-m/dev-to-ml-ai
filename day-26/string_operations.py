print("sanjay km")

fname = "sanjay"
lname = "km"
num = 23

print("hello {}".format(fname))
print("hello {1} {0}".format(fname,lname))
print("Hello {} {}welcome to python programming".format(fname,lname))  # string formatting

print("{a} {c} {f}".format(a="hey",c=fname,f=lname))

print(f"hello {fname} {lname}")


# traditional way
print("hello %s %s %i welcome to python programming" %(fname,lname,num))

# print()