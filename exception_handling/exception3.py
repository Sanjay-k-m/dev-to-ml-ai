# try:
#     val = int(input('Enter The Number: '))
# except:
#     print('Invalid Input')
# else:
#     print(f'entered :- {val}')


def fn():
    try:
        val = int(input('Enter The Number: '))
    except:
        print('Invalid Input')
        fn()
    else:
        print(f'entered :- {val}')
fn()