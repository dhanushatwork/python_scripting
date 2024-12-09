#Percentage calculator
sub1 = int(input("Enter total marks obtained in English "))
sub2 = int(input("Enter total marks obtained in Language II "))
sub3 = int(input("Enter total marks obtained in Science "))
sub4 = int(input("Enter total marks obtained in Maths "))
sub5 = int(input("Enter total marks obtained in Social "))

total = (sub1+sub2+sub3+sub4+sub5)

print("Total marks obtained = ", total,"/500", "percentage = ", total/5)

#Area of Circle
radius = int(input("Enter radius of a circle "))
area = 3.141*(radius * radius)
print(area)
cirm = 2 * 3.141 * radius
print(cirm)
