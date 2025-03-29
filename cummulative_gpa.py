import grade_convertor
import gpa_calculator

def calculate_cgpa(semesters):
    total_weighted_gpa = 0
    total_credits = 0

    for semester in semesters:
        semester_gpa = semester["GPA"]
        semester_credits = semester["Credits"]
        
        if semester_gpa is None:
            continue 
        
        total_weighted_gpa += semester_gpa * semester_credits
        total_credits += semester_credits
    
    return total_weighted_gpa / total_credits if total_credits > 0 else None