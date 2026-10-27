name=input("Enter student name:")
mark1=float(input("Enter marks in Subject 1:"))
mark2=float(input("Enter marks in Subject 2:"))
mark3=float(input("Enter marks in Subject 3:"))
total=mark1 + mark2 + mark3 average=total/3
print("\n---Student Result---")
print("Student Name:",name)
print("Total Marks:",total)
print("Average Marks:",round(average,2))
