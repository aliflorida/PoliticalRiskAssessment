def run_icrg_model(country, industry, time_horizon):
    return {
        "model": "ICRG",
        "country": country,
        "score": 65,
        "risk_level": "Elevated",
        "key_risks": ["Sovereign debt", "FX volatility", "Inflation"],
        "summary": f"ICRG analysis shows elevated macro risk in {country}, especially affecting {industry} over {time_horizon}."
    }