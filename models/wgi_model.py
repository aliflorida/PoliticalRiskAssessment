def run_wgi_model(country, industry, time_horizon):
    return {
        "model": "WGI",
        "country": country,
        "sector": industry,
        "time_horizon": time_horizon,
        "summary": f"Sample WGI results for {country} in {industry} ({time_horizon})",
        "score": 78
    }