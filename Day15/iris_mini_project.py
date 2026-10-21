
# Day 15 - Iris Flower Clustering and Visualization Mini Project

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Set project paths
BASE_DIR = Path(__file__).resolve().parent
GRAPHS_DIR = BASE_DIR / "graphs"
GRAPHS_DIR.mkdir(exist_ok=True)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["Species"] = [iris.target_names[i] for i in y]

print("=" * 50)
print("IRIS FLOWER CLUSTERING AND VISUALIZATION")
print("=" * 50)

# Explore the dataset
print("\nFirst five rows:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nSpecies counts:")
print(df["Species"].value_counts())

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
inertia_values = []

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    model.fit(X_scaled)
    inertia_values.append(model.inertia_)

# Save Elbow graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia_values, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method - Iris Dataset")
plt.xticks(range(1, 11))
plt.grid(True)
plt.savefig(
    GRAPHS_DIR / "mini_project_elbow.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Apply K-Means with three clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)
df["Cluster"] = clusters

print("\nK-Means cluster counts:")
print(df["Cluster"].value_counts().sort_index())

# Visualize original data using selected features
plt.figure(figsize=(8, 5))
scatter = plt.scatter(
    X[:, 2],
    X[:, 3],
    c=y,
    cmap="viridis",
    edgecolor="black"
)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Original Iris Data - Actual Species")
plt.colorbar(scatter, label="Species (0, 1, 2)")
plt.grid(True)
plt.savefig(
    GRAPHS_DIR / "original_iris_data.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Visualize K-Means clusters
plt.figure(figsize=(8, 5))
scatter = plt.scatter(
    X[:, 2],
    X[:, 3],
    c=clusters,
    cmap="viridis",
    edgecolor="black"
)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris Data - K-Means Clusters")
plt.colorbar(scatter, label="Cluster")
plt.grid(True)
plt.savefig(
    GRAPHS_DIR / "mini_project_kmeans.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Apply PCA to reduce four features to two
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualize PCA data colored by actual species
plt.figure(figsize=(8, 5))
scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y,
    cmap="viridis",
    edgecolor="black"
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization - Actual Species")
plt.colorbar(scatter, label="Species (0, 1, 2)")
plt.grid(True)
plt.savefig(
    GRAPHS_DIR / "mini_project_pca.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Visualize PCA data colored by K-Means clusters
plt.figure(figsize=(8, 5))
scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters,
    cmap="viridis",
    edgecolor="black"
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization - K-Means Clusters")
plt.colorbar(scatter, label="Cluster")
plt.grid(True)
plt.savefig(
    GRAPHS_DIR / "mini_project_pca_clusters.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Display observations
print("\nPCA total variance retained:")
print(f"{sum(pca.explained_variance_ratio_) * 100:.2f}%")

print("\nPROJECT OBSERVATIONS")
print("Number of clusters formed: 3")
print("Setosa is generally well separated from the other species.")
print("Versicolor and Virginica may overlap in some regions.")
print("PCA reduced four features to two principal components.")
print("The PCA plot makes the data easier to visualize.")

print("\nAll mini project graphs saved in:")
print(GRAPHS_DIR)

print("\nMini project completed successfully!")
