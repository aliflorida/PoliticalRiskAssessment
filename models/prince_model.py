def run_prince_model(country, industry, time_horizon):
    return {
        "model": "PRINCE",
        "country": country,
        "sector": industry,
        "time_horizon": time_horizon,
        "summary": f"Sample PRINCE results for {country} in {industry} ({time_horizon})",
        "score": 72
    }