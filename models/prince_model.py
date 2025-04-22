def run_prince_model(country, industry, time_horizon):
    return {
        "model": "PRINCE",
        "country": country,
        "score": 70,
        "risk_level": "Moderate",
        "key_risks": ["Regulatory uncertainty", "Elite capture", "Judicial delays"],
        "summary": f"PRINCE model finds moderate institutional risk in {country} for the {industry} sector over {time_horizon}."
    }