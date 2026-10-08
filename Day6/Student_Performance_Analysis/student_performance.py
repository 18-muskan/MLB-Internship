import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Day6/Student_Performance_Analysis/student_performance.csv")

print("===== STUDENT PERFORMANCE DATASET =====")
print(df)

# 2. Display basic information about the dataset
print("\n===== FIRST FIVE ROWS =====")
print(df.head())

print("\n===== DATASET INFORMATION =====")
df.info()

# 3. Find missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 4. Calculate average marks for each subject
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]

print("\n===== AVERAGE MARKS FOR EACH SUBJECT =====")

for subject in subjects:
    average = df[subject].mean()
    print(f"{subject}: {average:.2f}")

# 5. Calculate average marks for each student
df["Average_Marks"] = df[subjects].mean(axis=1)

print("\n===== STUDENT AVERAGES =====")
print(df[["Student_ID", "Name", "Average_Marks"]])

# 6. Identify the top 5 performing students
top_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print("\n===== TOP 5 PERFORMING STUDENTS =====")
print(top_students[["Student_ID", "Name", "Average_Marks"]])

# 7. Find the overall class average
class_average = df["Average_Marks"].mean()

print("\n===== OVERALL CLASS AVERAGE =====")
print(f"{class_average:.2f}")

# 8. Find students scoring below the average
below_average = df[df["Average_Marks"] < class_average]

print("\n===== STUDENTS SCORING BELOW AVERAGE =====")
print(below_average[["Student_ID", "Name", "Average_Marks"]])

# 9. Display total number of students
total_students = len(df)

print("\n===== TOTAL NUMBER OF STUDENTS =====")
print(total_students)

# 10. Save the processed dataset
output_file = "Day6/Student_Performance_Analysis/processed_student_performance.csv"

df.to_csv(output_file, index=False)

print("\n===== PROCESSED DATASET SAVED =====")
print(output_file)

# 11. Display final dataset
print("\n===== FINAL PROCESSED DATASET =====")
print(df)