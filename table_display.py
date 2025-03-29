def display_table(semesters):
    print("\nSemester-wise GPA and Credits:\n")
    print("+-----------+--------+--------+")
    print("| Semester  |  GPA   | Credits|")
    print("+-----------+--------+--------+")
    for i, sem in enumerate(semesters, start=1):
        print(f"|    {i}      |  {sem['GPA']:.2f}  |   {sem['Credits']}   |")
    print("+-----------+--------+--------+")
