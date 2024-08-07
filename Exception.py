a =10
try:
    print(a/0)
except ZeroDivisionError:
    print("number can't be divsible by 0")
except FileNotFoundError:
    print("file not found")
