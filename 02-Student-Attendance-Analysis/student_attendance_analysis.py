import numpy as np
import pandas as pd

attendance = np.array([
    [90, 85, 95, 88],
    [75, 80, 70, 78],
    [95, 92, 98, 96],
    [65, 70, 72, 68],
    [85, 88, 90, 87]
])

# Q1. Calculate average attendance of each student
student_attendance_avg = np.mean(attendance, axis=1)
print("\nAverage attendance of each student:")
print(student_attendance_avg)

# Q2. Calculate average attendance of each subject
subject_attendance_avg = np.mean(attendance, axis=0)
print("\nAverage attendance of each subject:")
print(subject_attendance_avg)

# Q3. Find highest attendance in each subject
highest_attendance_subject = np.max(attendance, axis=0)
print("\nHighest attendance in each subject:")
print(highest_attendance_subject)

# Q4. Find lowest attendance in each subject
lowest_attendance_subject = np.min(attendance, axis=0)
print("\nLowest attendance in each subject:")
print(lowest_attendance_subject)

# Q5. Find students having average attendance above 80%
students_above_80_attendance = np.where(student_attendance_avg > 80)[0] + 1
print("\nStudents having average attendance above 80%:")
print(students_above_80_attendance)

# Q6. Find the student with the highest average attendance
best_attendance_student = np.argmax(student_attendance_avg)
print("\nStudent with highest average attendance:")
print(best_attendance_student + 1)

# Q7. Calculate standard deviation of attendance
attendance_standard_deviation = np.std(attendance)
print("\nStandard deviation of attendance:")
print(attendance_standard_deviation)

# Q8. Classify students as Eligible or Not Eligible based on 75% attendance
eligibility_status = np.where(student_attendance_avg >= 75, "Eligible", "Not Eligible")
print("\nEligibility status:")
print(eligibility_status)

# Q9. Convert attendance data into a Pandas DataFrame
attendance_table = pd.DataFrame({
    "Student": [1, 2, 3, 4, 5],
    "Python": attendance[:, 0],
    "Java": attendance[:, 1],
    "SQL": attendance[:, 2],
    "ML": attendance[:, 3]
})

# Q10. Add Status column to the DataFrame
attendance_table["Status"] = eligibility_status

print("\nFinal Attendance DataFrame:")
print(attendance_table)