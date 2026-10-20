
GRADE_CATEGORIES = ("Distinction", "Credit", "Pass", "Fail")

def validate_score(score):
    """Validates that a score is between 0 and 100."""
    if 0 <= score <= 100:
        return score
    raise ValueError("Score must be between 0 and 100.")

def calculate_average(scores):
    """Returns the average score from a list of scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def classify_grade(score):
    """Classifies a student's score into a grade category using conditionals."""

    if score >= 85:
        return GRADE_CATEGORIES[0]
    elif score >= 70:
        return GRADE_CATEGORIES[1]
    elif score >= 50:
        return GRADE_CATEGORIES[2]
    else:
        return GRADE_CATEGORIES[3]

def count_passed(students):
    """Returns the number of passing students (score >= 50)."""
    count = 0
    for student in students:
        if student["score"] >= 50:
            count += 1
    return count

def main():

    students = [
        {"name": "Alice", "age": 20, "study_hours": 15, "score": 92},
        {"name": "Bob", "age": 22, "study_hours": 10, "score": 78},
        {"name": "Charlie", "age": 21, "study_hours": 4, "score": 42},
        {"name": "Diana", "age": 23, "study_hours": 14, "score": 88},
        {"name": "Ethan", "age": 19, "study_hours": 8, "score": 65}
    ]


    for student in students:
        try:
            validate_score(student["score"])
        except ValueError as e:
            print(f"Error for {student['name']}: {e}")
            return


    scores = [student["score"] for student in students]
    avg_score = calculate_average(scores)
    passed_count = count_passed(students)


    print("=" * 60)
    print(f"{'STUDENT PERFORMANCE REPORT':^60}")
    print("=" * 60)
    print(f"{'Name':<18} | {'Age':<4} | {'Hours':<6} | {'Score':<6} | {'Grade':<12}")
    print("-" * 60)


    for student in students:
        grade = classify_grade(student["score"])
        print(f"{student['name']:<18} | {student['age']:<4} | {student['study_hours']:<6} | {student['score']:<6} | {grade:<12}")

    print("-" * 60)
    print(f"Total Students Evaluated : {len(students)}")
    print(f"Students Passed          : {passed_count}")
    print(f"Class Average Score      : {avg_score:.2f}")
    print("=" * 60)

if __name__ == "__main__":
    main()