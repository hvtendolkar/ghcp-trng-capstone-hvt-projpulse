## Description

<!-- Describe what changed and why. Link to any related issues or tickets. -->

## Which Governance Principles Apply?

Mark which principles apply to this PR:

- [ ] **Principle I: AI-Driven Financial Intelligence**
  - Involves AI model inference, confidence scores, or decision logging
  - If checked: See [AI Code Developer Guide](../docs/governance/ai-code-developer-guide.md)

- [ ] **Principle II: Financial Data Integrity & Compliance**
  - Involves financial data, calculations, audit trails, or reconciliation
  - If checked: See [Financial Code Developer Guide](../docs/governance/financial-code-developer-guide.md)

- [ ] **Principle III: Scalable API-First Architecture**
  - Changes API contracts, database schema, or system architecture
  - If checked: See [Architecture Reviewer Guide](../docs/governance/architecture-reviewer-guide.md)

- [ ] **Principle IV: Test-Driven Development & Quality Gates** (applies to all code)
  - Includes unit tests, integration tests, and database tests where applicable
  - Target: 80% code coverage minimum

## Governance Checklist

### Pre-Review Automated Gates
- [ ] CI/CD checks passed (tests, linting, coverage)
- [ ] No merge conflicts
- [ ] Branch is up to date with main

### Principle I Checklist (if applicable)

- [ ] AI model used is documented (which model? which version?)
- [ ] Confidence score is calculated and available to calling code
- [ ] Decision reasoning/logic is logged for audit
- [ ] Model parameters are configurable (not hardcoded)

### Principle II Checklist (if applicable)

- [ ] Currency amounts use DECIMAL type (never float/double)
- [ ] Single source of truth maintained (no duplicate calculations)
- [ ] All financial transactions logged to audit trail (user, timestamp, amount, before/after state)
- [ ] Reconciliation process documented or updated
- [ ] Input validation present (range checks, currency validation)

### Principle III Checklist (if applicable)

- [ ] API request/response schemas documented (OpenAPI/Pydantic)
- [ ] Backward compatibility maintained (2+ major versions)
- [ ] Database schema changes use migrations (not direct changes)
- [ ] Foreign key constraints and data integrity enforced

### Principle IV Checklist (all code)

- [ ] Test coverage >= 80% for business logic
- [ ] Unit tests present for individual functions
- [ ] Integration tests present for full request/response flows
- [ ] Database tests present (if schema or transactions affected)
- [ ] Regression tests present (if bug fix: test fails before fix, passes after)

## Test Coverage

- Current coverage: [X]%
- Target: 80% minimum
- Coverage report: [Link if available]

## Deployment Notes

<!-- Describe any deployment considerations, database migrations, or runtime configuration changes. -->

## Related Issues/Tickets

Closes: #[issue]
Related to: #[issue]

---

## Before You Submit

Please complete the developer pre-PR checklist:
👉 [Developer Pre-PR Checklist](../docs/governance/developer-pre-pr-checklist.md)

Have questions about governance requirements?
👉 [FAQ](../docs/governance/FAQ.md)

---

**Reviewers**: Please verify governance compliance using the checklist above before approving.
