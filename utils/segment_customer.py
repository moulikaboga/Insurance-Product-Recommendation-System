# utils/segment_customer.py

import pickle
import pandas as pd

# ✅ Load scaler and model correctly
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('models/kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

def get_customer_segment(customer):
    features = pd.DataFrame([{
        'age': customer['age'],
        'bmi': customer['bmi'],
        'children': customer['children']
    }])
    scaled = scaler.transform(features)  # ✅ Now defined
    segment = kmeans.predict(scaled)[0]
    return segment
