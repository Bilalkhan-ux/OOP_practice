import csv
import os
class Student:
    def __init__(self,id,name,age,marks):
        self.id = id
        self.name = name
        self.age= age
        self.marks = marks

    def __str__(self):
        return f"Id: {self.id} Name: {self.name} Age: {self.age} Marks: {self.marks}"


class School:
    def __init__(self):
        self.students = []

    def addStudent(self,obj):
        self.students.append(obj)

    def showStudents(self):
        for student in self.students:
            print(student)

    def findStudent(self,id):
        for student in self.students:
            if student.id == id:
                print("Student found\nName: ",student.name, "Age: ", student.age, "Marks: ",student.marks)
                break
        else:
            print("Student not found")

    def updateMarks(self,id, marks):
        for student in self.students:
            if student.id == id:
                student.marks = marks
                break
        else:
            print("Student not found")

    def delStudent(self,id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                break
        else:
            print("Student not found")

    def updateFile(self):
        with open("school.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id","name","age","marks"])

            for row in self.students:
                writer.writerow([row.id, row.name,row.age,row.marks])


school = School()
if not os.path.exists("school.csv"):
    with open("school.csv", "w",newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["id","name","age","marks"])

else: 
    with open("school.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = Student(int(row["id"]) , row["name"], int(row["age"]), float(row["marks"]))
            school.addStudent(student)

student_id = 1
while True:
    print("*************")
    choice = int(input("Choose an option: \n1. Add student\n2. Show all students\n3. Find student\n4. Update marks\n5. Delete student\n6. Exit\n"))
    match choice:
        case 1 :
            name = input("Enter name: ")
            if school.students:
                student_id = max(student.id for student in school.students)+1
            else:
                student_id = 1

            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))
            student = Student(student_id,name,age,marks)
            school.addStudent(student)
            print("Student added")
            print("Student id is ",student_id)
            school.updateFile()
            student_id+=1
            
        
        case 2:
            school.showStudents()

        case 3:
            search_id = int(input("Enter student id: "))
            school.findStudent(search_id)

        case 4:
            search_id = int(input("Enter student id: "))
            marks = float(input("Enter marks: "))
            school.updateMarks(search_id, marks)
            school.updateFile()


        case 5:
            search_id = int(input("Enter student id: "))
            school.delStudent(search_id)
            school.updateFile()


        case 6:
            school.updateFile()
            break

        case _:
            print("Invalid input")






        
        