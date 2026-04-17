class GradeCalculator:
    @staticmethod
    def get_grade(score):
        if score >= 96: return "A+"
        if score >= 92: return "A"
        if score >= 88: return "A-"
        if score >= 82: return "B+"
        if score >= 78: return "B"
        if score >= 74: return "B-"
        if score >= 68: return "C+"
        if score >= 64: return "C"
        if score >= 60: return "C-"
        if score >= 50: return "D"
        return "Fail"

    @staticmethod
    def get_status(grade):
        if grade in ("A+", "A", "A-"): return "Excellent"
        if grade in ("B+", "B", "B-"): return "Good"
        if grade in ("C+", "C"): return "Satisfactory"
        if grade in ("C-", "D"): return "Marginal"
        return "Failure"
