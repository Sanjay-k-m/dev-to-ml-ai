import math
# ls = []
# for i in range(1,11):
#     ls.append(i*i)

# print([i*i for i in range(10)])



# for i in range(21):
#     if i%2 ==0:

# print([i for i in range(1,21) if i%2 ==0])


# print([math.sqrt(i) for i in range(1,21)])


a = ['devin','dainty','david']
b =['python','cuber','analyst']


# tupleList = []

# for a in zip(a,b):
#     tupleList.append(a)
# print(tupleList)


# print([(i,j) for i,j in zip(a,b)])
# print([(i,j) for i in a for j in b])
# print(((i,j) for i in a for j in b))





# print([(i,'Even') if i%2==0 else(i,'Odd') for i in range(20) ])

ls = [1,0,-2,4,0,3,-5,'a']

# print([(i,'positive')if i>0 else (i,'zero') if i==0  else(i,'negative') for i in ls])

print([("Its a ALPHA")if i is alpha() else(i,'pos') if i>0 else (i,'zero') if i==0 else(i,'neg') if i<0 else() for i in ls])

