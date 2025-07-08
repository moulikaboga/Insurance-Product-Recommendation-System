# insurance_recommendation_engine.py
# Combines customer profiling, needs analysis, product matching, explanations, and ranking

from customer_profiling import profile_customer
from needs_analysis import identify_needs
from product_matching import match_products


def explain_recommendation(product, customer_profile, needs):
    explanation = []

    if product['type'].lower() in needs:
        explanation.append(f"Matches identified need: {product['type']}")

    if product['target_risk'].lower() == customer_profile['risk'].lower():
        explanation.append(f"Risk profile matched: {product['target_risk']}")

    explanation.append(f"Suitable for age and income range")

    return "; ".join(explanation)


def score_product(product):
    # Simple rule-based scoring; you can replace this with ML-based ranking
    score = 0
    if product['type'].lower() in ['health', 'life']:
        score += 2
    if product['target_risk'].lower() == 'low':
        score += 1
    return score

def recommend(customer):
    customer_profile = profile_customer(customer)
    needs = identify_needs(customer_profile)
    matched = match_products(customer, customer_profile, needs)

    if not matched:
        return {
            "profile": customer_profile,
            "needs": needs,
            "recommendations": [],
        }

    enriched = []
    for product in matched:
        enriched.append({
            **product,
            "score": score_product(product),
            "explanation": explain_recommendation(product, customer_profile, needs)
        })

    ranked = sorted(enriched, key=lambda x: x['score'], reverse=True)

    return {
        "profile": customer_profile,
        "needs": needs,
        "recommendations": ranked,
    }



# def recommend(customer):
#     customer_profile = profile_customer(customer)
#     needs = identify_needs(customer_profile)
#     matched = match_products(customer_profile, needs)

#     if not matched:
#         return {
#             "profile": customer_profile,
#             "needs": needs,
#             "recommendations": [],
#         }

    # Rank and explain each product
    enriched = []
    for product in matched:
        enriched.append({
            **product,
            "score": score_product(product),
            "explanation": explain_recommendation(product, customer_profile, needs)
        })

    # Sort by score descending
    ranked = sorted(enriched, key=lambda x: x['score'], reverse=True)

    return {
        "profile": customer_profile,
        "needs": needs,
        "recommendations": ranked,
    }


# Example test
if __name__ == "__main__":
    import json
    with open("sample_input.json") as f:
        customer = json.load(f)

    output = recommend(customer)

    print("--- Customer Profile ---")
    print(output['profile'])

    print("\n--- Identified Needs ---")
    print(output['needs'])

    print("\n--- Product Recommendations ---")
    for rec in output['recommendations']:
        print(f"- {rec['name']} ({rec['type']}) | Score: {rec['score']} | {rec['explanation']}")
