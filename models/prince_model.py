def run_prince_model(country, industry, time_horizon, broad_risk, future_concerns, recommendation_type):
    score = 60
    risks = ["Political interference", "Weak institutions"]

    if "corruption" in broad_risk.lower():
        score -= 5
        risks.append("Corruption")

    if "election" in future_concerns.lower():
        score -= 10
        risks.append("Election volatility")

    if recommendation_type == "Go / No Go Decision":
        recommendation = "Proceed with caution due to political uncertainty."
    elif recommendation_type == "Investment Timing Advice":
        recommendation = "Consider delaying until after elections or reforms clarify policies."
    else:
        recommendation = "Use local legal counsel and multi-stakeholder agreements to reduce political exposure."

    summary = (
        f"The PRINCE model reveals institutional and regulatory challenges for the {industry} sector in {country}. "
        f"{recommendation}"
    )

    return {
        "model": "PRINCE",
        "country": country,
        "score": score,
        "risk_level": "Moderate" if score > 50 else "High",
        "key_risks": risks,
        "summary": summary
    }