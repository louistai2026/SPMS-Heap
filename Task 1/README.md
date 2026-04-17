# Task 1 – Student Performance Management System
This repository contains the Python code of the Student Performance Management System.
________________________________________
Student Performance Management System (SPMS) – User Guide
This User Guide explains how to install, run, and operate the Student Performance Management System. It is designed for instructors or users who need to manage course assessments, student records, and grade calculations efficiently.
________________________________________
1. Introduction
The SPMS is a Python based console application that allows instructors to:
•	Create a course
•	Define OCAS and OES assessment components
•	Add students and record attendance
•	Enter scores or tutorial submissions
•	Automatically calculate weighted marks, grades, and statuses
•	Generate individual reports and a full results table
The system uses object oriented programming principles and modular design across multiple Python files.
________________________________________
2. Program Structure
Your project folder should contain the following files:
main.py
menu.py
course.py
student.py
component.py
grade.py
calculator.py
Each file defines a specific class or function group:
•	main.py – Entry point of the program
•	menu.py – User interface and menu navigation
•	course.py – Course structure and student registry
•	student.py – Student data and grade calculation
•	component.py – Assessment component logic
•	grade.py – Grade and status mapping
•	calculator.py – Polymorphic score calculation wrapper
________________________________________
3. How to Run the Program
Step 1: Install Python
Ensure Python 3.8+ is installed.
Step 2: Navigate to the project folder
cd your_project_directory
Step 3: Run the program
python main.py
The main menu will appear.
________________________________________
4. Main Menu Overview
When the program starts, you will see:
===== SPMS Menu =====
1. Create course
2. Add OCAS component
3. Add OES component
4. Add student
5. Enter scores
6. View student report
7. Print results table
8. Exit
Each option is explained below.
________________________________________
5. Menu Options Explained
1. Create Course
Allows you to define:
•	Course code
•	Course title
•	Whether 80% attendance is required
Example:
Course Code: COMP8090
Course Title: Data Structures
Require 80% attendance? (yes/no): yes
________________________________________
2. Add OCAS Component
Creates a continuous assessment component.
You will be prompted for:
•	Component name
•	Weight (%)
•	Whether it is a tutorial
•	Tutorial mode (Actual or Submission)
________________________________________
3. Add OES Component
Creates an exam based component.
Prompts are similar to OCAS but without tutorial settings.
________________________________________
4. Add Student
Adds a student to the course.
Example:
Student ID: S001
Name: Alice
Attendance (%): 92
________________________________________
5. Enter Scores
Enter OCAS and OES marks for a student.
The program automatically handles:
•	Tutorial actual mode
•	Tutorial submission mode
•	Normal numeric scores
Example:
Student ID: S001
Tutorial score: 85
Assignment score: 78
Final Exam score: 90
________________________________________
6. View Student Report
Displays a detailed report for a single student, including:
•	Course information
•	Attendance
•	Overall score
•	Grade
•	Status
________________________________________
7. Print Results Table
Shows a summary of all students:
ID | Name | Overall | Grade | Status
This is useful for final grade submission.
________________________________________
8. Exit
Closes the program.
________________________________________
6. Example Workflow
1.	Create the course
2.	Add OCAS components (e.g., Tutorial 20%, Assignment 30%)
3.	Add OES components (e.g., Final Exam 50%)
4.	Add students
5.	Enter scores
6.	Print results table
7.	View individual reports
This workflow mirrors real life teaching processes.
________________________________________
7. Error Handling and Tips
•	Ensure component weights add up to 100%.
•	Student IDs must be unique.
•	Attendance below 80% automatically triggers failure if required.
•	OES and OCAS must each be ≥ 50% to pass.
________________________________________
8. Link to 5-minute introduction video
https://www.dropbox.com/scl/fi/c6uzjjzrq1vkzk2vwrkmv/20260417_104144.mp4?rlkey=qnj17t7qredrcgkvu3i3krohs&st=512yobpk&dl=0
