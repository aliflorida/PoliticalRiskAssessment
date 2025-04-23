def generate_full_report(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type, models):
    sections = []

    sections.append(f"## Executive Summary\nThis report provides a comprehensive political risk analysis for {company_name}'s proposed {investment_type.lower()} in the {industry} sector in {target_country}.")
    sections.append("## Political Risk Overview\nPolitical risk refers to the likelihood that political decisions, events, or conditions will adversely affect the business environment and investment returns.")

    sections.append(f"## Contextual Risk Factors\nBased on known conditions and historical precedent in {target_country}, significant concerns include: {broad_risk}.\nForecasted issues such as {future_concerns} are also likely to disrupt short and mid-term operations.")

    sections.append("## Model Analysis and Scoring")
    decision_score = 0
    for model in models:
        sections.append(f"### {model['model']} Model")
        sections.append(f"**Score**: {model['score']} / 100")
        decision_score += model['score']
        sections.append("**Risk Breakdown:**")
        sections.append(f"- Macro: {', '.join(model['macro'])}")
        sections.append(f"- Micro: {', '.join(model['micro'])}")
        sections.append(f"- Sovereign: {', '.join(model['sovereign'])}")
        sections.append("**Recommendations:**")
        sections.append(model['recommendations'])

    avg_score = decision_score / len(models)
    if avg_score > 70:
        decision = "GO"
        advisory = "Conditions are acceptable for expansion, though ongoing monitoring is required."
    elif avg_score > 50:
        decision = "DELAY"
        advisory = "Current risk levels are moderate. Recommend delaying investment until after key reforms or elections."
    else:
        decision = "NO-GO"
        advisory = "Political and economic instability present significant barriers to sustainable operations."

    sections.append("## Final Recommendation")
    sections.append(f"**Decision**: {decision}\n**Rationale**: {advisory}")

    return "\n\n".join(sections)