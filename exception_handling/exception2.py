try:
    a = int(input('first num'))
    b = int(input('sec num'))
    val = a/b
    print(val)
    print([1,2,3,4][3])
    print(un)
except ZeroDivisionError as s :
    print(s)
    print("cant divisible by zero")
except IndexError:
    print('invalid index')
except NameError:
    print('invalid varible')
except:
    print('completed')
print('Done') 
