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


def test_view_students():
    new_file_tested({"name": "Mike", "literature": "5", "math": "7", "english": "7"})
    show_student = tabulate({"name": "Mike", "literature": "5", "math": "7", "english": "7"}, headers = "keys", tablefmt = "grid")
    assert view_students("test_students.csv") == show_student

    

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



    
