import numpy as np
import pandas as pd

marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

# Q1. Calculate total marks obtained by each student
student_totals = np.sum(marks, axis=1)
print("\nTotal marks of each student:")
print(student_totals) 

# Q2. Calculate average marks of each student
student_averages = np.mean(marks, axis=1)
print("\nAverage marks of each student:")
print(student_averages)

# Q3. Calculate average marks in each subject
subject_averages = np.mean(marks, axis=0)
print("\nAverage marks in each subject:")
print(subject_averages)

# Q4. Find highest score in each subject
highest_subject_scores = np.max(marks, axis=0)
print("\nHighest score in each subject:")
print(highest_subject_scores)

# Q5. Find lowest score in each subject
lowest_subject_scores = np.min(marks, axis=0)
print("\nLowest score in each subject:")
print(lowest_subject_scores)

# Q6. Find students whose average marks are above 80
students_above_80 = np.where(student_averages > 80)[0] + 1
print("\nStudents whose average marks are above 80:")
print(students_above_80)

# Q7. Assign Pass or Fail status using np.where()
pass_fail_status = np.where(student_averages >= 40, "Pass", "Fail")
print("\nPass/Fail status:")
print(pass_fail_status)

# Q8. Find the index of the highest-performing student
highest_student_index = np.argmax(student_averages)
print("\nIndex of highest-performing student:")
print(highest_student_index)

# Q9. Calculate standard deviation for each subject
subject_standard_deviation = np.std(marks, axis=0)
print("\nStandard deviation of each subject:")
print(subject_standard_deviation)

# Q10. Convert final results into a Pandas DataFrame
student_results = pd.DataFrame({
    "Student": [1, 2, 3, 4, 5],
    "Python": marks[:, 0],
    "SQL": marks[:, 1],
    "Machine Learning": marks[:, 2],
    "Total Marks": student_totals,
    "Average Marks": student_averages,
    "Status": pass_fail_status
})

print("\nFinal Student Performance DataFrame:")
print(student_results)