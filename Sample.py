#HUMAN RESOURCE MANAGEMENT SYSTEM PROJECT FOR SOFTWARE ENGINEERING
#DEVELOPED BY :-
#1. AMAL KRISHNA M [21162171001]
#2. ATHARVA DESHPANDE [21162171003]

class Employee:
    def __init__(self,name,age,gender,designation,salary):
        self.name=name
        self.age=age
        self.gender=gender
        self.designation=designation
        self.salary=salary

    def display(self):
        print("Employee Name : ",self.name)
        print("Employee Age : ",self.age)
        print("Employee Gender :",self.gender)
        print("Employee Designation : ",self.designation)
        print("Employee Salary : ",self.salary)

class HRMS:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def remove_employee(self, employee):
        self.employees.remove(employee)
    def display_all_employees(self):
        for employee in self.employees:
            employee.display()
            print("")
    def search_employee(search, name):
        for employee in self.employees:
            if employee.name.lower()==name.lower():
                employee.display()
                return
        print("Employee not found!!!")

hrms = HRMS()
emp1 = Employee("Smith",25,"Male","Intern",30000)
emp2 = Employee("Jane",27,"Female","Manager",50000)
hrms.add_employee(emp1)
hrms.add_employee(emp2)
hrms.display_all_employees()
hrms.search_employee("Jane")
