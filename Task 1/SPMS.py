class Student:
    def __init__(self, student_id, name, attendance):
        self.student_id = student_id
        self.name = name
        self.attendance = attendance


class Course:
    def __init__(self, code, title, attendance_required):
        self.code = code
        self.title = title
        self.attendance_required = attendance_required

