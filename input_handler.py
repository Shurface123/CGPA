def get_courses():
    courses = []
    while True:
        course_name = input("Enter course name, enter 'q' to quit: ")
        if course_name.lower() == 'q':
            break
        
        grade = input("Enter grade (A, A-, B+, B, C+, C, D, E, F): ").strip().upper()
        if grade not in ["A", "A-", "B+", "B", "C+", "C", "D", "E", "F"]:
            print("Invalid grade, please enter a valid grade.")
            continue
        try:
            credit_hours = int(input("Enter credit hours: "))  
            courses.append({"Course Name": course_name, "Grade": grade, "Credit Hours": credit_hours})
        except ValueError:
            print("Invalid input, credit hours must be a number.")
    
    return courses
