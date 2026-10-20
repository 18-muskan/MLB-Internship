# Day 14 - Breast Cancer Classification

## 1. Project Overview
This project uses the Scikit-learn Breast Cancer Wisconsin dataset to classify tumors as malignant or benign using Logistic Regression.

## 2. What I Learned About Model Evaluation
I learned how to evaluate a machine learning model using accuracy, precision, recall, F1-score, confusion matrix, and classification report. These metrics help us understand how well a model makes predictions and where it makes mistakes.

## 3. What Is Hyperparameter Tuning and Why Does It Matter?
Hyperparameter tuning means testing different model settings to find the best combination. It matters because suitable settings can improve model performance. I used GridSearchCV with 5-fold cross-validation to test different values of C and solver.

## 4. Best Parameters Found by GridSearchCV
- C: 0.1
- Solver: liblinear
- Best cross-validation accuracy: 98.02%

## 5. Baseline and Tuned Model Comparison

| Metric | Baseline Model | Tuned Model |
|---|---:|---:|
| Accuracy | 98.25% | 98.25% |
| Precision (benign) | 98.61% | 98.61% |
| Recall (benign) | 98.61% | 98.61% |
| F1-score (benign) | 98.61% | 98.61% |

Both models achieved the same test performance. Hyperparameter tuning found the best settings, but these settings did not improve the test results.

## 6. Key Observations
- The dataset contains 569 samples and 30 features.
- The data was divided into 455 training samples and 114 testing samples.
- The baseline and tuned models both achieved 98.25% accuracy.
- The confusion matrix shows 41 malignant and 71 benign cases correctly classified, with one incorrect prediction for each class.
- The model performed well on this test set, but this result does not guarantee performance on all new data.

## 7. Input
The input is the Breast Cancer Wisconsin dataset built into Scikit-learn. It contains 30 numerical features describing tumor characteristics.

Target labels:
- 0 = Malignant
- 1 = Benign

## 8. Output
The program displays:
- Dataset information and target distribution
- Baseline model evaluation metrics
- Best hyperparameters and cross-validation accuracy
- Tuned model evaluation metrics
- Confusion matrices and classification report
- Comparison between baseline and tuned models

It also saves the confusion matrix visualization as `confusion_matrix.png`.

## 9. How to Run
Open PowerShell or the VS Code terminal and run:

cd "C:\Users\owner\Documents\MLB-Internship\MLB-Internship\Day14"

Run dataset exploration:

python dataset_exploration.py

Run the baseline model:

python baseline_model.py

Run hyperparameter tuning:

python hyperparameter_tuning.py

Run the complete prediction pipeline:

python breast_cancer_prediction.py


If `python` does not work, use the full Python executable path:

& "C:\Users\owner\AppData\Local\Programs\Python\Python313\python.exe" breast_cancer_prediction.py

## 10. Conclusion
I learned dataset exploration, model training, evaluation, hyperparameter tuning, and model comparison using Scikit-learn. The final model achieved 98.25% test accuracy. This project is for educational purposes only and is not a medical diagnostic tool.
