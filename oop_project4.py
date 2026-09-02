import csv
import os
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name,id,salary):
        self.name = name
        self.id= id
        self.salary = salary

    @abstractmethod
    def calculateSalary(self, hours):
        pass

class FullTimeEmp(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)

    def calculateSalary(self, hours = 0):
        return self.salary 

    def __str__(self):
        return f"Name: {self.name} Id: {self.id} Salary: {self.salary}"

class HalfTimeEmp(Employee):
    def __init__(self, name, id, hourly_rate):
        super().__init__(name, id, hourly_rate)
        
    def __str__(self):
        return f"Name: {self.name} Id: {self.id} Hourly rate: {self.salary}"

    def calculateSalary(self,hours):
        return self.salary * hours


class Company:
    def __init__(self):
        self.employees = []

    def addEmp(self,emp):
        self.employees.append(emp)


company = Company()
if not os.path.exists("company.csv"):
    with open ("company.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["type", "name", "id", "salary"])
else:
    with open("company.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["type"] == "FTE":
                emp = FullTimeEmp(row["name"],int(row["id"]),int(row["salary"]))
            else:    
                emp = HalfTimeEmp(row["name"],int(row["id"]),int(row["salary"]))
            company.employees.append(emp)

emp_id = 1
while True:
    print("*****************")
    choice = int(input("Choose an option: \n1. Add employee\n2. Show employees\n3. Calculate salaries\n4. Exit\n"))

    match choice:
        case 1:
            name = input("Enter name: ")
            try:
                with open("company.csv" , "r") as file:
                    reader = csv.DictReader(file)
                    for data in reader:
                        if int(data["id"]) >= emp_id:
                            emp_id = int(data["id"])+1
            except FileNotFoundError:
                    emp_id = 1

            type_of_emp = int(input("Press 1 for full time employee / 2 for part time employee: "))
            if type_of_emp == 1:
                salary = int(input("Enter salary: "))
                emp = FullTimeEmp(name,emp_id,salary)
                company.addEmp(emp)
                with open("company.csv", "a",newline="") as file: 
                    writer = csv.writer(file)
                    writer.writerow(["FTE",name,emp_id,salary])
                print("Employee added")
                print("**************")

            elif type_of_emp == 2:
                emp = HalfTimeEmp(name,emp_id,10)
                company.addEmp(emp)
                with open("company.csv", "a",newline="") as file: 
                            writer = csv.writer(file)
                            writer.writerow(["HTE",name,emp_id,10])
                print("Employee added")
                print("**************")
            else:
                print("Invalid input")

        case 2:
            print("Which employees' data do you want to view?")
            type_of_emp = int(input("Press 1 for full time employee / 2 for part time employee / 3 for both: "))
            if type_of_emp == 1:
                if not company.employees:
                    print("No employees to display")
                else:
                    for emp in company.employees:
                        if isinstance(emp,FullTimeEmp):
                            print(emp)
            elif type_of_emp == 2:
                if not company.employees:
                    print("No employees to display")
                else:
                    for emp in company.employees:
                        if isinstance(emp,HalfTimeEmp):
                            print(emp)
            elif type_of_emp == 3:
                for emp in company.employees:
                    print(emp)

            else:
                print("Invalid input")

        case 3:
            for emp in company.employees:
                hours = int(input(f"Enter hours worked by {emp.name}: "))
                print(emp.calculateSalary(hours))

        case 4:
            break

        case _:
            print("Invalid input")

                







