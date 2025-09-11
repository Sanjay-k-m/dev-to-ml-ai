#write a program to count the the total digits in a number 
num = int(input("Enter a number : "))
count = 0
while num!=0:
    num //= 10
    count +=1

print(f'string length {count}')

