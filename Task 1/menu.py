from course import Course
from student import Student
from component import AssessmentComponent

def read_int(prompt):
    return int(input(prompt))

def read_float(prompt):
    return float(input(prompt))

class Menu:
    def __init__(self):
        self.course = None

    def create_course(self):
        code = input("Course Code: ")
        title = input("Course Title: ")
        att = input("Require 80% attendance? (yes/no): ").lower() == "yes"
        self.course = Course(code, title, att)

    def add_component(self, is_ocas):
        name = input("Component name: ")
        weight = read_float("Weight (%): ")
        is_tutorial = input("Tutorial? (yes/no): ").lower() == "yes"

        comp = AssessmentComponent(name, weight, is_tutorial)

        if is_tutorial:
            mode = input("Mode (Actual/Submission): ").lower()
            if mode == "actual":
                comp.actual_mode = True
            else:
                comp.total_exercises = read_int("Total exercises: ")
                comp.min_full = read_int("Min submissions for full mark: ")

        if is_ocas:
            self.course.ocas_components.append(comp)
        else:
            self.course.oes_components.append(comp)

    def add_student(self):
        sid = input("Student ID: ")
        name = input("Name: ")
        att = read_float("Attendance (%): ")
        self.course.add_student(Student(sid, name, att))

    def enter_scores(self):
        sid = input("Student ID: ")
        if sid not in self.course.students:
            print("Not found.")
            return

        s = self.course.students[sid]

        print("OCAS:")
        for i, comp in enumerate(self.course.ocas_components):
            if comp.is_tutorial and not comp.actual_mode:
                s.ocas_submissions[i] = read_int(f"{comp.name} submissions: ")
            else:
                s.ocas_scores[i] = read_float(f"{comp.name} score: ")

        print("OES:")
        for i, comp in enumerate(self.course.oes_components):
            if comp.is_tutorial and not comp.actual_mode:
                s.oes_submissions[i] = read_int(f"{comp.name} submissions: ")
            else:
                s.oes_scores[i] = read_float(f"{comp.name} score: ")

    def print_results(self):
        for s in self.course.students.values():
            s.calculate(self.course)
            print(f"{s.student_id} | {s.name} | {s.overall:.1f} | {s.grade} | {s.status}")

    def run(self):
        while True:
            print("\n===== SPMS Menu =====")
            print("1. Create course")
            print("2. Add OCAS component")
            print("3. Add OES component")
            print("4. Add student")
            print("5. Enter scores")
            print("6. View student report")
            print("7. Print results table")
            print("8. Exit")

            choice = input("Choice: ")

            if choice == "1":
                self.create_course()
            elif choice == "2":
                self.add_component(True)
            elif choice == "3":
                self.add_component(False)
            elif choice == "4":
                self.add_student()
            elif choice == "5":
                self.enter_scores()
            elif choice == "6":
                sid = input("Student ID: ")
                if sid in self.course.students:
                    print(self.course.students[sid].report_text(self.course))
            elif choice == "7":
                self.print_results()
            elif choice == "8":
                break
