
def generate_full_report(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type, models):
    report = f"""
# Executive Summary
This report evaluates political risks associated with {company_name}'s {investment_type.lower()} in the {industry} sector in {target_country}. Using PRINCE, ICRG, and WGI models, we examine macroeconomic, sovereign, and institutional risks over short, mid, and long-term horizons.

# Company Background
{company_name} is exploring international opportunities as part of its strategic growth plan. This expansion targets {target_country}, with operations in the {industry} sector.

# Country Context
{target_country} has experienced political volatility, economic instability, and institutional inconsistencies. These dynamics impact risk models significantly.

# Political Risk and its Importance
Political risk refers to the likelihood of disruptions to operations due to political or institutional factors such as policy shifts, regulatory changes, or civil unrest.

# Forecast Objective
Our goal is to understand risk implications, forecast key disruptions, and guide investment decisions.

# Broad Risk Concerns
{broad_risk}

# Specific Forecast Concerns
{future_concerns}

# Recommendation Type
{recommendation_type}

# Detailed Model Outputs
""".strip()

    for model in models:
        report += f"""

## {model['model']} Model
**Score**: {model['score']}  
**Macro Risk**: {', '.join(model['macro'])}  
**Micro Risk**: {', '.join(model['micro'])}  
**Sovereign Risk**: {', '.join(model['sovereign'])}  
**Recommendations**: {model['recommendations']}

""".strip()

    return report
