class parent:
    age=int()
    def __init__(self):
        self.parent_name=input("enter name")
        self.parent_income=input("enter income")
obj1=parent()
obj2=parent()
obj1.age=33
print(obj1,obj1.age,obj1.parent_name) 
print(obj2,obj2.age,obj2.parent_name) 
