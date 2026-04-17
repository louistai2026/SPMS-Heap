class Course:
    def __init__(self, code, title, attendance_required):
        self.code = code
        self.title = title
        self.attendance_required = attendance_required

        self.ocas_components = []
        self.oes_components = []
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def has_valid_weights(self):
        total = sum(c.weight for c in self.ocas_components) + \
                sum(c.weight for c in self.oes_components)
        return round(total) == 100
