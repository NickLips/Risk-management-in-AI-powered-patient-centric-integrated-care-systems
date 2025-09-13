# Clinical Scenarios

## 1) ED Triage AI (Sepsis Early Warning)
- **Context**: Vital signs + labs to flag possible sepsis at triage.
- **Typical ranges**: probability_failure 0.08–0.15; time_delay_months 1–3; patient_population 5k–50k.
- **FHIR**: `Observation`, `Encounter`, `Condition`, `DiagnosticReport`.

## 2) Radiology Diagnostic AI (Mammography)
- **Context**: AI-aided detection improves early-stage detection.
- **Typical ranges**: missed_benefits_usd 200k–3M; time_delay_months 3–12.
- **FHIR**: `ImagingStudy`, `DiagnosticReport`, `Observation`.

## 3) ICU Monitoring AI
- **Context**: Predicts deterioration to prompt interventions.
- **Typical ranges**: workflow_disruption 0.2–0.6; integration_quality 0.5–0.9.
- **FHIR**: `Observation`, `Device`, `Observation.component`.

**Equity considerations** apply to all scenarios via `vulnerability_score`, `access_barriers`, `outcome_disparities`.
