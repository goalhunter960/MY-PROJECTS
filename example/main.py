

flag=True

while flag==True:
    weight = float(input("w:- "))
    height = float(input("h:- "))

    bmi = (weight) / (height**2)
    print(bmi)
    if bmi < 18.5:
        print("you are underweight")
    elif (bmi >= 18.5 and bmi < 25):

        print("You are normal")
    elif bmi < 30:
        print("you are overwight")
    else:
        print("YOU ARE OBESES NIGAAAAAAA")



    
