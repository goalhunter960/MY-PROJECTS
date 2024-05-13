x=int(input("Enter start number:- "))
y=input("Enter operation for pattern (+,*,/,-) :- ")
z=int(input("Enter number pattern:- "))
a=int(input("How long should it run for:- "))

table=[]
table.append(x)
value=True

indicator=0

if y=='+':
    while (value== True):

        if indicator== a:
            value= False
        else:
            table.append(table[indicator] + z)
            indicator += 1
elif y=='-':
    while (value== True):

        if indicator== a:
            value= False
        else:
            table.append(table[indicator] - z)
            indicator += 1
elif y=='*':
    while (value== True):

        if indicator== a:
            value= False
        else:
            table.append(table[indicator] * z)
            indicator += 1
elif y=='/':
    while (value== True):

        if indicator== a:
            value= False
        else:
            table.append(table[indicator] / z)
            indicator += 1





print(table)





