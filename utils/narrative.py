def generate_full_report(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type):
    return f"""
# Executive Summary
This report evaluates political risks associated with {company_name}'s {investment_type.lower()} in the {industry} sector in {target_country}. Using PRINCE, ICRG, and WGI models, we examine macroeconomic, sovereign, and institutional risks over short, mid, and long-term horizons.

# Problem Definition
{company_name} seeks to expand operations internationally, targeting {target_country} as a potential growth market. The core problem is determining whether political risk factors might hinder the venture’s viability or increase exposure to loss.

# Company Background
{company_name} is exploring international opportunities as part of its strategic growth plan. The current expansion focuses on {industry}, requiring stable legal frameworks, government transparency, and market accessibility.

# Target Country Context
{target_country} has a complex political history marked by regulatory instability, leadership transitions, and regional volatility. These factors shape the risk landscape for foreign investors and influence model forecasts.

# Political Risk Definition and Relevance
Political risk refers to the probability that political decisions, actions, or instability will negatively affect investment value or business continuity. For {industry} projects, risks may involve expropriation, policy shifts, social unrest, or legal unpredictability.

# Foreign Investor Loss Baseline
Historical trends in emerging markets show a correlation between high sovereign debt, weak regulatory enforcement, and investor losses due to unexpected reforms, revoked licenses, or blocked remittances.

# Forecasting Objectives
This report aims to forecast key risk factors, simulate political volatility, and identify mitigation strategies. The focus is on prevention and informed decision-making for the leadership team.

# Methodology
We applied the PRINCE (Political, Regulatory, Institutional, Nationalism, Corruption, External), ICRG (Macroeconomic/Sovereign), and WGI (Governance Quality) models.
- **Variable Selection**: Includes inflation, FX stability, institutional strength, judicial independence, corruption indices.
- **Scoring**: Weighted by relevance to investment type and country indicators.
- **Rationale**: These models reflect both qualitative and quantitative data and are standard across risk assessment practices.

# Model Output Summary
Each model outputs a score (0–100) and qualitative risk factors. Variables are grouped into macro, micro, and sovereign domains.

# Forecast Highlights
Key concerns based on user input and modeling:
- General risk concerns: {broad_risk}
- Future outlook: {future_concerns}

# Recommendations ({recommendation_type})
Based on scenario modeling, the recommendation type is tailored to the requested outcome. Details appear in the model-specific output.

# Mitigation Strategies
- Develop risk-sharing partnerships
- Secure political risk insurance
- Delay entry until after regulatory reforms
- Monitor sovereign credit and election cycles

# Final Guidance
Proceed with caution, contingent on upcoming stability indicators. Risk mitigation plans should be in place pre-entry.
"""