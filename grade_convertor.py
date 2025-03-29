def grade_to_point(grade):
    grade_points_dict = {
        "A": 4.0,
        "A-": 3.85,
        "B+": 3.50,
        "B": 3.00,
        "C+": 2.50,
        "C": 2.00,
        "D": 1.50,
        "E": 1.0,
        "F": 0.0,
    }
    return grade_points_dict.get(grade, None)