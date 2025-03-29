def predict_final_cgpa(current_cgpa, remaining_semesters):
    print("\nBased on your current performance, here are some CGPA predictions:")
    for target_gpa in [4.0, 3.5, 3.0, 2.5]:
        predicted_cgpa = (current_cgpa + (target_gpa * remaining_semesters)) / (remaining_semesters + 1)
        print(f"If you maintain a GPA of {target_gpa}, your final CGPA will be: {predicted_cgpa:.2f}")
