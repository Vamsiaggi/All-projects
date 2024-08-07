number=int(input("enter number"))
for i in range(number):
    for j in range(number):
        if (i==0 or j==0 or j==number-1 or i==number-1):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()            