n=int(input("enter n value"))
n=n*2
modified_n=n+1
for i in range(int(modified_n/2)):
    for j in range ((modified_n*2)):
        if((j>=int(modified_n/2)-i and j<=int(modified_n/2)+i)):
            print("*",end=" ")
        else:
            print(" ",end=" ")   
    print()   
             