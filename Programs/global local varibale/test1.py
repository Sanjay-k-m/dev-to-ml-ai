val = "im global"

def callme():

    val="im local"
    print(val)

callme()
print(val)




l = "im global"

def callme():
    global val
    val="im local" # it overwrite global variable from this local data 
    print(val)

callme()
print(val)

