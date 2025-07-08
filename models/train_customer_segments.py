# models/train_customer_segments.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import os

# Load customer data
df = pd.read_csv('data/insurance.csv')

# Select numeric features
X = df[['age', 'bmi', 'children']]

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Save models
os.makedirs('models', exist_ok=True)
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

with open('models/kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)

print("✅ KMeans model and scaler saved to 'models/' folder.")
