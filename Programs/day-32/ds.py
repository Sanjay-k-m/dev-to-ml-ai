ds = {1:'sanjay','val':25,2:[2,3,4],3:[1,2,3,4],4:'david'}
print(ds)
ds[3] = {1,2,3,4,5,}
print(ds)

ds ={}
print(type(ds))
ds.setdefault("dev",25)
print(ds)

ds = {1:2,2:3,3:4}
ds.update([(1,2),(3,4),['a',23]])
print(ds)

ds = {1:2,2:3,3:4}

ds.update(a=12,b=13,c=14)
print(ds)

ds = {1:2,2:3,3:4}
ds.pop(3)
print(ds)
print(ds.pop(2))
ds = {1:2,2:3,3:4}
print(ds.popitem())
ds.clear()
print(ds)

ds = {1:2,2:3,3:4}
del ds[2]
print(ds)


ds = {1:2,2:3,3:4}
print(ds,id(ds))
new = ds.copy()
print(new,id(new))


ds={1:'dainty',2:'devid',3:'davidd'}
print(ds.keys())
print(ds.keys())
print(ds.items())
print(list(ds.items()))

ds={}
ds[1] = 'python'
print(ds)