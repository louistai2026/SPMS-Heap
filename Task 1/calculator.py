class ScoreCalculator:
    def calculate(self, student, course):
        # Polymorphic call to Student.calculate()
        student.calculate(course)
        return student.overall
