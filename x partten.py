number=int(input("enter number"))
for i in range(number):
    for j in range (number):
        if((i==j) or (j==(number-1)-i)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            