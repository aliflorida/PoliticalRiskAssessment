
def generate_full_report(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type, models):
    sections = []

    sections.append(f"# Executive Summary\nThis analysis assesses the political risk facing {company_name}'s proposed {investment_type.lower()} in the {industry} sector within {target_country}.")
    sections.append("## What Is Political Risk?\nPolitical risk refers to the probability that political actions or instability will affect an investor’s ability to operate profitably or safely within a host country. This includes regulatory uncertainty, corruption, elections, military intervention, or nationalization of assets.")

    sections.append(f"## Why It Matters\nFor the {industry} sector in {target_country}, exposure to volatile regulatory systems and shifting political alliances directly affects licensing, transaction processing, and legal protections for digital operations.")

    if broad_risk:
        sections.append(f"## Primary Political Risk Concerns\n{broad_risk}")
    if future_concerns:
        sections.append(f"## Future-Oriented Forecast Risks\n{future_concerns}")

    sections.append("## Methodology\nThis report uses a blended application of the PRINCE, ICRG, and WGI models. Each model assesses a specific dimension of political risk across macroeconomic, institutional, and sovereign stability categories. Variables are scored from 0–10, weighted by relevance to sector and country dynamics, and aggregated to form model scores.")

    total_score = 0
    for model in models:
        sections.append(f"### {model['model']} Model")
        sections.append(f"**Score**: {model['score']} / 100")
        total_score += model['score']
        sections.append("**Macro Risk Variables**: " + ', '.join(model['macro']))
        sections.append("**Micro Risk Variables**: " + ', '.join(model['micro']))
        sections.append("**Sovereign Risk Variables**: " + ', '.join(model['sovereign']))
        sections.append("**Mitigation Strategy**: " + model['recommendations'])

    avg_score = total_score / len(models)
    if avg_score >= 70:
        decision = "GO"
        rationale = "Aggregate risk is moderate to low. Expansion may proceed with basic safeguards."
    elif avg_score >= 50:
        decision = "DELAY"
        rationale = "Risk levels suggest operational instability in the mid term. Delay recommended pending next election/reform cycle."
    else:
        decision = "NO-GO"
        rationale = "Host country conditions do not favor entry. Risk of financial and reputational harm is high."

    sections.append("## Final Recommendation")
    sections.append(f"**Recommended Action**: {decision}")
    sections.append(f"**Rationale**: {rationale}")

    return "\n\n".join(sections)
