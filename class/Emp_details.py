class Emp_details:
    def __init__(self, name, domain, salary):
        self.name = name
        self.domain = domain
        self.salary =  salary

    def emp_info(self):
        print("Name = ",self.name, "\nDomain =",self.domain, "\nSalary =",self.salary) 
#object creation
emp1 = Emp_details("Adam", "Python-Developer", 85000)
emp1.emp_info()

emp2 = Emp_details("Mike", "Python-Developer", 105000)
emp2.emp_info()

emp3 = Emp_details("Jack", "Ai-Developer", 95000)
emp3.emp_info()

emp4 = Emp_details("Sky", "DevOps", 90000)
emp4.emp_info()

