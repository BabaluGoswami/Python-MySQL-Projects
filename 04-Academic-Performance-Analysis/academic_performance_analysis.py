import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Q1. Create dataset containing marks from Semester 1 to Semester 6
academic_data = pd.DataFrame({
    "Subject": ["Python", "Java", "DBMS", "Computer Networks", "Operating System"],
    "Semester 1": [72, 68, 75, 70, 74],
    "Semester 2": [76, 71, 78, 73, 77],
    "Semester 3": [80, 75, 82, 78, 79],
    "Semester 4": [84, 79, 85, 81, 83],
    "Semester 5": [88, 84, 87, 85, 86],
    "Semester 6": [91, 88, 90, 89, 92]
})

# Q2. Find the number of semesters present in the dataset
semester_columns = academic_data.columns[1:]
number_of_semesters = len(semester_columns)
print("\nNumber of semesters:")
print(number_of_semesters)

# Q3. Find the total number of subjects studied
number_of_subjects = len(academic_data["Subject"])
print("\nTotal number of subjects:")
print(number_of_subjects)

# Q4. Find the highest marks
highest_marks = academic_data[semester_columns].max().max()
print("\nHighest marks:")
print(highest_marks)

# Q5. Find the lowest marks
lowest_marks = academic_data[semester_columns].min().min()
print("\nLowest marks:")
print(lowest_marks)

# Q6. Find the semester with the highest total marks
semester_totals = academic_data[semester_columns].sum()
best_total_semester = semester_totals.idxmax()
print("\nSemester with highest total marks:")
print(best_total_semester)

# Q7. Find the semester with the lowest total marks
worst_total_semester = semester_totals.idxmin()
print("\nSemester with lowest total marks:")
print(worst_total_semester)

# Q8. Display the first five records
print("\nFirst five records:")
print(academic_data.head())

# Q9. Find average marks for each semester
semester_averages = academic_data[semester_columns].mean()
print("\nAverage marks for each semester:")
print(semester_averages)

# Q10. Create a line graph of semester-wise average marks
plt.figure(figsize=(8, 5))
plt.plot(semester_columns, semester_averages, marker="o")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Semester-wise Average Marks")
plt.grid()
plt.show()

# Q11. Create a bar graph of subject-wise average marks
subject_averages = academic_data[semester_columns].mean(axis=1)

plt.figure(figsize=(8, 5))
plt.bar(academic_data["Subject"], subject_averages)
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Q12. Identify the highest-performing subject
best_subject_index = subject_averages.idxmax()
best_subject = academic_data.loc[best_subject_index, "Subject"]
print("\nHighest-performing subject:")
print(best_subject)

# Q13. Identify the lowest-performing subject
worst_subject_index = subject_averages.idxmin()
worst_subject = academic_data.loc[worst_subject_index, "Subject"]
print("\nLowest-performing subject:")
print(worst_subject)

# Q14. Identify the best and worst semester
best_semester = semester_averages.idxmax()
worst_semester = semester_averages.idxmin()

print("\nBest semester:")
print(best_semester)

print("\nWorst semester:")
print(worst_semester)

# Q15. Calculate improvement between Semester 1 and Semester 6
improvement = semester_averages["Semester 6"] - semester_averages["Semester 1"]
print("\nImprovement between Semester 1 and Semester 6:")
print(improvement)

# Q16. Calculate mean, median, maximum, minimum and standard deviation using NumPy
all_marks = academic_data[semester_columns].to_numpy()

marks_mean = np.mean(all_marks)
marks_median = np.median(all_marks)
marks_maximum = np.max(all_marks)
marks_minimum = np.min(all_marks)
marks_standard_deviation = np.std(all_marks)

print("\nMean:")
print(marks_mean)

print("\nMedian:")
print(marks_median)

print("\nMaximum:")
print(marks_maximum)

print("\nMinimum:")
print(marks_minimum)

print("\nStandard deviation:")
print(marks_standard_deviation)

# Q17. Create a graph showing performance of each subject across six semesters
plt.figure(figsize=(10, 6))

for index, subject in enumerate(academic_data["Subject"]):
    plt.plot(
        semester_columns,
        academic_data.iloc[index][semester_columns],
        marker="o",
        label=subject
    )

plt.xlabel("Semester")
plt.ylabel("Marks")
plt.title("Subject Performance Across Six Semesters")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Q18. Set academic target of 75% and show it using axhline()
plt.figure(figsize=(8, 5))
plt.plot(semester_columns, semester_averages, marker="o", label="Average Marks")
plt.axhline(y=75, linestyle="--", label="Academic Target 75%")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Performance with Academic Target")
plt.legend()
plt.grid()
plt.show()

# Q19. Compare performance with class average if class data is available
class_average = [70, 72, 74, 76, 78, 80]

plt.figure(figsize=(8, 5))
plt.plot(semester_columns, semester_averages, marker="o", label="My Average")
plt.plot(semester_columns, class_average, marker="o", label="Class Average")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("My Performance vs Class Average")
plt.legend()
plt.grid()
plt.show()

# Q20. Create a 2x2 Matplotlib dashboard
fig, dashboard = plt.subplots(2, 2, figsize=(14, 10))

dashboard[0, 0].plot(semester_columns, semester_averages, marker="o")
dashboard[0, 0].set_title("Semester-wise Average")
dashboard[0, 0].set_xlabel("Semester")
dashboard[0, 0].set_ylabel("Average Marks")
dashboard[0, 0].grid()

dashboard[0, 1].bar(academic_data["Subject"], subject_averages)
dashboard[0, 1].set_title("Subject-wise Average")
dashboard[0, 1].set_xlabel("Subject")
dashboard[0, 1].set_ylabel("Average Marks")
dashboard[0, 1].tick_params(axis="x", rotation=45)

dashboard[1, 0].bar(semester_columns, semester_totals)
dashboard[1, 0].set_title("Semester-wise Total")
dashboard[1, 0].set_xlabel("Semester")
dashboard[1, 0].set_ylabel("Total Marks")

dashboard[1, 1].plot(semester_columns, semester_averages, marker="o", label="My Average")
dashboard[1, 1].plot(semester_columns, class_average, marker="o", label="Class Average")
dashboard[1, 1].set_title("My Performance vs Class Average")
dashboard[1, 1].set_xlabel("Semester")
dashboard[1, 1].set_ylabel("Average Marks")
dashboard[1, 1].legend()
dashboard[1, 1].grid()

plt.tight_layout()
plt.show()

# Q21. Write five observations based on the visualizations
print("\nFive observations:")
print("1. Semester-wise average marks show an overall improvement in performance.")
print("2. Semester 6 has the highest average performance among all semesters.")
print("3. The subject-wise graph shows which subjects have stronger and weaker performance.")
print("4. The semester performance remains above the academic target of 75% in the later semesters.")
print("5. The comparison graph shows how my performance changes compared with the class average.")