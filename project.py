import csv
import os
import re
from tabulate import tabulate



def get_name():
    while True:
        name = input("Student's name: ").strip()
        if re.match(r"^[a-z]", name, re.IGNORECASE):
            return name
        else:
            print("Invalid name")

def get_grade(subject):
    while True:
        try:
            grade = float(input(f"{subject} points: "))
            if 0 <= grade <= 10:
                return grade
            else: raise ValueError(f"Invalid {subject} points")

        except ValueError:
            print(f"Invalid {subject} points")

def add_student(filename):
    name = get_name()
    literature_grade = get_grade("Literature")
    math_grade = get_grade("Math")
    english_grade = get_grade("English")
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if name == line["name"]:
                    print("")
                    print("Student existed")
                    return
    else: 
        print("File does not exist. Creating a new file")


    with open(filename, "a") as file:
         writer = csv.DictWriter(file, fieldnames=["name", "literature", "math", "english"])
         if os.path.getsize(filename) == 0:
            writer.writeheader()
         writer.writerow({"name": name, "literature": literature_grade, "math": math_grade, "english": english_grade})
def view_students(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = list(csv.DictReader(file))
            # for line in reader:
            #     print(f"Student's name: {line['name']}, literature points: {line["literature"]}, math points: {line['math']}, english points: {line["english"]}")
            print("")
            show_student = tabulate(reader, headers = "keys", tablefmt = "grid")
            return show_student
    else:
        print("File does not exist")

def average_score_calculate(filename, name):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            student_found = False
            for line in reader:
                if name == line["name"]:
                    literature = float(line["literature"])
                    math = float(line["math"])
                    english = float(line["english"])
                    average = (literature + math + english) / 3
                    student_found = True
                    return average
        
            if not student_found:
                print("")
                print("Student not found")
                return
                    
    
    else:
        print("File does not existed")
        return


   
def show_average_score(filename, name):

    average = average_score_calculate(filename, name)
    if average is not None:
        print("")
        return f"{name} average score is {average:.2f}"

def ranking_students(filename):
    if os.path.exists(filename):
        sorted_student = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            
            for line in reader:
                average = average_score_calculate(filename, line["name"])
                sorted_student.append({"name": line["name"], "average score": round(average, 2)})
            # for student in sorted(sorted_student, key = lambda student : student["score"]):
            #     print(f"{student["name"]}, score: {student["score"]}")
            sorted_student = sorted(sorted_student, key = lambda student : student["average score"], reverse=True)
            print(tabulate(sorted_student, headers = "keys", tablefmt = "grid"))
               


 
def delete_student(filename, name):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            students = []
            reader = csv.DictReader(file)
            for row in reader:
                if name != row["name"]:
                    students.append(row)
                     
                    
        with open(filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "literature", "math", "english"])
            writer.writeheader()
            writer.writerows(students)

           
    else:
        print("File does not exist")

def main():
    # filename = "students.csv"
    file_path = "students.csv"
    while True:
        print("\n============Menu============")
        print("1. Add student")
        print("2. View students")
        print("3. Calculate average student score")
        print("4. Ranking")
        print("5. Delete student")
        print("6. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_student(file_path)
        elif choice == "2":
            print(view_students(file_path))
        elif choice == "3":
            name = input("Enter student's name: ").strip()
            average_score_calculate(file_path, name)
            print(show_average_score(file_path, name))
        elif choice =="4":
            ranking_students(file_path)
        elif choice == "5":
            name = input("Enter student's name: ").strip()
            delete_student(file_path, name)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
