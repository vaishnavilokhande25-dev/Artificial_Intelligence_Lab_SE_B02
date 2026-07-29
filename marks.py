subA = int(input("Enter marks of DS : "))
subB = int(input("Enter marks of AI: "))
subC = int(input("Enter marks of DELD: "))
subD = int(input("Enter marks of UHV: "))
subE = int(input("Enter marks of OS: "))

total = subA + subB + subC + subD + subE
percentage = total / 5

print("\n Total Marks =", total)
print("Percentage =", percentage, "%")

if percentage >= 75:
    print("Result: Distinction")
elif percentage >= 60:
    print("Result: First Class")
elif percentage >= 50:
    print("Result: Second Class")
elif percentage >= 35:
    print("Result: Third Class")
else:
    print("Result: Fail")


