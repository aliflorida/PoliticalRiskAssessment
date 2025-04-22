def select_models(investment_type, industry, time_horizon):
    models = set()
    if industry.strip().lower() in ["fintech", "banking", "insurance"]:
        models.add("ICRG")
    if investment_type.lower() in ["joint venture", "infrastructure"]:
        models.add("PRINCE")
    if "long" in time_horizon.lower():
        models.add("WGI")
    if len(models) < 2:
        models.update(["PRINCE", "ICRG"])
    return list(models)[:3]