class AssessmentComponent:
    def __init__(self, name, weight, is_tutorial=False,
                 actual_mode=False, total_exercises=0,
                 min_full=0):
        self.name = name
        self.weight = weight
        self.is_tutorial = is_tutorial
        self.actual_mode = actual_mode
        self.total_exercises = total_exercises
        self.min_full = min_full

    # Demonstrates encapsulation
    def compute_score(self, raw_score, submissions):
        if not self.is_tutorial:
            return raw_score

        if self.actual_mode:
            return raw_score

        if self.min_full > 0:
            return min(100.0, (submissions * 100.0) / self.min_full)

        return 0.0
