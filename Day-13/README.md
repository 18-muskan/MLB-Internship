
# Day 13 - Classification and Model Evaluation

## Introduction

In this task, I learned about classification, model evaluation, Logistic Regression, Decision Trees, and confusion matrices. I used Python and Scikit-learn to build an Iris Flower Classification System.

## What is Classification?

Classification is a Machine Learning technique used to predict categories or classes. For example, predicting whether an email is spam or not spam.

Regression predicts numerical values, such as house prices, while classification predicts categories, such as flower species.

## Dataset

I used the built-in Iris dataset from Scikit-learn. It contains 150 samples, 4 features, and 3 flower species: setosa, versicolor, and virginica.

The features are sepal length, sepal width, petal length, and petal width.

## How to Run the Project

First, install the required libraries:
python -m pip install scikit-learn matplotlib

Run the classification practice script from the main repository folder:

python ".\Day-13\Classification_Practice\classification_practice.py"

Run the Iris classification project:
python ".\Day-13\Iris_Classification_Project\iris_classification.py"

## Input and Output

The model takes flower measurements as input, including sepal length, sepal width, petal length, and petal width.

The output is the predicted flower species: setosa, versicolor, or virginica.

The scripts also display model evaluation metrics, a classification report, and a confusion matrix. The Iris project prints sample predicted species alongside their actual species.

## Model Evaluation

I divided the dataset into 80% training data and 20% testing data. The model used 120 samples for training and 30 samples for testing.

The Logistic Regression model achieved the following results:

Accuracy: 0.9667 (96.67%)

Precision: 0.9697 (96.97%)

Recall: 0.9667 (96.67%)

F1-Score: 0.9666 (96.66%)

## Confusion Matrix

The confusion matrix was:

[[10  0  0]
 [ 0  9  1]
 [ 0  0 10]]


The model correctly classified 29 out of 30 test samples. All setosa and virginica samples were classified correctly, while one versicolor sample was predicted as virginica.

The confusion matrix images are saved in their respective project folders.


## Decision Tree Model Comparison

I also trained a Decision Tree model and compared it with Logistic Regression using the same training and testing data.

| Metric | Logistic Regression | Decision Tree |
| Accuracy | 96.67% | 93.33% |
| Precision | 96.97% | 93.33% |
| Recall | 96.67% | 93.33% |
| F1-Score | 96.66% | 93.33% |

Logistic Regression performed better than the Decision Tree on this test split. It correctly classified 29 out of 30 samples, while the Decision Tree achieved 28 correct predictions out of 30.

Both models performed well, but their results may change with different data splits or datasets.

## Conclusion

This task helped me understand classification, training and testing data, Logistic Regression, evaluation metrics, and confusion matrices. I also learned how to check model performance and identify incorrect predictions.

## Tools Used

Python 3.13, Scikit-learn, Matplotlib, and VS Code.
