cource = "Computer"
theory = 54 
practical =25

if('science' == cource.lower()):
    if(theory > 60):
        print("please check the input score for science theory")
    elif(practical > 60):
        print("please check the input score for science practical")
    else:
        print('score validated for science your total is ',theory + practical)
elif('computer' == cource.lower()):
    if(theory > 60):
        print("please check the input score for computer theory")
    elif(practical > 60):
        print("please check the input score for computer practical")
    else:
        print('score validated for computer your total is ',theory + practical)
else: print("Cource not recoganized. please enter score for either computer or English")