mark = int(input("Enter mark: "))

if mark<0 or mark>100:
    print("Invalid mark")
if mark>=85:
    print("Distinction")
elif mark>=50:
    print("Pass")
else:   
    print("Fail")