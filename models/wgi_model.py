def run_wgi_model(country, industry, time_horizon):
    return {
        "model": "WGI",
        "country": country,
        "score": 78,
        "risk_level": "Medium-High",
        "key_risks": ["Weak regulatory quality", "Corruption", "Low accountability"],
        "summary": f"WGI data suggests governance challenges in {country} for long-term {industry} investment."
    }