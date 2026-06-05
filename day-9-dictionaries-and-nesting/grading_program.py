student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for i in student_scores:
    if student_scores[i] < 101 and student_scores[i] > 90: s = "Outstanding"
    elif student_scores[i] < 91 and student_scores[i] > 80: s = "Exceeds Expectations"
    elif student_scores[i] < 81 and student_scores[i] > 70: s = "Acceptable"
    else: s = "Fail"
    student_grades[i] = s
print(student_grades)