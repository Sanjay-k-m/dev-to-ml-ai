# find out put of number 124 : 1+2+4 =7

num = 124
sum = 0
while(num != 0 ):
    sum += num%10
    num //= 10
print(sum)