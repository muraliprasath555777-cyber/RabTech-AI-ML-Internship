# Responsible Data Card

## Dataset Purpose

This dataset supports a customer churn prediction exercise.
The intended decision is to identify customers who may be at risk of
churning so that appropriate retention or support actions can be considered.

The dataset must not be used as the sole basis for high-impact decisions
about customers.

## Provenance and Permission

The dataset was provided as part of the RabTech Academy internship task.
It is a small labelled training dataset intended for educational and
machine-learning baseline development.

Consent, licensing restrictions, and original data-collection procedures
are not documented in the provided dataset. These limitations should be
considered before any real-world deployment.

## Population and Representation

The dataset contains 12 customer records.

It represents a small sample of customers and may not represent the full
customer population. The sample is too small to establish reliable
population-level or demographic conclusions.

No demographic or sensitive attributes are provided.

## Features and Target

Features:
- tenure_months
- support_tickets
- monthly_spend_inr
- last_login_days
- plan_type

customer_id is an identifier and should not be used as a predictive feature.

Target:
- churned

Potential leakage should be checked before model training. Features should
only contain information that would have been available at prediction time.

## Quality Checks

- Number of records: 12
- Missing values: 0
- Duplicate rows: 0
- Target classes: 7 non-churned and 5 churned
- Plan types: Basic, Pro, Standard
- The dataset is very small and therefore model evaluation results may be
  unstable.

Train/test separation must be performed carefully to avoid information
leakage.

## Risks and Safeguards

### Bias Risk
The small sample may not represent the broader customer population.

Safeguard: collect a larger and more representative dataset before
production use.

### Privacy Risk
Customer-related information could be sensitive if linked to real people.

Safeguard: minimise personally identifying information and apply appropriate
access controls.

### False Positive Risk
A customer may be incorrectly classified as likely to churn and receive
unnecessary retention intervention.

Safeguard: use human review before consequential actions.

### False Negative Risk
A customer who is actually at risk of churning may be missed.

Safeguard: monitor model errors and combine predictions with business rules
and support-team judgement.

### Misuse Risk
The model could be treated as an automatic decision-maker.

Safeguard: use the model as decision support rather than as the sole basis
for customer decisions.

## Intended Evaluation

The majority-class baseline will be used as the initial non-ML reference.

Evaluation should include:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Error analysis

Because the dataset is very small, results should be treated as an
educational demonstration rather than evidence of production performance.