# Governance Reviewer Procedures

This guide explains how to enforce the governance framework during code review.

## Overview

As a reviewer, you're the gate that ensures all code meets governance principles before merge.

**Your responsibility**: Verify that PRs comply with the 4 governance principles and governance checklist before approving.

## Pre-Review Preparation

### 1. Understand the 4 Principles

Read the [Constitution](../../.specify/memory/constitution.md):
- **Principle I**: AI insights transparent, validated, auditable, configurable
- **Principle II**: Financial data precise, single source, auditable, reconciled, validated
- **Principle III**: Architecture stateless, contracts documented, modular, database integrity enforced
- **Principle IV**: Testing 80% coverage, unit + integration + database tests, manual review, regression prevention

### 2. Get the Review Checklist

Reference the general governance checklist from project contracts:
- Location: `specs/001-project-governance/contracts/general-governance-checklist.md`
- This is the authoritative list of items to verify during review

### 3. Check for Specialized Reviewers Needed

Some PRs require specialized review from domain experts:
- **Financial data changes** → Request financial domain expert review
- **AI feature changes** → Request AI systems reviewer
- **API/Architecture changes** → Request architecture owner review

## The Review Process

### Step 1: Read the PR Description

Check:
- [ ] PR author has completed the governance section of PR template
- [ ] PR author has marked which principles apply to this change
- [ ] PR author has referenced principle-specific requirements

### Step 2: Assess Which Principles Apply

Determine which governance principles are relevant:

| Change Type | Principle | Reviewer Responsibility |
|-------------|-----------|----------------------|
| Involves AI inference | I | Verify transparency, validation, auditability, configurability |
| Touches financial data | II | Verify DECIMAL precision, audit trail, reconciliation, validation |
| Changes API/database | III | Verify contracts, backward compatibility, schema integrity |
| Any code change | IV | Verify 80% test coverage, test types, quality |

### Step 3: Check General Governance Checklist

Use `specs/001-project-governance/contracts/general-governance-checklist.md`:

- [ ] **Pre-Review Automated Checks**: CI/CD passes (tests, linting, coverage)
- [ ] **Principle I Checklist** (if AI involved):
  - [ ] Model used is documented
  - [ ] Confidence score calculated and available
  - [ ] Reasoning/decision logged
  - All items checked?

- [ ] **Principle II Checklist** (if financial involved):
  - [ ] Currency precision: DECIMAL not float
  - [ ] Single source of truth: no duplicate calculations
  - [ ] Audit trail: all transactions logged
  - [ ] Reconciliation: process defined
  - [ ] Validation: input checks present
  - All items checked?

- [ ] **Principle III Checklist** (if API/database involved):
  - [ ] API contracts: documented in OpenAPI/Pydantic
  - [ ] Backward compatibility: maintained for 2+ versions
  - [ ] Database migrations: tested, with rollback plan
  - [ ] Schema integrity: constraints enforced
  - All items checked?

- [ ] **Principle IV Checklist** (all code):
  - [ ] Coverage: minimum 80% achieved
  - [ ] Unit tests: individual functions tested
  - [ ] Integration tests: full workflows tested
  - [ ] Database tests: (if applicable) migrations tested
  - [ ] Regression tests: (if bug fix) test fails before fix, passes after
  - All items checked?

### Step 4: Identify Violations

If any governance items are not checked:

**Minor issue** (≤ 1 item unchecked):
- Request changes from PR author
- Specify exactly what needs to be added/fixed
- Suggest principle-specific guide for reference

**Major issue** (2+ items unchecked or fundamental problem):
- Request changes
- Document the issue clearly
- Consider requesting specialized reviewer (financial expert, AI reviewer, architect)

### Step 5: Request Specialized Reviewers

If PR affects specialized areas:

**For Principle I (AI)**:
- [ ] Request AI systems reviewer
- [ ] Share principle-specific AI review guide
- [ ] Wait for AI reviewer approval

**For Principle II (Financial)**:
- [ ] Request financial domain expert
- [ ] Share principle-specific financial review guide  
- [ ] Wait for financial reviewer approval

**For Principle III (Architecture)**:
- [ ] Request architecture owner
- [ ] Share architecture review guide
- [ ] Wait for architecture reviewer approval

### Step 6: Request Changes

Format change requests clearly:

```
Governance Issue - [Principle #]: [Issue Name]

Violation: [Description of what doesn't meet governance requirement]
Principle Requirement: [Reference to relevant principle section]
Suggested Fix: [How to address this]

Severity: CRITICAL / MAJOR / MINOR

Link to principle guide: [Link to guide for this principle]
```

### Step 7: Approve PR

Once all governance items are checked:

```
✅ Governance Approval - [Principle/Principles]

This PR meets governance requirements for:
- Principle I (if applicable): ✅ / N/A
- Principle II (if applicable): ✅ / N/A
- Principle III (if applicable): ✅ / N/A
- Principle IV: ✅

Approved for merge.
```

## Common Governance Issues

### Principle I (AI) Issues
- **Missing confidence score**: AI output without confidence threshold
- **No audit logging**: AI decisions not logged for review
- **Hardcoded thresholds**: Model parameters not configurable
- **Undocumented model**: Model version or type not documented

### Principle II (Financial) Issues
- **Float for currency**: Using float/double instead of DECIMAL
- **Missing audit trail**: Financial transactions not logged
- **No reconciliation**: No process to verify calculations correct
- **Missing validation**: User input not checked before use

### Principle III (Architecture) Issues
- **API contract broken**: Response format changed without backward compatibility
- **Missing schema migration**: Direct database schema change instead of migration
- **Foreign key removed**: Database integrity constraint lost
- **Breaking change**: API endpoint changed in incompatible way

### Principle IV (Testing) Issues
- **Low coverage**: < 80% coverage for business logic
- **Missing integration tests**: Unit tests only, no full-flow testing
- **No database tests**: (if applicable) Schema migrations not tested
- **No regression test**: (if bug fix) Test doesn't verify bug is fixed

## Handling Disagreements

If PR author disagrees with your governance feedback:

1. **Clarify the requirement**: Point to specific principle text or guide
2. **Discuss options**: If requirement is unclear, discuss with tech lead
3. **Escalate if needed**: Ask tech lead to make final decision
4. **Document the discussion**: Add comments explaining rationale

## When to Escalate

Escalate to tech lead or CTO if:
- Governance requirement is unclear or ambiguous
- PR author requests exception to governance principle
- Multiple reviewers disagree on governance interpretation
- Critical violation found (CRITICAL severity)
- Amendment to governance seems needed

## Compliance Tracking

Your reviews contribute to compliance metrics:
- Each approved PR counts toward **SC-001** (100% of PRs reference governance principles)
- Your enforcement contributes to **SC-003** (95% PR compliance rate)
- Violations documented are tracked in monthly audits

## Support & Resources

- **Constitution**: [.specify/memory/constitution.md](../../.specify/memory/constitution.md)
- **Governance Checklist**: `specs/001-project-governance/contracts/general-governance-checklist.md`
- **Principle-Specific Guides**: `docs/governance/` (see AI, financial, architecture specific guides)
- **FAQ**: [docs/governance/FAQ.md](FAQ.md)
- **Questions**: Ask tech lead

---

Thank you for maintaining governance standards! Your review discipline ensures ProjectPulse AI stays compliant and maintainable. 🎯
