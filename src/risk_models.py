from dataclasses import dataclass
from typing import Dict, Any

EPS = 1e-9

@dataclass
class RiskParams:
    w_impl: float = 0.4
    w_opp: float  = 0.4
    w_int: float  = 0.2
    discount_rate: float = 0.03
    opp_cap_usd_per_patient: float = 10000.0  # normalization cap

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def validate_parameters(p: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and coerce parameters to specification ranges."""
    q = dict(p)
    # Probabilities and severities
    for k in [
        'probability_failure','impact_severity','current_performance',
        'system_conflicts','workflow_disruption','user_confusion','integration_quality',
        'vulnerability_score','access_barriers','outcome_disparities'
    ]:
        if k in q:
            q[k] = clamp(float(q[k]), 0.0, 1.0)
    # Non-negative
    for k in ['data_volume','missed_benefits_usd','time_delay_months','patient_population',
              'discount_rate','time_horizon_years','urgency_factor','opp_cap_usd_per_patient']:
        if k in q:
            q[k] = max(0.0, float(q[k]))
    # Avoid zero maturity / population / cap
    if q.get('standardization_maturity', 0) <= 0:
        q['standardization_maturity'] = 0.01
    else:
        q['standardization_maturity'] = clamp(float(q['standardization_maturity']), 0.01, 1.0)
    if q.get('patient_population', 0) < 1:
        q['patient_population'] = 1.0
    if q.get('opp_cap_usd_per_patient', 0) <= 0:
        q['opp_cap_usd_per_patient'] = 10000.0
    # Weights
    for k in ['w_impl','w_opp','w_int']:
        if k in q:
            q[k] = clamp(float(q[k]), 0.0, 1.0)
    # Normalize weights
    tw = (q.get('w_impl',0.4) + q.get('w_opp',0.4) + q.get('w_int',0.2))
    if tw <= 0:
        q['w_impl'], q['w_opp'], q['w_int'] = 0.4, 0.4, 0.2
    else:
        q['w_impl'] /= tw; q['w_opp'] /= tw; q['w_int'] /= tw
    return q

# Algorithm 1: Implementation Risk
def implementation_risk(probability_failure, impact_severity, data_volume, standardization_maturity):
    if standardization_maturity <= 0:
        standardization_maturity = 0.01
    return (probability_failure * impact_severity * data_volume) / standardization_maturity

# Algorithm 2: Opportunity Risk (normalized per capita)
def opportunity_risk(missed_benefits_usd, time_delay_months, patient_population, current_performance, opp_cap_usd_per_patient=10000.0):
    per_capita = missed_benefits_usd / max(patient_population, 1.0)
    time_factor = time_delay_months / 12.0
    unmet_need = (1.0 - current_performance)
    raw = per_capita * time_factor * unmet_need  # USD per patient
    normalized = raw / max(opp_cap_usd_per_patient, EPS)  # unitless
    return normalized

# Algorithm 3: Interaction Risk (socio-technical)
def interaction_risk(system_conflicts, workflow_disruption, user_confusion, integration_quality):
    base = 0.5*system_conflicts + 0.3*workflow_disruption + 0.2*user_confusion
    mitigated = base * (1.0 - integration_quality + 0.0)
    return mitigated

# Algorithm 4: Temporal Weight
def calculate_temporal_weight(time_horizon_years, discount_rate, urgency_factor):
    return urgency_factor / ((1.0 + max(discount_rate, 0.0)) ** max(time_horizon_years, 0.0))

# Algorithm 5: Equity Weight
def calculate_equity_weight(vulnerability_score, access_barriers, outcome_disparities):
    # Baseline 1.0; additive modifiers with caps
    ew = 1.0 + 0.5*vulnerability_score + 0.3*access_barriers + 0.2*outcome_disparities
    return max(1.0, ew)

# Algorithm 6: Total Risk (aggregated, unitless)
def total_risk(params: Dict[str, Any]) -> Dict[str, float]:
    p = validate_parameters(params)
    r_impl = implementation_risk(p['probability_failure'], p['impact_severity'], p['data_volume'], p['standardization_maturity'])
    r_opp  = opportunity_risk(p['missed_benefits_usd'], p['time_delay_months'], p['patient_population'], p['current_performance'], p['opp_cap_usd_per_patient'])
    r_int  = interaction_risk(p['system_conflicts'], p['workflow_disruption'], p['user_confusion'], p['integration_quality'])
    w_t    = calculate_temporal_weight(p['time_horizon_years'], p['discount_rate'], p['urgency_factor'])
    w_e    = calculate_equity_weight(p['vulnerability_score'], p['access_barriers'], p['outcome_disparities'])
    # Normalize implementation by exposure to get unitless scale
    impl_norm = r_impl / (p['data_volume'] + EPS)  # 0..~
    agg = p['w_impl']*impl_norm + p['w_opp']*r_opp + p['w_int']*r_int
    agg_weighted = agg * w_t * w_e
    return {
        'r_impl': r_impl,
        'r_opp': r_opp,
        'r_int': r_int,
        'w_temporal': w_t,
        'w_equity': w_e,
        'r_total': agg_weighted
    }
