# Day 12 - Data Preprocessing and Student Score Prediction

## Overview
In this task, I learned data preprocessing and built a Linear Regression model using Python and Scikit-learn to predict student average scores.

## Tasks Completed
- Loaded and checked the student performance dataset.
- Checked missing values.
- Created the Average_Score column.
- Selected features (X) and target (y).
- Split the dataset into 80% training and 20% testing data.
- Trained a Linear Regression model.
- Compared actual and predicted scores.
- Calculated MAE, MSE, and R² score.
- Generated an Actual vs Predicted scatter plot.

## Requirements
- Python
- Pandas
- Scikit-learn
- Matplotlib
- The provided student_performance.csv dataset

## Input
The program uses the existing dataset:

`Day6/Student_Performance_Analysis/student_performance.csv`

The dataset contains 20 students and the following columns:
- Student_ID
- Name
- Age
- Program
- Python
- Mathematics
- Statistics
- Machine_Learning
- Attendance

The model uses Python, Mathematics, Statistics, and Machine_Learning marks as input features. Average_Score, calculated from these four subjects, is the target.

## How to Run
Open PowerShell in the MLB-Internship repository root folder.

Run the preprocessing script:

`python Day12/data_preprocessing.py`

Run the Linear Regression model:

`python Day12/linear_regression.py`

Run the complete prediction project:

`python Day12/student_score_prediction.py`

Install any missing libraries if required:

`python -m pip install pandas scikit-learn matplotlib`

## Expected Outputs
The preprocessing script displays:
- The first five dataset rows.
- Missing values in each column.
- The Average_Score column.
- Training and testing dataset shapes.

Expected split:
- Training features: (16, 4)
- Testing features: (4, 4)
- Training target: (16,)
- Testing target: (4,)

The prediction scripts display:
- Actual vs Predicted scores.
- MAE, MSE, and R² evaluation metrics.

The complete project also saves a scatter plot at:

`Day12/graphs/actual_vs_predicted.png`

## Model Evaluation
Results from the current run:
- MAE: 0.0000
- MSE: 0.0000
- R² Score: 1.0000

## Observations
The model predicted the test scores exactly in this experiment. This happened because Average_Score is calculated directly from the same four subject marks used as input features. Therefore, these results do not demonstrate independent real-world prediction accuracy.

Train-test splitting helps evaluate a model on data not used during training. Data preprocessing must be handled carefully to avoid data leakage.

## What I Learned
I learned how to prepare a dataset, select features and a target, split data into training and testing sets, train a Linear Regression model, make predictions, and evaluate results using standard metrics.

## Project Files
- data_preprocessing.py
- linear_regression.py
- student_score_prediction.py
- graphs/actual_vs_predicted.png
- README.md
- day12_explanation.mp4 (screen recording)
