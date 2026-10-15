
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Get project folder paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "cleaned_student_performance.csv"
CHARTS_DIR = BASE_DIR / "charts"

# Create charts folder if it does not exist
CHARTS_DIR.mkdir(exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

sns.set_theme(style="whitegrid")

# Subject columns
subjects = ["Python", "Mathematics", "Statistics", "Machine_Learning"]

# 1. Bar Chart: Average marks of each student
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Name", y="Average_Score")
plt.title("Average Marks of Each Student")
plt.xlabel("Student Name")
plt.ylabel("Average Score")
plt.xticks(rotation=70, ha="right")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "student_average_bar_chart.png")
plt.close()

# 2. Histogram: Distribution of Average Scores
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Average_Score", bins=8, kde=True)
plt.title("Distribution of Student Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "average_score_histogram.png")
plt.close()

# 3. Scatter Plot: Python vs Machine Learning
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Python",
    y="Machine_Learning",
    hue="Performance",
    s=100
)
plt.title("Python vs Machine Learning Marks")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "python_vs_machine_learning.png")
plt.close()

# 4. Pie Chart: Performance categories
performance_counts = df["Performance"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    performance_counts.values,
    labels=performance_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Students by Performance Category")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "performance_pie_chart.png")
plt.close()

# 5. Box Plot: Marks in all subjects
plt.figure(figsize=(9, 5))
sns.boxplot(data=df[subjects])
plt.title("Distribution of Marks Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "subject_marks_box_plot.png")
plt.close()

print("All five charts created successfully!")
print("Charts saved in:", CHARTS_DIR)
