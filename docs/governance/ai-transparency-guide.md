# AI Transparency & Compliance Guide: Principle I Enforcement

## Overview

As an AI systems reviewer, you enforce **Principle I: AI-Driven Financial Intelligence** during code review.

Principle I requires:
- **Transparent Models**: AI model and version documented
- **Validated Decisions**: Confidence scores calculated and exposed
- **Auditable Logic**: All AI decisions logged with reasoning
- **Configurable Parameters**: Model parameters adjustable, not hardcoded

## The Four Pillars of AI Governance

### 1. Transparency: Model Documentation

Every AI feature must document:
- **Model name**: Exact model identifier (e.g., "GPT-4-turbo v1", "XGBoost 1.7.2")
- **Model version**: Version used in production
- **Model source**: Where was model obtained/trained (OpenAI API, internal ML pipeline, third-party library)
- **License**: AI model license and restrictions
- **Purpose**: What business problem does this model solve

### 2. Validation: Confidence Scores

Every AI prediction must include confidence information:
- **Confidence score**: Numerical score (0.0-1.0) of model confidence
- **Confidence threshold**: What's the minimum acceptable confidence?
- **Below-threshold behavior**: What happens if confidence too low?
  - Return "insufficient data" error?
  - Escalate to human review?
  - Use fallback calculation?

### 3. Auditability: Decision Logging

Every AI decision must be logged with:
- **Input data**: What data was used for prediction?
- **Model used**: Which model and version made this decision?
- **Confidence score**: How confident was the model?
- **Output**: What decision/prediction was made?
- **Reasoning**: Key factors influencing the decision (feature importance, decision rules)
- **Timestamp**: When was decision made?
- **User/context**: Who triggered this decision (system, user, API call)?

### 4. Configurability: Parameter Control

Model parameters must be adjustable:
- **Confidence threshold**: Adjustable (can raise bar for acceptance)
- **Model selection**: Can choose different model/version
- **Input weighting**: Importance of different input factors
- **Fallback behavior**: Configurable rules for low-confidence cases

**Anti-Pattern**: Hardcoded parameters that require code change to adjust

## Review Checklist for Principle I

### Model Transparency

- [ ] **Model documented clearly**
  - [ ] Model name/identifier: ________________
  - [ ] Model version: ________________
  - [ ] Model source: ________________
  - [ ] Model license confirmed: ________________
  - [ ] Business purpose clear: ________________

- [ ] **Model card created** (for custom models)
  - [ ] Model performance metrics documented
  - [ ] Known limitations documented
  - [ ] Intended use cases defined
  - [ ] Misuse risks documented

### Confidence & Validation

- [ ] **Confidence score calculated**
  - [ ] Confidence returned with prediction
  - [ ] Confidence range clear (0.0-1.0)
  - [ ] Confidence properly scaled (not inverted)

- [ ] **Validation rules defined**
  - [ ] Confidence threshold documented
  - [ ] Below-threshold behavior specified
  - [ ] Error handling clear
  - [ ] Fallback logic defined

- [ ] **Edge cases handled**
  - [ ] Very high confidence (>0.99): Verified not overconfident
  - [ ] Very low confidence (<0.1): Fallback works correctly
  - [ ] Empty/null input: Proper error returned
  - [ ] Out-of-range input: Validation rejects

### Audit Trail & Logging

- [ ] **Decision logging implemented**
  - [ ] All AI decisions logged
  - [ ] Log includes: model, version, confidence, input, output
  - [ ] Log includes: timestamp, user context
  - [ ] Log format structured (JSON, not free text)

- [ ] **Reasoning captured**
  - [ ] Key decision factors logged
  - [ ] Feature importance available
  - [ ] Top contributing inputs documented
  - [ ] Explanation query-able

- [ ] **Log queryability**
  - [ ] Can filter by model/version
  - [ ] Can filter by confidence range
  - [ ] Can filter by date/user
  - [ ] Can identify problematic decisions

### Parameter Configurability

- [ ] **No hardcoded model parameters**
  - [ ] Confidence threshold: configurable ✅
  - [ ] Model selection: configurable ✅
  - [ ] Fallback behavior: configurable ✅
  - [ ] Input weighting: configurable ✅

- [ ] **Configuration validated**
  - [ ] Invalid configuration caught
  - [ ] Configuration changes logged
  - [ ] Configuration backwards-compatible

- [ ] **Parameter documentation**
  - [ ] All configurable parameters documented
  - [ ] Default values specified
  - [ ] Valid ranges specified
  - [ ] Examples provided

## Common AI Governance Violations

### CRITICAL

**Violation**: Model identity unknown
```python
# ❌ CRITICAL: Model unclear
def predict_portfolio_performance(portfolio):
    model = load_model("model.pkl")  # Which model? Version?
    return model.predict(portfolio.features)

# ✅ FIX: Model documented
def predict_portfolio_performance(portfolio):
    MODEL_NAME = "XGBoost Portfolio Predictor"
    MODEL_VERSION = "v2.1.0"
    MODEL_SOURCE = "s3://models/portfolio-v2.1.0.pkl"
    # Retrieve specific model version
    model = load_model_version(MODEL_SOURCE)
    return model.predict(portfolio.features)
```

