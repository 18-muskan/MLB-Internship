
# Day 15 - K-Means Clustering and Elbow Method

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# Get the current script folder
BASE_DIR = Path(__file__).resolve().parent

# Create graphs folder inside Day15
GRAPHS_DIR = BASE_DIR / "graphs"
GRAPHS_DIR.mkdir(exist_ok=True)

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Convert dataset into a Pandas DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)

print("===== K-MEANS CLUSTERING =====")

print("\nFirst five rows:")
print(df.head())

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply the Elbow Method
inertia_values = []

print("\nCalculating inertia for different K values...")

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)
    inertia_values.append(model.inertia_)

    print(f"K = {k}, Inertia = {model.inertia_:.2f}")

# Plot the Elbow Method graph
plt.figure(figsize=(8, 5))
plt.plot(
    range(1, 11),
    inertia_values,
    marker="o"
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Iris Dataset")
plt.xticks(range(1, 11))
plt.grid(True)

# Save graph inside Day15/graphs
elbow_path = GRAPHS_DIR / "elbow_method.png"
plt.savefig(elbow_path, dpi=300, bbox_inches="tight")
print(f"\nElbow graph saved at: {elbow_path}")

plt.show()
plt.close()

# Apply K-Means with 3 clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to the DataFrame
df["Cluster"] = clusters

print("\nCluster counts:")
print(df["Cluster"].value_counts().sort_index())

# Visualize clusters using petal measurements
plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 2],
    X[:, 3],
    c=clusters,
    cmap="viridis",
    edgecolor="black"
)

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clustering of Iris Flowers")
plt.colorbar(label="Cluster")
plt.grid(True)

# Save cluster graph inside Day15/graphs
cluster_path = GRAPHS_DIR / "kmeans_clusters.png"
plt.savefig(cluster_path, dpi=300, bbox_inches="tight")
print(f"Cluster graph saved at: {cluster_path}")

plt.show()
plt.close()

print("\nK-Means clustering completed successfully!")
print("Check the Day15/graphs folder for both PNG files.")
