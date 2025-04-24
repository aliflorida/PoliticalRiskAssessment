def generate_full_report(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type, models):
    report = f"""
# Executive Summary
This report evaluates political risks for {company_name}'s {investment_type.lower()} in the {industry} sector in {target_country}. Using PRINCE and other models, we assess macroeconomic, sovereign, and institutional threats.

# Context
{target_country} presents complex institutional and economic challenges. These risks may impact regulatory clarity and operational security.

# Definition
Political risk refers to threats from government instability, conflict, corruption, or abrupt legal changes that affect business outcomes.

# Objective
- Concerns: {broad_risk}
- Forecast Focus: {future_concerns}
- Recommendation Type: {recommendation_type}

# Models Analyzed
""".strip()

    for model in models:
        report += f"""

## {model['model']} Model
Score: {model['score']} / 100  
Macro Risk: {', '.join(model['macro'])}  
Micro Risk: {', '.join(model['micro'])}  
Sovereign Risk: {', '.join(model['sovereign'])}  
Recommendations: {model['recommendations']}

""".strip()
    return report