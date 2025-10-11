# # integer reverse


# num = 12312
# result = num % 10
# num //= 10
# print(result)
# print(num)

num = int(input("Enter a number"))
rev = 0
while num != 0:
    digit = num % 10
    rev = (rev*10) + digit
    num //=10
print(rev)