**Violation**: No confidence score returned
- Fix: Calculate and return confidence with every prediction
- Impact: Decisions lack uncertainty context

**Violation**: Hardcoded model parameters
```python
# ❌ CRITICAL: Threshold hardcoded
def predict_recommendation(portfolio):
    score = model.predict(portfolio.features)[0]
    if score > 0.75:  # Hardcoded!
        return "RECOMMEND"
    else:
        return "SKIP"

# ✅ FIX: Configurable parameter
AI_CONFIDENCE_THRESHOLD = 0.75  # In config/settings
def predict_recommendation(portfolio):
    score = model.predict(portfolio.features)[0]
    if score > AI_CONFIDENCE_THRESHOLD:
        return "RECOMMEND"
    else:
        return "SKIP"
```

### MAJOR

**Violation**: AI decisions not logged
- Fix: Add comprehensive logging (model, confidence, inputs, outputs, reasoning)
- Impact: Can't audit AI decision-making

**Violation**: Confidence not validated
- Fix: Add below-threshold handling (error, escalate, fallback)
- Impact: Bad predictions used without warning

**Violation**: Reasoning not captured**
- Fix: Log feature importance or decision factors
- Impact: Can't explain why model made a decision

## Sample PR Review Workflow

**Example PR**: Add AI-powered portfolio risk assessment

1. **Check Model Documentation**:
   ```python
   # ✅ Good: Model clearly identified
   class PortfolioRiskAssessor:
       MODEL = "RandomForest-RiskPredictor-v1.2"
       MODEL_VERSION = "1.2.0"
       MODEL_SOURCE = "s3://ml-models/risk-v1.2.0.joblib"
       
       def assess(self, portfolio):
           model = self.load_model()
           risk_score, confidence = model.predict_with_confidence(portfolio)
           return {"risk_score": risk_score, "confidence": confidence}
   ```

2. **Verify Confidence Calculation**:
   - Confidence score returned? ✅
   - Range is 0.0-1.0? ✅
   - Properly scaled (high confidence = high probability)? ✅

3. **Check Validation & Fallback**:
   ```python
   # ✅ Good: Confidence validation
   if confidence < AI_CONFIDENCE_THRESHOLD:
       return {
           "risk_score": None,
           "confidence": confidence,
           "status": "LOW_CONFIDENCE",
           "recommended_action": "ESCALATE_TO_HUMAN_REVIEW"
       }
   ```

4. **Verify Audit Logging**:
   ```python
   # ✅ Good: Comprehensive logging
   logger.info({
       "event": "portfolio_risk_assessment",
       "model": "RandomForest-RiskPredictor-v1.2",
       "portfolio_id": portfolio.id,
       "input_features": portfolio.feature_dict(),
       "risk_score": risk_score,
       "confidence": confidence,
       "timestamp": datetime.now(),
       "user_id": context.user_id
   })
   ```

5. **Check Parameter Configurability**:
   - Confidence threshold configurable? ✅
   - Model version configurable? ✅
   - Fallback behavior configurable? ✅

6. **Approval**:
   ```markdown
   ✅ AI Review - Principle I APPROVED
   
   - Model clearly identified and sourced
   - Confidence scores calculated and returned
   - Below-threshold fallback handled
   - All decisions logged with reasoning
   - Parameters configurable
   - Ready for merge
   ```

## AI Team Review Responsibilities

| Responsibility | When | Who | Details |
|---|---|---|---|
| Principle I verification | Every AI PR | AI Systems Reviewer | Use checklist above |
| Model validation | New model introductions | AI Team | Verify model performance/fit |
| Reasoning audit | Complex AI PRs | AI Team | Verify decision logic sound |
| Confidence calibration | Quarterly | AI Team | Adjust thresholds if needed |
| Performance monitoring | Ongoing | AI Team | Monitor model performance drift |

## Escalation Path

Request changes if:
- Model identity unclear or missing
- Confidence scores absent
- Decisions not logged
- Parameters hardcoded
- Reasoning not captured

Escalate to Tech Lead if:
- Model performs poorly in audit
- Confidence threshold needs architectural change
- Logging infrastructure insufficient
- Multiple models need orchestration

## Resources

- [Constitution Principle I](../../.specify/memory/constitution.md#i-ai-driven-financial-intelligence)
- [Model Card Framework](https://arxiv.org/abs/1810.03993)
- [General Governance Checklist](../../specs/001-project-governance/contracts/general-governance-checklist.md)
- [Audit Trail Best Practices](compliance-audit-procedures.md)

## Questions?

Contact AI Systems Reviewer or Tech Lead.
