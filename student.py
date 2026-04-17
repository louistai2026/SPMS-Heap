from grade import GradeCalculator

class Student:
    def __init__(self, student_id, name, attendance):
        self.student_id = student_id
        self.name = name
        self.attendance = attendance

        self.ocas_scores = {}
        self.ocas_submissions = {}
        self.oes_scores = {}
        self.oes_submissions = {}

        self.overall = 0.0
        self.grade = "Fail"
        self.status = "Failure"

    # Demonstrates abstraction
    def compute_percent(self, components, scores, submissions):
        total_weight = sum(c.weight for c in components)
        if total_weight == 0:
            return 0.0

        weighted_sum = 0.0

        for i, comp in enumerate(components):
            raw = scores.get(i, 0.0)
            subs = submissions.get(i, 0)
            val = comp.compute_score(raw, subs)
            weighted_sum += (val * comp.weight) / 100.0

        return (weighted_sum / total_weight) * 100.0

    # Demonstrates composition + polymorphism
    def calculate(self, course):
        ocas = self.compute_percent(course.ocas_components,
                                    self.ocas_scores,
                                    self.ocas_submissions)

        oes = self.compute_percent(course.oes_components,
                                   self.oes_scores,
                                   self.oes_submissions)

        attendance_ok = (not course.attendance_required) or (self.attendance >= 80)
        ocas_ok = ocas >= 50
        oes_ok = oes >= 50

        weighted = (ocas * 0.5) + (oes * 0.5)

        if not (attendance_ok and ocas_ok and oes_ok):
            self.overall = weighted
            self.grade = "Fail"
        else:
            self.overall = weighted
            self.grade = GradeCalculator.get_grade(weighted)

        self.status = GradeCalculator.get_status(self.grade)

    def report_text(self, course):
        self.calculate(course)
        return (
            f"\n===== Student Report =====\n"
            f"Course: {course.code} - {course.title}\n"
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Attendance: {self.attendance}%\n"
            f"Overall Score: {self.overall:.1f}\n"
            f"Grade: {self.grade}\n"
            f"Status: {self.status}\n"
            f"==========================\n"
        )
