def run_wgi_model(country, industry, time_horizon, broad_risk, future_concerns, recommendation_type):
    score = 75
    risks = ["Weak rule of law", "Limited accountability"]

    if "governance" in broad_risk.lower():
        score -= 10
        risks.append("Governance instability")

    if "corruption" in future_concerns.lower():
        score -= 10
        risks.append("Corruption risk")

    if recommendation_type == "Go / No Go Decision":
        recommendation = "Rule of law concerns may impact enforceability of agreements."
    elif recommendation_type == "Investment Timing Advice":
        recommendation = "Wait for regulatory clarity or improvement in governance indicators."
    else:
        recommendation = "Work with compliance advisors and evaluate third-party transparency ratings."

    summary = (
        f"WGI indicators suggest long-term concerns in governance quality affecting {industry} ventures in {country}. "
        f"{recommendation}"
    )

    return {
        "model": "WGI",
        "country": country,
        "score": score,
        "risk_level": "Medium" if score > 60 else "High",
        "key_risks": risks,
        "summary": summary
    }