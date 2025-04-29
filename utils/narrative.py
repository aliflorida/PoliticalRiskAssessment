def generate_full_report(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type, models):
    sections = []
    sections.append(f"# Executive Summary\n{company_name} is exploring a {investment_type.lower()} in {target_country}'s {industry} sector.")
    sections.append("## What is Political Risk?\nIt refers to threats posed by political actions or instability affecting investments.")
    if broad_risk:
        sections.append(f"## Primary Concerns\n{broad_risk}")
    if future_concerns:
        sections.append(f"## Forecasting Focus\n{future_concerns}")
    sections.append("## Model Results")
    total = 0
    for m in models:
        sections.append(f"### {m['model']}\nScore: {m['score']}\nMacro: {', '.join(m['macro'])}\nMicro: {', '.join(m['micro'])}\nSovereign: {', '.join(m['sovereign'])}")
        sections.append(f"Recommendations: {m['recommendations']}")
        total += m['score']
    avg = total / len(models)
    if avg > 70: dec, reason = "GO", "Low-moderate risk."
    elif avg > 50: dec, reason = "DELAY", "Moderate risk. Wait for improvement."
    else: dec, reason = "NO-GO", "High risk. Proceeding not advised."
    sections.append(f"## Final Recommendation\n**{dec}** - {reason}")
    return "\n\n".join(sections)