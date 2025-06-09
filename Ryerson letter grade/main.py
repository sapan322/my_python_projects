def ryerson_letter_grade(pct):
    """The function loop through dictionary and return grade, based on pct."""
    grade_dict = {
        "A+" : 90, "A" : 85, "A-" : 80,
        "B+" : 77, "B" : 73, "B-" : 70,
        "C+" : 67, "C" : 63, "C-" : 60,
        "D+" : 57, "D" : 53, "D-" : 50
    }

    for grade, points in grade_dict.items():
        if pct >= points:
            return grade
    return "F"

if __name__ == '__main__':
    print(ryerson_letter_grade(89))

