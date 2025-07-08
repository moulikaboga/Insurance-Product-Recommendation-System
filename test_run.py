# test_run.py
import json
from recommendation_engine import recommend

with open("sample_input.json") as f:
    customer = json.load(f)

result = recommend(customer)

print("---- Customer Profile ----")
print(result["profile"])

print("\n---- Identified Needs ----")
print(result["needs"])

# print("\n---- Product Recommendations ----")
# for r in result["recommendations"]:
#     print(f"- {r['name']} ({r['type']}) | Risk: {r['target_risk']}")
print("\n---- Product Recommendations ----")
for rec in result['recommendations']:
    print(f"- {rec['name']} ({rec['type']}) | Risk: {rec['target_risk']} | Score: {rec['score']}")
    print(f"  → Why: {rec['explanation']}\n")

