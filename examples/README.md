# Risk Calculation Examples (v2)

Healthcare-focused risk calculations with temporal and equity weights.

## Contents
- `docs/parameter_definitions.md`
- `docs/clinical_scenarios.md`
- `docs/validation_framework.md`
- `data/example_inputs.csv`
- `data/validation_scenarios.csv`
- `data/healthcare_contexts.json`
- `src/risk_models.py`
- `notebooks/01_risk_examples.ipynb`
- `tests/test_suite.py`
- `requirements.txt`

## Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Run tests
```bash
pytest -q
```
