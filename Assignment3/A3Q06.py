marks = float(input("Enter the student's marks: "))
if 90 <= marks <= 100:
    print("The student's grade is: A")
elif 70 <= marks <= 89:
    print("The student's grade is: B")
elif 50 <= marks <= 69:
    print("The student's grade is: C")
elif 40 <= marks <= 49:
    print("The student's grade is: D")
elif 0 <= marks <= 39:
    print("The student's grade is: F")
else:
    print("Please enter a valid mark")


