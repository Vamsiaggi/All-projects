sleep =int(input("sleep hr:"))
meals =int(input("meals:"))
mobile=int(input("mobile:"))
study=int(input("study:"))
if(sleep==8 and meals==3 and mobile==2 and study==5):
    print("Happy")
elif(sleep<8 and meals==3 and mobile>2 and study<5):
    print("Unhappy")
elif(sleep==8 and meals==1 and mobile==7 and study==1):
    print("Unhappy")
else:
    print("unhappy")   
