def run_icrg_model(country, industry, horizon):
    return {
        "model": "ICRG",
        "score": 70,
        "macro": ["FX risk", "High inflation"],
        "micro": ["Low investment confidence"],
        "sovereign": ["Debt servicing pressure"],
        "recommendations": "Hedge currency exposure, partner with local entities, delay large capital projects."
    }