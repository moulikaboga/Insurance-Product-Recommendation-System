# product_matching.py

import pandas as pd

def in_range(value, range_str):
    try:
        low, high = map(int, range_str.split("-"))
        return low <= value <= high
    except:
        return False

def match_products(customer, profile, needs):
    df = pd.read_csv("data/products.csv")  # ✅ Load the product data inside
    recommendations = []

    for _, row in df.iterrows():
        if row["type"].lower() not in needs:
            continue

        # age_ok = in_range(customer["age"], str(row["target_age"]))
        # income_ok = in_range(customer["income"], str(row["target_income"]))
        # risk_ok = row["target_risk"].lower() == customer["risk"].lower()
        age_ok = in_range(customer["age"], str(row["target_age"]))
        income_ok = in_range(customer["income"], str(row["target_income"]))
        risk_ok = row["target_risk"].lower() == profile["risk"].lower()


        if age_ok and income_ok and risk_ok:
            recommendations.append({
                "product_id": row["product_id"],
                "name": row["name"],
                "type": row["type"],
                "target_risk": row["target_risk"]
            })

    return recommendations
