# AI Code Developer Guide: Principle I Implementation

## Overview

As a developer implementing AI-driven features, you must follow **Principle I: AI-Driven Financial Intelligence** to ensure AI insights are transparent, validated, auditable, and configurable.

This guide shows HOW to implement Principle I in your code.

## The Core Rule: AI Must Be Explainable

AI features must ALWAYS include:
1. **Transparency**: The model is documented and identifiable
2. **Validation**: Confidence scores tell us when to trust predictions
3. **Auditability**: All AI decisions are logged and queryable
4. **Configurability**: Model parameters can be changed without code updates

## Principle I Requirements

### 1. Model Transparency

Every AI feature must document:
- **Model name**: Exact identifier (e.g., "GPT-4-turbo", "portfolio-risk-v2.1")
- **Model version**: Version number being used
- **Model source**: Where it comes from (OpenAI, Hugging Face, custom pipeline)
- **Purpose**: What business problem it solves

**Code Implementation**:
```python
class PortfolioRecommendationEngine:
    """AI engine for portfolio recommendations with governance compliance"""
    
    # ✅ Model transparently documented
    MODEL_NAME = "XGBoost-Portfolio-Recommender"
    MODEL_VERSION = "2.1.0"
    MODEL_SOURCE = "s3://ml-models/portfolio-recommender/v2.1.0.joblib"
    MODEL_LICENSE = "Apache-2.0"
    BUSINESS_PURPOSE = "Recommend portfolio allocation changes based on market conditions"
    
    def __init__(self):
        self.model = self._load_model()
        self._log_model_loaded()
    
    def _load_model(self):
        """Load model from versioned source"""
        import joblib
        model = joblib.load(self.MODEL_SOURCE)
        return model
    
    def _log_model_loaded(self):
        """Log which model is being used"""
        logging.info({
            "event": "model_loaded",
            "model": self.MODEL_NAME,
            "version": self.MODEL_VERSION,
            "source": self.MODEL_SOURCE
        })
```

**Configuration** (not hardcoded):
```python
# config.py - AI configuration stored separately
AI_CONFIG = {
    "portfolio_recommender": {
        "model_name": "XGBoost-Portfolio-Recommender",
        "model_version": "2.1.0",
        "model_source": "s3://ml-models/portfolio-recommender/v2.1.0.joblib",
        "confidence_threshold": 0.75,
        "fallback_behavior": "escalate_to_human"
    }
}

# In code:
def get_recommendation(portfolio):
    config = AI_CONFIG["portfolio_recommender"]
    model = load_model(config["model_source"], config["model_version"])
    # Use config["confidence_threshold"] for validation
```

### 2. Validation with Confidence Scores

Every AI prediction must include:
- **Confidence score**: Numerical (0.0-1.0) of model confidence
- **Threshold validation**: Is confidence high enough to trust?
- **Fallback behavior**: What to do if confidence too low

**Code Implementation**:
```python
class AIPredictor:
    """Make predictions with confidence validation"""
    
    # ✅ Confidence threshold configurable
    CONFIDENCE_THRESHOLD = 0.75  # Or from config
    FALLBACK_ACTION = "escalate_to_human"  # Or from config
    
    def predict_with_validation(self, input_data):
        """
        Make prediction and validate confidence
        Returns: (prediction, confidence, status)
        """
        # Get prediction AND confidence score
        prediction, confidence = self.model.predict_with_confidence(input_data)
        
        # ✅ Check if confidence is acceptable
        if confidence < self.CONFIDENCE_THRESHOLD:
            return {
                "prediction": None,
                "confidence": confidence,
                "status": "LOW_CONFIDENCE",
                "action": self.FALLBACK_ACTION,
                "message": f"Confidence {confidence:.2%} below threshold {self.CONFIDENCE_THRESHOLD:.2%}"
            }
        
        # ✅ Confidence acceptable
        return {
            "prediction": prediction,
            "confidence": confidence,
            "status": "SUCCESS",
            "message": f"Prediction made with {confidence:.2%} confidence"
        }

# Usage
predictor = AIPredictor()
result = predictor.predict_with_validation(portfolio_data)

if result["status"] == "SUCCESS":
    use_prediction(result["prediction"])
else:
    handle_low_confidence(result["message"])
    # Escalate to human review, use fallback calculation, etc.
```

### 3. Auditability Through Logging

All AI decisions must be logged with:
- **Input data**: What was used for prediction
- **Model used**: Which model and version
- **Confidence score**: Model's confidence in output
- **Output**: What prediction was made
- **Key factors**: Why the model made this decision
- **Context**: Who triggered, when, system info

