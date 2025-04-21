x=int(input("enter your science marks:"))
y=int(input("enter your maths marks:"))
z=int(input("enter your english marks:"))
total=x+y+z
avg=total/3
if avg>=90 and avg<=100:
    print("You have secured A1")
elif avg>=80 and avg<=89:
    print("You have secured A2")
elif avg>=70 and avg<=79:
    print("You have secured B1")
elif avg>=60 and avg<=69:
    print("You have secured B2")
else:
    print("You have secured C")