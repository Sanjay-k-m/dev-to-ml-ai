# val = 10/0
# print(val) #division by zero

# print(a)  

# try:
#     pass
# except:
#     pass
# finally:
#     print('done')


# try:
#     a = int(input("Enter a number"))
#     b = int(input("Enter another number"))

#     val = a/b
#     print(val)
# except: 
#     print('hello')
# finally: 
#     print('done')

def test():
    try:
        a = int(input("Enter a number"))
        b = int(input("Enter another number"))

        val = a/b
        print(val)
    except: 
        print('please enter the firsst and second number')
        test()
    finally: 
        print('done')
test()