**Code Implementation**:
```python
class AuditableAIService:
    """AI service that logs all decisions for audit"""
    
    def make_decision(self, user_id, portfolio_id, decision_type):
        """
        Make AI decision and log for audit
        """
        # Prepare input
        portfolio = get_portfolio(portfolio_id)
        market_data = get_market_data()
        
        # Make prediction
        prediction, confidence = self.model.predict(
            features=self._extract_features(portfolio, market_data)
        )
        
        # ✅ Log EVERYTHING about this decision
        audit_log = {
            "event": "ai_decision",
            "decision_type": decision_type,
            
            # Model information
            "model_name": self.MODEL_NAME,
            "model_version": self.MODEL_VERSION,
            "model_source": self.MODEL_SOURCE,
            
            # Input data
            "portfolio_id": portfolio_id,
            "portfolio_value": str(portfolio.total_value),
            "portfolio_composition": str(portfolio.asset_allocation),
            "market_conditions": market_data,
            
            # Output
            "prediction": str(prediction),
            "confidence_score": float(confidence),
            "threshold_used": self.CONFIDENCE_THRESHOLD,
            "passed_validation": confidence >= self.CONFIDENCE_THRESHOLD,
            
            # Key factors (feature importance)
            "top_contributing_factors": self._get_feature_importance(prediction),
            
            # Context
            "user_id": user_id,
            "timestamp": datetime.utcnow().isoformat(),
            "request_id": generate_request_id(),
            "system_version": self.SYSTEM_VERSION
        }
        
        # ✅ Write to structured audit log
        self._write_audit_log(audit_log)
        
        # Return decision with audit reference
        return {
            "prediction": prediction,
            "confidence": confidence,
            "audit_id": audit_log["request_id"]
        }
    
    def _write_audit_log(self, log_entry):
        """Write to immutable audit log"""
        import json
        logging.info(json.dumps(log_entry))  # Structured logging
        
        # Also write to database/audit table for queryability
        db.execute("""
            INSERT INTO ai_decision_audit (audit_data, timestamp)
            VALUES (?, NOW())
        """, [json.dumps(log_entry)])
        db.commit()
    
    def _get_feature_importance(self, prediction):
        """Extract which inputs most influenced this prediction"""
        # Model-specific implementation
        # Return top 3-5 most important features and their impact
        pass
```

**Query Audit Log**:
```python
def query_ai_decisions(portfolio_id, confidence_range=None):
    """Query audit log to see all AI decisions for a portfolio"""
    
    query = "SELECT * FROM ai_decision_audit WHERE audit_data->>'portfolio_id' = ?"
    params = [portfolio_id]
    
    # Optional: filter by confidence range
    if confidence_range:
        min_conf, max_conf = confidence_range
        query += " AND (audit_data->>'confidence_score')::float BETWEEN ? AND ?"
        params.extend([min_conf, max_conf])
    
    results = db.query(query, params)
    return results
```

### 4. Configurability

Model parameters must be adjustable WITHOUT code changes:

**Configuration File** (YAML or JSON):
```yaml
# config/ai-config.yaml
ai_models:
  portfolio_recommender:
    model_name: "XGBoost-Portfolio-Recommender"
    model_version: "2.1.0"
    model_path: "s3://ml-models/portfolio-recommender/v2.1.0.joblib"
    
    # ✅ Thresholds configurable
    confidence_threshold: 0.75
    min_confidence: 0.5
    
    # ✅ Fallback behavior configurable
    fallback_action: "escalate_to_human"  # or "use_fallback_calculation"
    
    # ✅ Input weighting configurable
    feature_weights:
      market_volatility: 1.0
      portfolio_size: 0.8
      sector_concentration: 0.9
    
    # ✅ Enable/disable features
    enable_logging: true
    enable_mock_mode: false  # Set to true for testing
```

**Load Configuration**:
```python
import yaml

class ConfigurableAIEngine:
    def __init__(self, config_file):
        self.config = self._load_config(config_file)
        self.model = self._load_model()
    
    def _load_config(self, config_file):
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    
    def predict(self, input_data):
        # Use configurable threshold
        threshold = self.config["confidence_threshold"]
        
        prediction, confidence = self.model.predict(input_data)
        
        if confidence < threshold:
            # Use configurable fallback
            fallback = self.config["fallback_action"]
            if fallback == "escalate_to_human":
                return self._escalate_to_human(input_data)
            else:
                return self._use_fallback_calculation(input_data)
        
        return prediction
```

## Testing AI Code

