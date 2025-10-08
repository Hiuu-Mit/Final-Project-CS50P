# STUDENT MANAGEMENT TOOL
    #### Video Demo:  https://youtu.be/eoWWPqvWOiM
    #### Description:
        -This is my final project for CS50P course
        -This is a python project use for manage student information and their grade
    This project allow user to:
        - Add student
        - View student
        - Calculate average score of a student
        - Ranking student based on average score
        - Delete student
    Features:
        - Add student:
            - Allow user adding a new student and stored it in a csv file call students.csv, if the file is not exist, it will automatically created a new file students.csv.
           In this file, the are four columns represents their name, literature grade, math grade and enlgish grade. It validate input date to ensure that name are correclty formated
           and grades are numeric values between 0-10. I use regular expression for name and simple if else statement to handle grades input. It will prompt the user again if name is already exist to prevent
           duplicate student.
        - View student:
            - Display all the student in the csv file with module tabulate. If the csv file does not exist any student the program will print a message notify user that there is no student info
            or if the file doesnt not exist yet it will print that the file does not exist.
        - Calculate average score of a student:
            - I split this part into two function, one return the average score the other display the average score to the user. If there is no file exist yet, it will print a message that the
            file does not exist and also notify to user when the user input a student that does not exist in the csv file.
        - Ranking student based on average score:
            - Display all the student with module tabulate but this time it will sort all student by their average score from high to low
        - Delete student:
            - Remove a student from the csv file by their name. If the student does not exist, it will notify the user.

         



