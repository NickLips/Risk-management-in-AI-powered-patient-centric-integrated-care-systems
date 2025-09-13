# Parameter Definitions (Healthcare Context)

| Parameter | Description | Type/Range | Default | Units | Notes |
|---|---|---|---|---|---|
| probability_failure | Likelihood AI implementation causes failure/harm | [0–1] | 0.10 | – | Clinical safety; higher = worse |
| impact_severity | Severity of harm if failure occurs | [0–1] | 0.60 | – | Maps to patient safety impact |
| data_volume | Throughput of records/events relevant to AI | ≥0 | 10_000 | records/month | Scaling factor for exposure |
| standardization_maturity | Maturity of data standards & interoperability | (0–1] | 0.70 | – | Use 0.01 floor to avoid ÷0 |
| missed_benefits_usd | Monetary value of benefits forgone due to delay/non-use | ≥0 | 500_000 | USD | e.g., avoided complications |
| time_delay_months | Delay in deployment/uptake | ≥0 | 6 | months | Used for temporal amplification |
| patient_population | Population exposed to decision | ≥1 | 10_000 | persons | Used to compute per-capita |
| current_performance | Baseline performance without AI | [0–1] | 0.70 | – | Higher baseline reduces opp. risk |
| system_conflicts | Tech/system conflicts introduced | [0–1] | 0.30 | – | Interfaces, versions, etc. |
| workflow_disruption | Disruption to clinical workflow | [0–1] | 0.40 | – | Interruptions, rework |
| user_confusion | Cognitive burden, UI ambiguity | [0–1] | 0.30 | – | Training, alerts overload |
| integration_quality | Effectiveness of integration | [0–1] | 0.70 | – | Higher quality reduces risk |
| vulnerability_score | Population clinical/social vulnerability | [0–1] | 0.50 | – | e.g., CVD risk, SDOH burden |
| access_barriers | Barriers to accessing care/AI | [0–1] | 0.40 | – | Distance, broadband, cost |
| outcome_disparities | Observed disparities in outcomes | [0–1] | 0.30 | – | By race, rurality, etc. |
| discount_rate | Annual discount rate | ≥0 | 0.03 | 1/yr | Time preference |
| time_horizon_years | Evaluation horizon | ≥0 | 1.0 | years | Converted from months if needed |
| urgency_factor | Clinical urgency multiplier | ≥0 | 1.0 | – | Higher = more urgent |
| w_impl | Weight for Implementation risk | [0–1] | 0.40 | – | Must sum to 1 with others |
| w_opp | Weight for Opportunity risk | [0–1] | 0.40 | – |  |
| w_int | Weight for Interaction risk | [0–1] | 0.20 | – |  |
| opp_cap_usd_per_patient | Cap used to normalize opp. risk per patient | >0 | 10000 | USD/patient | For unitless aggregation |

## FHIR / HL7 Considerations
- **FHIR resources**: `Patient`, `Observation`, `DiagnosticReport`, `MedicationRequest`, `Encounter`.
- **Data quality** aligned with **ISO/IEC 8000**: accuracy, completeness, consistency, timeliness.
- **USCDI v6** fields used for stratification: demographics + SDOH (Gravity Project domains).
