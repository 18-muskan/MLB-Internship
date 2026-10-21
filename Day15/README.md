
# Day 15 - Iris Flower Clustering and Visualization

## Overview
This project uses the Iris dataset to understand unsupervised learning, K-Means clustering, the Elbow Method, and Principal Component Analysis (PCA).

## Dataset
The Iris dataset is available in Scikit-learn.

- Total samples: 150
- Numerical features: 4
- Flower species: Setosa, Versicolor, Virginica
- Samples per species: 50

## 1. Dataset Exploration
The dataset was loaded using Scikit-learn and converted into a Pandas DataFrame.

The dataset was checked for:
- First five rows
- Dataset shape and column names
- Missing values
- Statistical summary
- Species counts

No missing values were found.

## 2. K-Means Clustering
K-Means is an unsupervised learning algorithm that groups similar data points into clusters.

The numerical features were standardized before clustering.

Three clusters were created using K-Means. The resulting cluster sizes were 53, 50, and 47 samples.

## 3. Elbow Method
The Elbow Method was used to compare inertia values for K values from 1 to 10.

The graph shows a noticeable reduction in inertia as K increases. Three clusters were used for the project because the Iris dataset contains three known species. The Elbow Method helps assess this choice, but it does not guarantee that the optimal K is exactly 3.

## 4. Principal Component Analysis (PCA)
PCA reduces the number of features while preserving as much data variation as possible.

The original four features were reduced to two principal components.

The two components retained 95.81% of the total variance, making the dataset easier to visualize in two dimensions.

## 5. Visualizations
The graphs are saved in the graphs folder.

- elbow_method.png: Elbow Method graph
- kmeans_clusters.png: K-Means cluster visualization
- pca_visualization.png: PCA visualization
- mini_project_elbow.png: Mini project Elbow graph
- original_iris_data.png: Original data using actual species
- mini_project_kmeans.png: K-Means clusters
- mini_project_pca.png: PCA visualization using actual species
- mini_project_pca_clusters.png: PCA visualization using cluster labels

## 6. Observations
- K-Means formed three clusters.
- Setosa is generally well separated from the other species.
- Versicolor and Virginica can overlap because their measurements are similar.
- Cluster numbers do not directly represent species names.
- PCA reduced four features to two components while retaining 95.81% of the variance.
- Visualizations helped compare the original species with the discovered clusters.

## 7. Files
- dataset_exploration.py: Dataset exploration
- kmeans_clustering.py: K-Means and Elbow Method
- pca_analysis.py: PCA analysis
- iris_mini_project.py: Complete mini project
- graphs/: Generated PNG graphs

## 8. Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn

## Conclusion
This project demonstrates how unsupervised learning can discover patterns in data. K-Means groups similar flowers, while PCA makes the dataset easier to visualize by reducing its dimensions.
