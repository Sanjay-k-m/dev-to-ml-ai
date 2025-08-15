"""
List all data types
"""
a = 5  # int
b = 3.14  # float
c = "hello"  # str
d = [1, 2, 3]  # list
e = (1, 2, 3)  # tuple
f = {1: "one", 2: "two"}  # dict
g = {1, 2, 3}  # set
h = True  # bool
i = None  # NoneType

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))


a = True

b = 5+a
print(b)
print(type(b))


f=5.6
print(f)
print(type(f))

a=5
print(float(a))

val ="12"
print(int(val))


print(True + True)  # 2
print(True + False)  # 1
print(False + False)  # 0
print(True * 2)  # 2
print(False * 2)  # 0
print(True / 2)  # 0.5

print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("Hello"))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True
print(bool(None))

val = "hello"
print(list(val))


val1 = {10,1,2,1,}
print(val1)  # {1, 2} - sets do not allow duplicates

val1 =list(val1)
print(val1)  # [1, 2, 10] - converted to list

val2 = (1, 2, 3)
print(list(val2))  # (1, 2, 3) - tuple remains unchanged


ls = [[1,2,],(3,4)]

print(ls)

print(dict(ls))  # TypeError: unhashable type: 'list'