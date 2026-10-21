
# Day 15 - Principal Component Analysis (PCA)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Get the current script folder
BASE_DIR = Path(__file__).resolve().parent

# Create graphs folder
GRAPHS_DIR = BASE_DIR / "graphs"
GRAPHS_DIR.mkdir(exist_ok=True)

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Create a Pandas DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)

print("===== PCA ANALYSIS =====")

print("\nOriginal dataset shape:")
print(df.shape)

# Scale the data before applying PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce four features to two components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create a DataFrame for PCA results
pca_df = pd.DataFrame(
    X_pca,
    columns=["Principal Component 1", "Principal Component 2"]
)

print("\nFirst five rows after PCA:")
print(pca_df.head())

print("\nTransformed dataset shape:")
print(pca_df.shape)

# Display explained variance
print("\nExplained variance ratio:")
print(pca.explained_variance_ratio_)

print(
    "\nTotal variance retained:",
    round(sum(pca.explained_variance_ratio_) * 100, 2),
    "%"
)

# Visualize PCA-transformed data
plt.figure(figsize=(8, 5))

scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=iris.target,
    cmap="viridis",
    edgecolor="black"
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization of Iris Dataset")

plt.colorbar(
    scatter,
    label="Actual Flower Species (0, 1, 2)"
)

plt.grid(True)

# Save graph in the graphs folder
pca_path = GRAPHS_DIR / "pca_visualization.png"

plt.savefig(
    pca_path,
    dpi=300,
    bbox_inches="tight"
)

print(f"\nPCA graph saved at: {pca_path}")

plt.show()
plt.close()

print("\nPCA analysis completed successfully!")
