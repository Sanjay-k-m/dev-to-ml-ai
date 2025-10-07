class NegativeNumbrError(Exception):
    pass

try:
    a  = int(input("Enter First Number : "))
    b  = int(input("Enter Second Number : "))

    if(a>0 and b>0):
        val = a/b
        print(val)
    else:
        raise NegativeNumbrError("Negative number is not acceptable")
except NegativeNumbrError as NNE:
    print(NNE)