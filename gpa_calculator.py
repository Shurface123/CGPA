import grade_convertor
def calculate_gpa(courses):
    total_grade_times_credits = 0
    total_credits = 0

    for course in courses:
        grade = course["Grade"]
        credit_hours = course["Credit Hours"]
        
        grade_points = grade_convertor.grade_to_point(grade)  
        if grade_points is None:  
            print(f"Error: Invalid grade '{grade}' in course.")
            return None
        
        total_grade_times_credits += grade_points * credit_hours  
        total_credits += credit_hours

    return total_grade_times_credits / total_credits if total_credits > 0 else None
