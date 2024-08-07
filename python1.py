Monthly_income=int(input("enter monthly :"))
Attendance_percentage=int(input("enter the student percentage"))
if(Attendance_percentage>=75 and Monthly_income<30000):
    print("Eligible")
elif(not Attendance_percentage<=80 ):
    print("Eligible")
else:
    
    print("Not Eligible")        