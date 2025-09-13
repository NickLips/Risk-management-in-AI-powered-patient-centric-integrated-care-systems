# Patient-Centric AI Risk Assessment Framework

This repository provides the **full implementation package** for the research article by  
**Dmitrii Kharchevnikov** and **Nikolay Lipskiy (2025)**:  
*Patient-Centric AI Risk Assessment Framework: Decision-theoretic foundations and practical implementation examples.*

---

## Overview

Healthcare AI systems introduce unique risks where **action and inaction** can both produce harm.  
This framework provides:

- A **novel definition** of healthcare AI risk (implementation + omission + interaction)  
- **Mathematical models** incorporating temporal and equity weights  
- **Healthcare-specific parameterization** (ED triage, mammography AI, ICU monitoring)  
- **Executable notebooks** and **data scenarios** for reproducible calculations  
- **Validation framework** with hand-checkable examples and unit tests  

---

## Repository Structure

```
docs/
├─ index.md                   # Landing page (this file)
├─ framework_definitions.md   # Extended risk definitions
├─ decision_theory_foundations.md
├─ metadata_implementation_blueprint.md
├─ PatC_ICS_mathematical_model.md
├─ standards_review_matrix.md
├─ parameter_definitions.md
├─ clinical_scenarios.md
├─ validation_framework.md
├─ references/                # PDFs, XLSX, and primary standards
└─ figures/                   # Images, charts, diagrams
```

Other key folders:
- **examples/** – runnable notebooks, datasets, and results  
- **src/** – Python risk model implementations  
- **tests/** – validation and reproducibility checks  

---

## Quick Links

- [Parameter Definitions](parameter_definitions.md)  
- [Clinical Scenarios](clinical_scenarios.md)  
- [Validation Framework](validation_framework.md)  
- [Decision Theory Foundations](decision_theory_foundations.md)  

---

## Citation

If you use this framework, please cite:

```
Kharchevnikov, D., & Lipskiy, N. (2025). Patient-Centric AI Risk Assessment Framework:
Decision-theoretic foundations and practical implementation examples.
GitHub repository. https://github.com/OWNER/REPO
```

Also see `CITATION.cff` for machine-readable metadata.

---

## License

Released under the **MIT License** – see [LICENSE](../LICENSE).
