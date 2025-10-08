import pytest
import csv
import os
from tabulate import tabulate
from project import add_student, view_students, average_score_calculate, show_average_score, ranking_students, delete_student


def new_file_tested(student_data):
    with open("test_students.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name","literature", "math", "english"])
        writer.writeheader()
        writer.writerow(student_data)

def test_view_students_file_not_found():
    filename = "non_existent_file.csv"
    assert view_students(filename) == "File does not exist"

def test_average_score_calculate_file_not_found():
    filename = "non_existent_file.csv"
    assert average_score_calculate(filename, "Phong") == None

def test_show_average_score_file_not_found():
    filename = "non_existent_file.csv"
    assert show_average_score(filename, "Phong") == "Student not found or file does not existed"



def test_view_students():
    new_file_tested({"name": "Mike", "literature": "5", "math": "7", "english": "7"})
    show_student = tabulate([{"name": "Mike", "literature": "5", "math": "7", "english": "7"}], headers = "keys", tablefmt = "grid")
    assert view_students("test_students.csv") == show_student
    if os.path.exists("test_students.csv"):
        os.remove("test_students.csv")


    

def test_average_score_calculate():
    new_file_tested({"name": "Mike", "literature": "5", "math": "7", "english": "7"})
    assert round(average_score_calculate("test_students.csv", "Mike"), 2) == 6.33
    if os.path.exists("test_students.csv"):
        os.remove("test_students.csv")


def test_show_average_score():
        new_file_tested({"name": "Mike", "literature": "5", "math": "7", "english": "7"})
        assert show_average_score("test_students.csv", "Mike") == "Mike average score is 6.33"
        if os.path.exists("test_students.csv"):
            os.remove("test_students.csv")

def test_ranking_student():
    new_file_tested({"name": "Mike", "literature": "5", "math": "7", "english": "7"})
    
    average = average_score_calculate("test_students.csv", "Mike")
    test_sorted_students = [{"name": "Mike", "average score": round(average, 2)}]

    show_ranking_students = tabulate(sorted(test_sorted_students, key=lambda s: s["average score"]), headers="keys", tablefmt="grid")
    
    assert ranking_students("test_students.csv") == show_ranking_students
    if os.path.exists("test_students.csv"):
        os.remove("test_students.csv")




    
