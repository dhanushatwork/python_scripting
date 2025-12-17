class Student:
    def __init__(self, fname, blood_group):
        self.name = fname
        self.blood_group = blood_group

    def display(self):
        print(f"Name : {self.name}, Blood Group : {self.blood_group}")

s1 = Student("Alex", "O+")
s1.display()
s2 = Student("Max", "B+")
s2.display()
s3 = Student("Bob", "AB-")
s3.display()
