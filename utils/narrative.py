def generate_full_narrative(country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type):
    return f"""
## Political Risk Definition and Why It Matters
Political risk is the probability that political decisions, events, or instability will negatively affect business operations or investment returns. For companies expanding into international markets, political risk assessment is vital to avoid losses, adapt strategies, and safeguard assets.

## Company and Investment Overview
{company_name} is evaluating a {investment_type.lower()} opportunity in the {industry} sector within {country}. The company seeks to understand potential political challenges and determine whether to proceed, when to invest, or how to mitigate exposure.

## Historical and Political Context
Historically, {country} has experienced shifts in political power, regulatory changes, and economic volatility, all of which contribute to foreign investor uncertainty. This background provides important context for assessing future scenarios and institutional risks.

## Problem Statement
The key issue is to evaluate whether entering {country}'s market would pose unacceptable political or regulatory risks, or if strategies can be employed to manage those risks effectively.

## Baseline: Investor Losses and Exposure
Global data shows foreign investor losses are frequently tied to expropriation, regulatory overhaul, capital controls, and political violence. Identifying and forecasting such risks is key to avoiding similar outcomes.

## Forecasting Objective
The goal is to forecast, prevent, or mitigate future political losses for {company_name} and provide actionable insight to support a go/no-go decision or guide mitigation efforts.

## Methodology and Models
We used multiple models including:
- **PRINCE**: Assesses political, regulatory, institutional, and external factors
- **ICRG**: Scores macroeconomic, sovereign, and structural risk
- **WGI**: Analyzes governance strength and rule-of-law indicators

## Variable Selection and Measurement
Variables were chosen based on relevance to investment security and political forecasting. Each was assigned a weighted score based on risk exposure, with qualitative validation and scenario-based stress testing.

## Future Forecast
Our models evaluated near-, mid-, and long-term time horizons and flagged the following major risks:
- {broad_risk}
- {future_concerns}

## Recommendation Type: {recommendation_type}
Based on the overall model scores and contextual analysis, we provide the following recommendation...

## Mitigation Strategy Overview
Key mitigation actions may include:
- Partnering with local entities
- Legal protections and arbitration clauses
- Political risk insurance
- Delaying entry until after elections or policy reform

""".strip()