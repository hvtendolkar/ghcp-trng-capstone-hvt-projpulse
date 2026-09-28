# Developer Pre-PR Checklist

Use this checklist before submitting your PR to verify governance compliance.

## Step 1: Identify Applicable Principles

- [ ] My code involves **AI** (inference, predictions, confidence scores) → Principle I
- [ ] My code touches **financial data** (amounts, calculations, audit trails) → Principle II
- [ ] My code changes **API or database** (endpoints, schemas, migrations) → Principle III
- [ ] All code requires → Principle IV (Testing)

## Step 2: Verify Principle I (if applicable)

If your PR involves AI:

- [ ] AI model used is **documented** (which model? which version?)
- [ ] **Confidence score** calculated and returned with prediction
- [ ] **Decision reasoning** logged (what inputs led to decision?)
- [ ] **Model parameters** are configurable (not hardcoded)
- [ ] **Fallback behavior** defined (what if confidence is low?)

❓ **Question**: How confident is the AI in this prediction? If you can't answer, you need more logging.

## Step 3: Verify Principle II (if applicable)

If your PR involves financial data:

- [ ] All **currency** uses DECIMAL type (never float/double)
- [ ] **No duplicate calculations** (single source of truth)
- [ ] **Audit trail logging** added (who, when, what, why)
- [ ] **Input validation** present (amount ranges, currency codes)
- [ ] **Reconciliation** process documented or updated

❓ **Question**: If this calculation is wrong, how would we detect it? If you can't answer, you need reconciliation.

## Step 4: Verify Principle III (if applicable)

If your PR changes API or database:

- [ ] **API schemas** documented (OpenAPI/Pydantic)
- [ ] **Backward compatibility** maintained (2+ versions)
- [ ] **Database migrations** created (not direct schema changes)
- [ ] **Foreign key constraints** added/maintained
- [ ] **Endpoint contracts** unchanged or have migration plan

❓ **Question**: If I deploy this code then need to rollback immediately, will data be lost? If yes, you need a safer migration.

## Step 5: Verify Principle IV (Testing - ALL code)

- [ ] **Coverage target**: 80% or higher
  - Command: `pytest --cov=src --cov-report=term`
  - Coverage report shows green?

- [ ] **Unit tests** present
  - Tests for individual functions/methods
  - Edge cases covered (empty, null, negative, large numbers)
  - Business logic tested in isolation

- [ ] **Integration tests** present (if applicable)
  - Full request/response workflows tested
  - Database interactions tested
  - External service calls mocked

- [ ] **Database tests** present (if applicable)
  - Migrations tested in isolation
  - Transactions tested
  - Rollback scenarios tested

- [ ] **Regression tests** present (if bug fix)
  - Test fails before your fix
  - Test passes after your fix
  - Demonstrates bug is fixed

❓ **Question**: If I run `pytest`, do all tests pass? If no, fix before submitting.

## Step 6: Double-Check Checklists

### Code Review Checklist

- [ ] Code follows project style guide
- [ ] No debug print statements left
- [ ] No TODOs without tracking issue
- [ ] No commented-out code blocks
- [ ] Documentation/comments updated

### Governance Checklist

Verify all relevant items are checked:

**If Principle I applies**: All I items checked? ✅
**If Principle II applies**: All II items checked? ✅
**If Principle III applies**: All III items checked? ✅
**Principle IV (always)**: All IV items checked? ✅

### PR Template

- [ ] PR description filled out
- [ ] Governance principles marked in PR template
- [ ] References to any related issues/tickets
- [ ] Test coverage percentage noted
- [ ] Deployment considerations documented

## Step 7: Submit PR

When all checklists pass:

1. Push your branch
2. Create PR using `.github/pull_request_template.md`
3. Fill out governance checklist in PR description
4. Request reviewers:
   - Architecture owner (if Principle III applies)
   - Financial domain expert (if Principle II applies)
   - AI systems reviewer (if Principle I applies)
   - Tech lead (reviews Principle IV and coordination)

## Common Pre-Submission Issues

### Issue: Coverage below 80%

**Solution**: Add missing tests before submitting
```bash
# Check coverage
pytest --cov=src

# Find untested lines
pytest --cov=src --cov-report=html
# Open htmlcov/index.html to see what's not covered
```

### Issue: Forgot to test database migration

**Solution**: Test migration locally
```bash
# Create migration
alembic revision --autogenerate -m "Add new column"

# Test migration forward
alembic upgrade head

# Test rollback
alembic downgrade -1
alembic upgrade head  # Should be idempotent
```

### Issue: API contract breaking change

**Solution**: Maintain backward compatibility
```python
# ❌ BAD: Removing field breaks clients
class Response(BaseModel):
    total_value: float
    # Removed: risk_score

# ✅ GOOD: Keep old field, add new optional field
class Response(BaseModel):
    total_value: float
    risk_score: float  # Keep for backward compat
    risk_level: str  # New field, more descriptive
```

### Issue: DECIMAL precision error

**Solution**: Use Decimal type, not float
```python
# ❌ BAD: Float precision errors
amount = 1.01 + 1.02  # Results in 2.0299999...

# ✅ GOOD: Use Decimal
from decimal import Decimal
amount = Decimal("1.01") + Decimal("1.02")  # Results in 2.03
```

## Help & Support

- **Governance questions**: Read principle-specific guides in `docs/governance/`
- **Code review feedback**: Ask reviewer to clarify
- **Test questions**: Ask tech lead or check pytest docs
- **Report issue**: Create GitHub issue or ask tech lead

## Estimated Checklist Time

- Principles review: 5 min
- Test coverage verify: 5 min
- Code review self-check: 5 min
- Full checklist: ~15 minutes

**Pro tip**: Do this checklist BEFORE you think your PR is ready, not after!

---

✅ Once all items checked, your PR is ready for review!

**Next**: Submit PR and expect governance review feedback.