### Unit Tests (Test Predictions)

```python
import pytest
from decimal import Decimal

def test_confidence_score_returned():
    """Every prediction includes confidence"""
    result = model.predict(test_data)
    assert "confidence" in result
    assert 0.0 <= result["confidence"] <= 1.0

def test_low_confidence_triggers_fallback():
    """Low confidence predictions use fallback"""
    with mock_model(confidence=0.5):  # Below threshold
        result = predictor.predict(test_data)
        assert result["status"] == "LOW_CONFIDENCE"
        assert result["action"] == "escalate_to_human"

def test_high_confidence_accepted():
    """High confidence predictions accepted"""
    with mock_model(confidence=0.95):  # Above threshold
        result = predictor.predict(test_data)
        assert result["status"] == "SUCCESS"
        assert result["prediction"] is not None

def test_model_version_matches():
    """Correct model version is loaded"""
    assert model.MODEL_VERSION == "2.1.0"
    assert model.MODEL_SOURCE == "s3://ml-models/portfolio-recommender/v2.1.0.joblib"
```

### Integration Tests (Test Full Flows with Mock API)

```python
def test_full_recommendation_flow_with_mock():
    """Full recommendation with audit logging"""
    
    # Mock Gemma API
    with mock_gemma_api(response="HOLD"):
        # Make recommendation
        result = ai_engine.get_recommendation(portfolio_id=1)
        
        # Verify response
        assert result["prediction"] is not None
        assert result["confidence"] >= 0.5
        
        # Verify audit logged
        audit_entry = db.query("SELECT * FROM ai_decision_audit WHERE portfolio_id = ?", [1])
        assert audit_entry is not None
        assert audit_entry.model_version == "2.1.0"
```

### Mock vs. Real API Testing

```python
def test_with_mock_gemma():
    """Test with mock before real API integration"""
    with mock_gemma_api():
        # Safe to test without real API calls
        result = predict_with_gemma(test_data)
        assert result is not None

@pytest.mark.integration
def test_with_real_gemma():
    """Real API integration test (separate from unit tests)"""
    # Only run with REAL_API_ENABLED=true
    result = predict_with_gemma(test_data)
    assert result["confidence"] > 0
```

## Code Review Checklist for AI Code

Before submitting PR with AI features:

- [ ] Model name, version, source documented
- [ ] Confidence score calculated and returned
- [ ] Confidence threshold enforced
- [ ] Fallback behavior defined (when confidence too low)
- [ ] All AI decisions logged with full context
- [ ] Audit log queryable (by model, date, confidence)
- [ ] Model parameters in configuration (not hardcoded)
- [ ] Mock tests written (before real API integration)
- [ ] Integration tests verify full flow
- [ ] Feature importance/reasoning captured in logs

## Common Patterns

### Pattern 1: Safe Gemma Integration (Mock First)

```python
# Step 1: Implement with mock
def predict(data):
    response = mock_gemma_call(data)
    return parse_response(response)

# Step 2: Add real API (but keep mock option)
GEMMA_MOCK_MODE = True  # In config

def predict(data):
    if GEMMA_MOCK_MODE:
        response = mock_gemma_call(data)
    else:
        response = real_gemma_call(data)
    return parse_response(response)

# Step 3: Tests use mock, can toggle to real
def test_predict():
    with config(GEMMA_MOCK_MODE=True):
        result = predict(test_data)
        assert result is valid
```

### Pattern 2: Configurable Thresholds

```python
# Bad: Hardcoded threshold
if confidence > 0.75:  # ❌ Can't change without code review

# Good: Configurable
CONFIDENCE_THRESHOLD = 0.75  # Can be overridden in config
if confidence > CONFIDENCE_THRESHOLD:  # ✅ Can be changed in config
```

### Pattern 3: Audit Trail with Request Tracking

```python
# Every AI decision gets unique ID for tracking
import uuid

def make_ai_decision(data):
    request_id = str(uuid.uuid4())
    
    # Make decision
    result = model.predict(data)
    
    # Log with request_id
    audit_log(request_id, result)
    
    # Return request_id so caller can trace
    return {"result": result, "audit_id": request_id}
```

## Resources

- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Constitution Principle I](../../.specify/memory/constitution.md#i-ai-driven-financial-intelligence)
- [AI Transparency Guide](ai-transparency-guide.md)
- [Pre-PR Checklist](developer-pre-pr-checklist.md)

---

**Remember**: AI must be explainable. Every model, every decision, every confidence score gets logged and auditable.

Questions? See FAQ.md or ask your Tech Lead.
