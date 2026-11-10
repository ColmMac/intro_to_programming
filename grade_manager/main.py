import os
from grade_manager import calculate_student_stats, validate_grade, InvalidGradeError


def read_student_records(filepath):
    with open("student_scores.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            splitted_line = line.split()
            student_name = splitted_line[0]
            raw_scores
