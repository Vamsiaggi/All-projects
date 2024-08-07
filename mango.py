row=int(input("enter the rows :"))
cols=int(input("enter the cols :"))
number=int(input("enter the number"))
if(number <cols or number % rows==0 or number % cols==0):
    print("mango tree")
else:
    print("pichi tree")    
