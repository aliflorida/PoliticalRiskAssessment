def generate_detailed_narrative(company_name, target_country, investment_type, industry, broad_risk, future_concerns, model_results):
    lines = []
    lines.append(f"# Executive Summary\n{company_name} is considering a {investment_type.lower()} in the {industry} sector of {target_country}.")
    lines.append("## Defining Political Risk\nPolitical risk refers to the probability that political events, decisions, or instability will adversely impact investment performance or operational continuity.")
    lines.append("## Why It Matters\nThis includes legal changes, government overreach, civil unrest, and policy volatility—all of which threaten investor certainty.")
    lines.append(f"## Background on {target_country}\nHistorically, {target_country} has experienced regulatory fluctuations, electoral disputes, and varying degrees of judicial independence impacting foreign direct investment (FDI).")
    if broad_risk:
        lines.append(f"## Specific Concerns\n{broad_risk}")
    if future_concerns:
        lines.append(f"## Forecasting Triggers\n{future_concerns}")

    lines.append("## Methodology\nThis report integrates PRINCE, ICRG, and WGI models using weighted multi-variable scoring. Variables are chosen based on historic correlation with investor disruption.")

    for model in model_results:
        lines.append(f"### {model['model']} Model Results\n**Total Score**: {model['score']} / 100")
        lines.append("| Variable | Category | Score | Weight | Risk Level |")
        lines.append("|---|---|---|---|---|")
        for v in model['variables']:
            lines.append(f"| {v['variable']} | {v['category']} | {v['score']} | {v['weight']} | {v['level']} |")
        lines.append(f"**Recommendations:** {model['recommendations']}")

    average_score = sum([m['score'] for m in model_results]) / len(model_results)
    if average_score >= 70:
        decision = "GO"
        rationale = "Low to moderate political risk across all core models."
    elif average_score >= 50:
        decision = "DELAY"
        rationale = "Moderate risk; reevaluation advised after electoral cycle."
    else:
        decision = "NO-GO"
        rationale = "High political volatility and institutional fragility."

    lines.append("## Final Recommendation")
    lines.append(f"**Recommendation**: {decision} — {rationale}")
    return "\n".join(lines)