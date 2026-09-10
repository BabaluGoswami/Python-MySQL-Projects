import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dataset load karna
education_data = pd.read_csv("EducationDataset_2023-24.csv")

# Q1. Find district with highest and lowest number of schools
highest_school_district = education_data.loc[
    education_data["No of Schools - Total"].idxmax(), "District"
]
lowest_school_district = education_data.loc[
    education_data["No of Schools - Total"].idxmin(), "District"
]

print("\nDistrict with highest number of schools:")
print(highest_school_district)

print("\nDistrict with lowest number of schools:")
print(lowest_school_district)


# Q2. Find district with highest total student enrollment
highest_enrollment_district = education_data.loc[
    education_data["No of Students - Total"].idxmax(), "District"
]

highest_enrollment = education_data["No of Students - Total"].max()

print("\nDistrict with highest total student enrollment:")
print(highest_enrollment_district)
print("Total students:", highest_enrollment)


# Q3. Compare boys and girls and find largest gender difference
education_data["Gender Difference"] = abs(
    education_data["No of Students - Boys"] -
    education_data["No of Students - Girls"]
)

largest_gender_difference = education_data.loc[
    education_data["Gender Difference"].idxmax(), "District"
]

print("\nDistrict with largest gender difference:")
print(largest_gender_difference)


# Q4. Find district with highest Class X pass percentage
highest_class_x_district = education_data.loc[
    education_data[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"].idxmax(),
    "District"
]

highest_class_x_percentage = education_data[
    " PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"
].max()

print("\nDistrict with highest Class X pass percentage:")
print(highest_class_x_district)
print("Pass percentage:", highest_class_x_percentage)


# Q5. Find district with highest Class XII pass percentage
highest_class_xii_district = education_data.loc[
    education_data["PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"].idxmax(),
    "District"
]

highest_class_xii_percentage = education_data[
    "PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"
].max()

print("\nDistrict with highest Class XII pass percentage:")
print(highest_class_xii_district)
print("Pass percentage:", highest_class_xii_percentage)


# Q6. Compare Class X and Class XII pass percentages across districts
class_x_pass_percentage = education_data[
    " PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"
]

class_xii_pass_percentage = education_data[
    "PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"
]

print("\nClass X pass percentages:")
print(class_x_pass_percentage)

print("\nClass XII pass percentages:")
print(class_xii_pass_percentage)

plt.figure(figsize=(12, 6))
plt.plot(education_data["District"], class_x_pass_percentage, marker="o", label="Class X")
plt.plot(education_data["District"], class_xii_pass_percentage, marker="o", label="Class XII")
plt.xticks(rotation=90)
plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII Pass Percentage")
plt.legend()
plt.tight_layout()
plt.show()


# Q7. Check relationship between number of schools and Class X pass percentage
plt.figure(figsize=(8, 6))
plt.scatter(
    education_data["No of Schools - Total"],
    class_x_pass_percentage
)
plt.xlabel("Number of Schools")
plt.ylabel("Class X Pass Percentage")
plt.title("Schools vs Class X Pass Percentage")
plt.tight_layout()
plt.show()


# Q8. Check relationship between total student enrollment and Class X pass percentage
plt.figure(figsize=(8, 6))
plt.scatter(
    education_data["No of Students - Total"],
    class_x_pass_percentage
)
plt.xlabel("Total Student Enrollment")
plt.ylabel("Class X Pass Percentage")
plt.title("Student Enrollment vs Class X Pass Percentage")
plt.tight_layout()
plt.show()


# Q9. Calculate students per school and find highest value
education_data["Students Per School"] = (
    education_data["No of Students - Total"] /
    education_data["No of Schools - Total"]
)

highest_students_per_school_district = education_data.loc[
    education_data["Students Per School"].idxmax(), "District"
]

highest_students_per_school = education_data["Students Per School"].max()

print("\nDistrict with highest students per school:")
print(highest_students_per_school_district)

print("Highest students per school:")
print(highest_students_per_school)

plt.figure(figsize=(12, 6))
plt.bar(
    education_data["District"],
    education_data["Students Per School"]
)
plt.xticks(rotation=90)
plt.xlabel("District")
plt.ylabel("Students Per School")
plt.title("Students Per School Across Districts")
plt.tight_layout()
plt.show()


# Q10. Identify three important observations using visualizations
print("\nImportant observations:")
print("1. Class X and Class XII pass percentages can be compared across districts using the line chart.")
print("2. The scatter plot shows whether number of schools appears related to Class X performance.")
print("3. The students-per-school chart shows differences in student load across districts.")