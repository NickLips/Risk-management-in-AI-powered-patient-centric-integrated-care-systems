import math
import pandas as pd
from src.risk_models import validate_parameters, implementation_risk, opportunity_risk, interaction_risk, calculate_temporal_weight, calculate_equity_weight, total_risk

def test_division_by_zero_handling():
    r = implementation_risk(0.2, 0.5, 1000, 0.0)  # maturity 0 -> floored to 0.01 in spec example; function protects locally
    assert r > 0

def test_parameter_bounds_validation():
    p = {'probability_failure': 2, 'impact_severity': -1, 'standardization_maturity': 0, 'patient_population': 0, 'w_impl': 2, 'w_opp': 2, 'w_int': 2}
    q = validate_parameters(p)
    assert 0.0 <= q['probability_failure'] <= 1.0
    assert 0.0 <= q['impact_severity'] <= 1.0
    assert q['standardization_maturity'] >= 0.01
    assert q['patient_population'] >= 1
    assert math.isclose(q['w_impl'] + q['w_opp'] + q['w_int'], 1.0, rel_tol=1e-9)

def test_hand_checkable_example():
    params = dict(
        probability_failure=0.10, impact_severity=0.5, data_volume=1000, standardization_maturity=0.5,
        missed_benefits_usd=120000, time_delay_months=6, patient_population=10000, current_performance=0.8,
        system_conflicts=0.2, workflow_disruption=0.3, user_confusion=0.1, integration_quality=0.9,
        vulnerability_score=0.2, access_barriers=0.2, outcome_disparities=0.1,
        discount_rate=0.0, time_horizon_years=1.0, urgency_factor=1.0,
        w_impl=0.4, w_opp=0.4, w_int=0.2, opp_cap_usd_per_patient=10000
    )
    out = total_risk(params)
    # Manual expectations:
    # impl = (0.1*0.5*1000)/0.5 = 100
    # opp_per_cap = 120000/10000 = 12 USD/patient; time_factor=0.5; unmet=0.2 -> raw=1.2 ; normalized=1.2/10000=0.00012
    # int = 0.5*0.2 + 0.3*0.3 + 0.2*0.1 = 0.1 + 0.09 + 0.02 = 0.21 ; mitigated = 0.21*(1-0.9)=0.021
    # impl_norm = 100/1000=0.1 ; agg = 0.4*0.1 + 0.4*0.00012 + 0.2*0.021 ≈ 0.04 + 0.000048 + 0.0042 = 0.044248
    # w_t=1.0 ; w_e = 1 + 0.5*0.2 + 0.3*0.2 + 0.2*0.1 = 1 + 0.10 + 0.06 + 0.02 = 1.18
    # r_total ≈ 0.044248 * 1 * 1.18 ≈ 0.052213
    assert math.isclose(out['r_impl'], 100.0, rel_tol=1e-9)
    assert math.isclose(out['r_opp'], 0.00012, rel_tol=1e-9)
    assert math.isclose(out['r_int'], 0.021, rel_tol=1e-9)
    assert math.isclose(out['w_temporal'], 1.0, rel_tol=1e-9)
    assert math.isclose(out['w_equity'], 1.18, rel_tol=1e-9)
    assert math.isclose(out['r_total'], 0.052213, rel_tol=1e-6)

def test_clinical_scenario_realism():
    # ICU scenario should reduce interaction risk with high integration quality
    icu = dict(
        probability_failure=0.1, impact_severity=0.5, data_volume=12000, standardization_maturity=0.9,
        missed_benefits_usd=400000, time_delay_months=4, patient_population=5000, current_performance=0.8,
        system_conflicts=0.25, workflow_disruption=0.5, user_confusion=0.4, integration_quality=0.8,
        vulnerability_score=0.6, access_barriers=0.5, outcome_disparities=0.4,
        discount_rate=0.03, time_horizon_years=0.25, urgency_factor=1.3,
        w_impl=0.4, w_opp=0.4, w_int=0.2, opp_cap_usd_per_patient=10000
    )
    out = total_risk(icu)
    assert out['r_int'] < 0.25  # mitigated by integration_quality
