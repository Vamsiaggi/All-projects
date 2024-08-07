odd=[]
even=[]
my_list=list(map(int ,input("enter numbers :").split(",")))
for i in my_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list :" ,even)
print("odd list :" ,odd)