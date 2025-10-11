a= [1,2,3,['1',23]]
b = [123,23,'LLL']


#to copy a value while doin this it will store into\
#  another memory location if you do a=b then it will point to same memory address
#so to store into different memory location use copy()



# b= a.copy() 

print(a ,'||||' , b)



a.extend(b)
print(a ,'a after extending b')
print(b ,'b')



b.extend(a)

print(b)

b.append("appended me")

print(a)
print(b)



a=['ab','123','a']

print(min(a))
print(max(a))
print(min(a,key=len))
print(max(a,key=len))

a=[1,2,'python',12,3,'python',23]

print(a.index("python"))
print(a.index('python',3))
# print(a.index('python',3,5))




###########  tuple   


tuple_A = ('ab',78,4,2,3,1,2)
print(tuple_A)

tuple_B =(3,2,4,1)
print(tuple_B)


print(tuple_A + tuple_B)

print(tuple_A * 5)

print(min(('a','12','D')))
print(max(tuple_B))
print(min(('a','12','D'),key=len))
print(tuple_A.count(2),'COUNTTTT')
print(tuple_A.index(2),'indexxxxxxxxx')
print(tuple_A.index('ab'))
# print(tuple_A.index(78,5))
# print(tuple_A.index(78,1,4))  here it will findout the 78 value inside tupule between index position 0 to 3



##### UNPACKING #####
print('Tuple')
a,b,c,d =tuple_B
print(a,b,c,d)

####

val = 1,2,3,4,5,"asdfasdfasdf"
print(val)


###########
#############
###########
# set

val1 = {1,2,3,4,5,7,6,6,6,6,6,6,6,6,'python','sanjay','python'}
print(val1)

val ={1,2,3,1+5j,"devin",(1,2,'dey'),frozenset({1,2,3})}
print(val)