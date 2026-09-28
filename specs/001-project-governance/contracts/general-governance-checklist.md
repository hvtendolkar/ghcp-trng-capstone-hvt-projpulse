# PR Review Checklist: General Governance & Principles

**Status**: Reference document for all PR reviews

**Applied to**: All PRs submitted after constitution ratification

**Purpose**: Ensure all code contributions align with ProjectPulse AI constitution principles

## Pre-Review Checklist (Automated)

- [ ] **CI Pipeline Passes**: All automated tests passing (GitHub Actions)
- [ ] **Code Formatting**: Code style matches project standards (linting pass)
- [ ] **Secret Scanning**: No credentials or API keys in code (automated scan)
- [ ] **Test Coverage**: Business logic has minimum 80% coverage
- [ ] **Branch Protection**: PR created from feature branch to main/develop

## Constitution Principles Compliance

### Principle I: AI-Driven Financial Intelligence ✓ AI-Related Code

**Apply this section if PR modifies AI-related code or adds financial insights**

- [ ] **AI Transparency**: AI insights are clearly marked as "AI-generated" in response/UI
- [ ] **Confidence Levels**: Model confidence score is included with every insight
- [ ] **Reasoning Disclosed**: Decision reasoning or factors are logged/available
- [ ] **Fallback Logic**: Code includes fallback to rule-based analysis when AI confidence < threshold
- [ ] **Auditable Logging**: All AI decisions logged with:
  - [ ] Input parameters
  - [ ] Model version used
  - [ ] Confidence score
  - [ ] Timestamp
  - [ ] User/request ID
- [ ] **Configuration**: AI parameters (threshold, model version, timeout) are configurable and tracked
- [ ] **Mock Testing**: Before Gemma API integration, mock responses were tested

**Required Approver**: AI Systems Reviewer

---

### Principle II: Financial Data Integrity & Compliance ✓ Financial Code

**Apply this section if PR modifies financial calculations, data models, or audit trails**

- [ ] **Precision**: All currency amounts use DECIMAL type (PostgreSQL) or Decimal (Python), never float
- [ ] **Single Source of Truth**: Financial calculation has one authoritative endpoint; no duplicate logic
- [ ] **Immutable Audit Trail**: All data modifications logged including:
  - [ ] User who made change
  - [ ] Timestamp of change
  - [ ] Justification/reason
  - [ ] Pre-value and post-value
- [ ] **Audit Trail Storage**: Logs stored immutably (triggers, event sourcing, or append-only table)
- [ ] **Reconciliation**: If feature includes WIP/invoicing/revenue data:
  - [ ] Monthly reconciliation check logic implemented
  - [ ] Discrepancies trigger alerts/notifications
  - [ ] Reconciliation report generated and accessible
- [ ] **Input Validation**: API endpoint validates financial figures before storage:
  - [ ] No unvalidated amounts accepted
  - [ ] Error messages clear without exposing system details
- [ ] **Edge Cases Tested**: Test coverage includes:
  - [ ] Negative amounts (if applicable)
  - [ ] Rounding behavior (half-up, banker's rounding, etc.)
  - [ ] Currency conversion (if applicable)
  - [ ] Large numbers (millions/billions)

**Required Approver**: Financial Domain Expert

---

### Principle III: Scalable API-First Architecture ✓ API/Database Code

**Apply this section if PR modifies API endpoints, database schema, or service boundaries**

- [ ] **API Contracts**: Endpoint has documented OpenAPI/Pydantic schema
- [ ] **Request/Response Validation**: Both input and output validated against schema
- [ ] **Backward Compatibility**: Change maintains compatibility for 2+ previous minor versions
  - [ ] Deprecated fields marked with `@deprecated` in schema
  - [ ] Old request formats still accepted with migration path documented
  - [ ] Response format stable (no breaking changes to field types/names)
- [ ] **Database Integrity**: If schema changes:
  - [ ] Foreign key constraints enforced
  - [ ] Indexes created on searchable/filterable fields
  - [ ] Prepared statements used for all dynamic queries (no SQL injection risk)
- [ ] **Schema Migrations**: If database changes:
  - [ ] Migration script tested in isolation
  - [ ] Rollback procedure documented and tested
  - [ ] Migration can run without downtime (if production concern)
- [ ] **Modular Design**: Code organized by domain with clear boundaries:
  - [ ] Business logic separated from HTTP handlers
  - [ ] Data access abstracted from business logic
  - [ ] External services (Gemma AI, payment processors) abstracted behind interfaces

**Required Approver**: Architecture Owner

---

### Principle IV: Test-Driven Development & Quality Gates ✓ All Code

**Apply this section to all PRs**

- [ ] **Test Coverage**: Business logic has ≥80% coverage
  - [ ] Unit tests: fast, isolated, no external dependencies
  - [ ] Integration tests: happy path and error cases
  - [ ] Edge case tests: boundary conditions, error conditions
- [ ] **Integration Tests**: All API endpoints have tests for:
  - [ ] Happy path (success case)
  - [ ] Error paths (validation errors, not-found, permission denied)
  - [ ] Edge cases (empty input, max values, timeout scenarios)
- [ ] **Database Tests** (if schema changes):
  - [ ] Schema migration tested in isolation
  - [ ] Rollback tested and verified
  - [ ] Transaction rollback scenarios covered
- [ ] **AI Integration Tests** (if uses Gemma API):
  - [ ] Mock responses tested before real API integration
  - [ ] Timeout scenarios handled
  - [ ] Rate limiting respected
  - [ ] Retry logic implemented for transient failures
- [ ] **Bug Fix Tests**: If fixing a bug:
  - [ ] Test written that fails before fix, passes after fix
  - [ ] Test prevents regression if bug reoccurs
  - [ ] Root cause analyzed in commit message

**Required Approver**: Code Reviewer (but financial/AI code needs specialized approver)

---

## Review Process

1. **Automated checks must pass** (pre-flight gates)
2. **Developer completes this checklist** in PR description
3. **Code reviewers verify items** based on PR type:
   - All PRs: Principle IV (TDD)
   - Financial code: Add Principle II review
   - AI code: Add Principle I review
   - API/Database code: Add Principle III review
4. **Specialized reviewer approval** required:
   - Financial code: Financial Domain Expert must approve
   - AI code: AI Systems Reviewer must approve
   - Architecture changes: Architecture Owner must approve
5. **No merge until all gates pass**

---

## Violation Handling

- **Blocking violation** (blocks merge):
  - [ ] Insufficient test coverage
  - [ ] Missing audit trail for financial data
  - [ ] AI insights not marked as AI-generated
  - [ ] Currency amounts use float instead of DECIMAL
  - [ ] SQL injection vulnerability in database query

- **Major violation** (must fix before merge):
  - [ ] Missing edge case tests
  - [ ] Incomplete audit logging
  - [ ] Backward compatibility broken without deprecation path
  - [ ] Foreign key constraints missing

- **Minor violation** (advisory, document in PR):
  - [ ] Code style inconsistency
  - [ ] Unclear variable naming
  - [ ] Missing documentation comments

---

## References

- Full Constitution: [constitution.md](../../.specify/memory/constitution.md)
- Development Workflow: [constitution.md#development-workflow](../../.specify/memory/constitution.md)
- Amendment Process: [constitution.md#amendment-process](../../.specify/memory/constitution.md)
