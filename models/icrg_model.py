def run_icrg_model(country, industry, time_horizon):
    return {
        "model": "ICRG",
        "country": country,
        "sector": industry,
        "time_horizon": time_horizon,
        "summary": f"Sample ICRG results for {country} in {industry} ({time_horizon})",
        "score": 65
    }
