
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Get the folder path
BASE_DIR = Path(__file__).resolve().parent

# Load cleaned dataset
DATA_PATH = BASE_DIR / "cleaned_student_performance.csv"
CHARTS_DIR = BASE_DIR / "charts"

df = pd.read_csv(DATA_PATH)

# Subject columns
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]

# 1. Total number of students
print("=" * 45)
print("STUDENT PERFORMANCE DASHBOARD")
print("=" * 45)

print("\n1. Total Number of Students:", len(df))

# 2. Average marks for each subject
subject_averages = df[subjects].mean().round(2)
print("\n2. Average Marks for Each Subject:")
print(subject_averages)

# 3. Top 5 performing students
top_students = df.nlargest(5, "Average_Score")
print("\n3. Top 5 Performing Students:")
print(top_students[["Name", "Average_Score", "Performance"]].to_string(index=False))

# 4. Students who need improvement
needs_improvement = df[df["Performance"] == "Needs Improvement"]
print("\n4. Students Who Need Improvement:")

if needs_improvement.empty:
    print("No students are in the Needs Improvement category.")
else:
    print(needs_improvement[["Name", "Average_Score"]].to_string(index=False))

# 5. Subject with highest class average
highest_subject = subject_averages.idxmax()
highest_average = subject_averages.max()

print("\n5. Highest Class Average:")
print(f"{highest_subject}: {highest_average}")

# 6. Visualize average marks by subject
plt.figure(figsize=(9, 5))
subject_averages.plot(kind="bar", rot=0)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "subject_average_chart.png")
plt.close()

# 7. Visualize top 5 students
plt.figure(figsize=(9, 5))
plt.bar(top_students["Name"], top_students["Average_Score"])
plt.title("Top 5 Performing Students")
plt.xlabel("Student Name")
plt.ylabel("Average Score")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "top_5_students_chart.png")
plt.close()

# 8. Three key insights
print("\n6. Key Insights:")
print(f"- The dataset contains {len(df)} students.")
print(f"- {highest_subject} has the highest class average of {highest_average}.")

if not needs_improvement.empty:
    print(
        f"- {len(needs_improvement)} student(s) need improvement "
        "because their average score is below 70."
    )
else:
    print("- No students have an average score below 70.")

print("\nDashboard analysis completed successfully!")
print("Additional charts saved in:", CHARTS_DIR)
