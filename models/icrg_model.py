def run_icrg_model(country, industry, horizon):
    return {
        "model": "ICRG",
        "score": 70,
        "macro": ["FX risk", "High inflation"],
        "micro": ["Low investment confidence"],
        "sovereign": ["Debt servicing pressure"],
        "recommendations": "- Hedge currency exposure\n- Partner with local entities\n- Delay large capital projects"
    }