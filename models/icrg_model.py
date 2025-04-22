def run_icrg_model(country, industry, time_horizon, broad_risk, future_concerns, recommendation_type):
    score = 70
    risks = ["Inflation", "Debt load", "Currency fluctuation"]

    if "fx" in broad_risk.lower() or "currency" in broad_risk.lower():
        score -= 10
        risks.append("FX exposure risk")

    if "sovereign" in future_concerns.lower():
        score -= 5
        risks.append("Sovereign instability")

    if recommendation_type == "Go / No Go Decision":
        recommendation = "High macroeconomic risk suggests caution in initial entry."
    elif recommendation_type == "Investment Timing Advice":
        recommendation = "Monitor inflation and FX trends before committing major capital."
    else:
        recommendation = "Consider currency hedging and partnering with institutions with local market experience."

    summary = (
        f"The ICRG model reflects macroeconomic pressures that may impact {industry} operations in {country}. "
        f"{recommendation}"
    )

    return {
        "model": "ICRG",
        "country": country,
        "score": score,
        "risk_level": "Moderate" if score > 60 else "High",
        "key_risks": risks,
        "summary": summary
    }