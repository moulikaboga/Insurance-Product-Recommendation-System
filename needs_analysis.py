# needs_analysis.py

def identify_needs(profile):
    needs = []

    if profile["has_dependents"]:
        needs.append("family_health")

    if profile["life_stage"] == "young_adult":
        needs.append("guaranteed_return_plan")

    if profile["risk"] == "high":
        needs.append("critical_illness_cover")

    return needs
