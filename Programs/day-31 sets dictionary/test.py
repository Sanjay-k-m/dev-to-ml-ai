from re import L


ds= {1:"sanjay",2:"dey"}

print(ds)

print(ds[1])
# print(ds[12])

print(ds.get(2))

print(ds.get(12))
print(ds.get(12,"Data Not Found"))


# convert a list to dictionary

ls = [[1,2],('a',2)]
# print(dict(ls))


ls1 =['sanjay','danial','rex',]
ls2 =['python','cyber','analyst']
new =tuple(zip(ls1,ls2))
print(new)

ls = {1:{1:[20,30,40],2:{},2:{'a':[10,120]}}}
print(ls[1][1][2])