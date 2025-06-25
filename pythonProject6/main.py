x=int(input("Your start number:- "))
z=input("Should we add or subtract- ")
y=int(input("How many should we add or substract- "))
a=int(input("How far should we go- "))


if z== '+':
    for i in range(x, a,+y):
        print(i, end=', ')

elif z== '-':
    for i in range(x, a,+y):
        print(i, end=', ')



