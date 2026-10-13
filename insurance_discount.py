def insurance_discount(age_group, claims_history, policy_type):
    """Illustrative rule only; replace with your instructor’s actual rules."""
    age_base = {"<25": 5, "25-65": 10, ">65": 5}
    claims_adjustment = {"none": 5, "1": 0, "2+": -5}
    policy_adjustment = {"Standard": 0, "Premium": 5}

    if age_group not in age_base:
        raise ValueError("Invalid age group")
    if claims_history not in claims_adjustment:
        raise ValueError("Invalid claims history")
    if policy_type not in policy_adjustment:
        raise ValueError("Invalid policy type")

    discount = age_base[age_group] + claims_adjustment[claims_history] + policy_adjustment[policy_type]
    return max(0, min(20, discount))
