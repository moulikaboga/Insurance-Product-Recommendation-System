from utils.segment_customer import get_customer_segment

def profile_customer(customer):
    life_stage = "young_adult" if customer["age"] < 35 else "middle_aged"
    has_dependents = customer["children"] > 0
    risk = "high" if customer["smoker"] == "yes" else "low"

    try:
        segment = get_customer_segment(customer)
    except Exception as e:
        print("Segmenting failed:", e)
        segment = "N/A"

    return {
        "life_stage": life_stage,
        "has_dependents": has_dependents,
        "risk": risk,
        "segment": f"Segment {segment}"
    }
