# Task 02 - ML Risk Register

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Small dataset | Model performance may be unstable | High | Use larger dataset before production |
| Class imbalance | Churn cases may be missed | Medium | Monitor recall, precision and F1-score |
| Data leakage | Inflated evaluation results | Medium | Use only prediction-time available features |
| False positive | Unnecessary retention action | Medium | Human review before action |
| False negative | At-risk customer may be missed | Medium | Monitor errors and combine ML with business rules |
| Privacy risk | Customer information may be exposed | Low/Medium | Minimise personal data and restrict access |
| Population bias | Model may not generalise to all customers | High | Collect representative data and evaluate across relevant groups |
| Model misuse | Automated decisions may harm customers | Medium | Use model as decision support, not sole decision-maker |