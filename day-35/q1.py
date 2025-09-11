# from curses.ascii import isupper

# alph = []
from curses.ascii import isalpha


sentence = input("Type a sentence .. : ")
uCase = 0
lCase = 0

data = {"LOWER_CASE":0,"UPPER_CASE":0}


for l in sentence:
    if l.isalpha():
        if(l == l.upper()):
            data["UPPER_CASE"]+=1
        else:
            data["LOWER_CASE"]+=1
# for k,v in data.items():
#     print(f'{k} = {v}')

for value in data:
    print(data)