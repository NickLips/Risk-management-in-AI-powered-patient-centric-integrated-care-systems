# Framework_definitions

## Novel Healthcare AI Risk Definition

Current risk definitions fail healthcare because they ignore timing and missed opportunities. We created a new definition that fixes these problems while building on established ISO standards. Our definition recognizes that in healthcare, doing nothing can be as risky as taking action:

**AI Healthcare Risk**  
"Effect of uncertainty on healthcare objectives arising from either implementing or not implementing AI-powered healthcare interventions, considering both immediate and temporal consequences for patient and population health outcomes."

*Note 1 to entry:* AI healthcare risk explicitly includes both commission risks (negative effects from AI use) and omission risks (negative effects from AI non-use or delayed use).  
*Note 2 to entry:* The temporal dimension recognizes that healthcare decisions often have irreversible consequences and that delayed beneficial interventions constitute a form of harm.  
*Note 3 to entry:* This risk definition requires simultaneous evaluation of action and inaction scenarios against healthcare objectives.

This definition extends ISO 31073:2022 by explicitly recognizing dual pathways in healthcare AI decision-making. Unlike traditional risk models where uncertainty affects only action consequences, healthcare AI introduces scenarios where both action and inaction carry potential for benefit and harm. In ICS environments, this distinction becomes operationally critical because care coordination decisions made by one institution affect patient outcomes across the entire network.

---

## Specialized ICS Risk Terminology

Building on our healthcare-specific risk definition, we developed precise terminology addressing multi-institutional care coordination challenges. To illustrate the framework's practical application, we trace a representative cancer detection scenario through each risk concept:

### AI Opportunity Risk
Expected harm from delayed or absent AI implementation when beneficial interventions are available.  
**Example:** An ICS network delays implementing an AI mammography screening tool with 15% higher early-stage cancer detection rates. During the 8-month delay, 50 women develop late-stage breast cancer that could have been detected earlier.  
**Calculation:** P_opportunity = 0.08 (probability of missed early detection) × S_opportunity = 0.75 (severity of health outcome deterioration from delayed diagnosis) = 0.06 expected loss per patient, compounded across the care network.

### Implementation Inertia
Systematic delays in AI adoption due to complex multi-institutional governance requiring consensus among organizations with different risk tolerances.  
**Example:** The mammography AI requires approval from three ICS institutions: primary care centers, imaging facilities, and oncology services. Primary care approves immediately, imaging requests 6-month validation, oncology demands 12-month liability review. The network implements nothing until all agree, creating 12-month implementation inertia while patients receive suboptimal screening.

### Foregone Health Benefit
Quantifiable health losses from delayed AI implementation preventing care pathway optimization.  
**Example:** During the implementation delay, the ICS experiences 25 preventable late-stage diagnoses, 40 unnecessary biopsies from false positives, and $2.3M in additional treatment costs — all quantifiable foregone benefits that could have been avoided through timely AI deployment.

### Therapeutic Lag
Measurable delays between AI readiness and network-wide deployment due to varying institutional timelines.  
**Example:** The mammography AI becomes clinically ready in January but achieves full ICS deployment in November — an 11-month therapeutic lag during which patients receive inconsistent care quality across the network, with some facilities providing AI-enhanced screening while others use standard protocols.

### Population Opportunity Exposure
Differential AI access across patient populations within ICS networks creating equity concerns.  
**Example:** Urban ICS facilities implement the AI tool first, while rural sites wait for technical infrastructure upgrades. This creates a 6-month disparity where urban women receive enhanced screening while rural women — already facing higher cancer mortality rates — experience delayed access to improved diagnostics, amplifying existing health disparities.

---

These terms provide semantic precision necessary for ICS risk metadata repositories in coordinated care environments where traditional single-institution frameworks prove inadequate. Mathematical models require operational implementation through existing healthcare information systems, necessitating alignment with established metadata standards and interoperability protocols.
