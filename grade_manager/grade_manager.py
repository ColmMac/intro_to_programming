class InvalidGradeError(Exception):
    def __init__(self, grade, message="Grade must be between 0 and 100"):
        self.grade = grade
        self.message = f"Recieved {grade}"
        super().__init__(self.message)


def validate_grade(score):
    if score >= 0 and score <= 100: 
        pass
    else:
        raise InvalidGradeError(score)

def calculate_student_stats(scores):
    if scores == None:
        return 0
    average = sum(scores) / len(scores)

    maximum = max(scores)
    minimum = min(scores)
    return (average, maximum, minimum)