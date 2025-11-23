print(" welocome to rajs class enrollment system")
name=input("enter the students name:")
age=int(input("enter the students age:"))
print("\nProcessing information\n")
if age>=10:
    if age<=20:
        print("enrollment status for:",name)
        print("Age:",age)
        print("congratulations! you are allowed to enroll")
    else:
        print("enrollment status for:",name)
        print("age:",age)
        print(" you cannot enroll because your age is above the limit")
else:
    print("enrollment status for :",name)
    print("age:",age)
    print(" you cannot enroll because you are younger than 10")
print("\nThankyou for using the enrollment system!!!")        