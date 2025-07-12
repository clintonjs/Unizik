"""
PSEUDOCODE: SIMPLE GRADING SYSTEM

START
    PROMPT user to enter student's score
    READ score

    IF score >= 70 AND score <= 100 THEN
        grade = "A"
    ELSE IF score >= 60 AND score <= 69 THEN
        grade = "B"
    ELSE IF score >= 50 AND score <= 59 THEN
        grade = "C"
    ELSE IF score >= 45 AND score <= 49 THEN
        grade = "D"
    ELSE IF score >= 40 AND score <= 44 THEN
        grade = "E"
    ELSE IF score < 40 THEN
        grade = "F"
    ELSE
        grade = "Invalid score"

    DISPLAY "Grade is: " + grade
END
"""

# PYTHON IMPLEMENTATION

def get_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif 0 <= score < 40:
        return "F"
    else:
        return "Invalid score"

# Main program
try:
    score = float(input("Enter the student's score (0 - 100): "))
    grade = get_grade(score)
    print("Grade is:", grade)
except ValueError:
    print("Invalid input. Please enter a number.")
