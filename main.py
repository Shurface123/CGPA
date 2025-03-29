# import gpa_calculator
# def main():
#     import input_handler, display_results, cummulative_gpa
    
#     all_semesters = []
#     num_semesters = int(input("Enter number of semesters: "))

#     for i in range(num_semesters):
#         print(f"Semester {i + 1}")
#         courses = input_handler.get_courses()
#         semester_gpa = gpa_calculator.calculate_gpa(courses)
        
#         if semester_gpa is None:
#             print("GPA calculation stopped due to invalid input.")
#             return
         
#         total_credits = sum(course["Credit Hours"] for course in courses)
#         all_semesters.append({"GPA": semester_gpa, "Credits": total_credits})
        
#         display_results.display_gpa(semester_gpa)
    
#     if all_semesters:
#         cgpa = cummulative_gpa.calculate_cgpa(all_semesters)
#         print(f"Your CGPA is: {cgpa}")
#     else:
#         print("No semesters to calculate CGPA.")

# if __name__ == "__main__":
#     main()


import grade_convertor
import gpa_calculator
import input_handler
import display_results
import cummulative_gpa
import predictions
import table_display

def main():
    all_semesters = []
    num_semesters = int(input("Enter number of semesters: "))

    for i in range(num_semesters):
        print(f"\nSemester {i + 1}")
        courses = input_handler.get_courses()
        semester_gpa = gpa_calculator.calculate_gpa(courses)
        
        if semester_gpa is None:
            print("GPA calculation stopped due to invalid input.")
            return
        
        total_credits = sum(course["Credit Hours"] for course in courses)
        all_semesters.append({"GPA": semester_gpa, "Credits": total_credits})

    table_display.display_table(all_semesters)
    
    cgpa = cumulative_gpa.calculate_cgpa(all_semesters)
    print("\nYour Cumulative GPA (CGPA) is:")
    display_results.display_gpa(cgpa)
    
    remaining_semesters = int(input("Enter number of remaining semesters: "))
    if remaining_semesters > 0:
        predictions.predict_final_cgpa(cgpa, remaining_semesters)
    
if __name__ == "__main__":
    main()
