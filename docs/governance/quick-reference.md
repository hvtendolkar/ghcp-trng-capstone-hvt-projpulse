# Governance Quick Reference

## The 4 Core Principles

### I. AI-Driven Financial Intelligence
**Requirement**: AI insights must be transparent, validated, auditable, configurable
- Document the model used and version
- Calculate and expose confidence scores
- Log all AI decisions for audit
- Make model parameters adjustable (not hardcoded)

### II. Financial Data Integrity & Compliance
**Requirement**: Financial data must be precise, single-source, auditable, reconciled, validated
- Use DECIMAL for currency (never float/double)
- No duplicate financial calculations
- Log all transaction changes (who, when, what, why)
- Monthly reconciliation of calculations
- Validate all financial inputs

### III. Scalable API-First Architecture
**Requirement**: API contracts defined, backward compatible, modular design, database integrity
- Document all API schemas (OpenAPI/Pydantic)
- Maintain 2+ versions backward compatibility
- Use database migrations (not direct schema changes)
- Enforce foreign keys and integrity constraints

### IV. Test-Driven Development & Quality Gates
**Requirement**: 80% coverage, unit + integration + database tests, manual review gates
- Minimum 80% code coverage for business logic
- Unit tests for individual functions
- Integration tests for full workflows
- Database tests for migrations and transactions
- Regression tests for bug fixes

## Quick Links

| Resource | Link | Purpose |
|----------|------|---------|
| Constitution | [.specify/memory/constitution.md](../../.specify/memory/constitution.md) | Full governance document |
| Developer Onboarding | [docs/governance/developer-onboarding.md](developer-onboarding.md) | New developer guide |
| Reviewer Procedures | [docs/governance/reviewer-procedures.md](reviewer-procedures.md) | Code review guidance |
| Pre-PR Checklist | [docs/governance/developer-pre-pr-checklist.md](developer-pre-pr-checklist.md) | Self-check before submitting |
| Amendment Process | [docs/governance/amendment-process.md](amendment-process.md) | Propose constitution changes |
| Compliance Audits | [docs/governance/compliance-audit-procedures.md](compliance-audit-procedures.md) | Monthly audit procedures |
| FAQ | [docs/governance/FAQ.md](FAQ.md) | Common questions |
| Violations | [.github/ISSUE_TEMPLATE/governance-violation.md](../../.github/ISSUE_TEMPLATE/governance-violation.md) | Report governance issues |

## Key Contacts

- **Architecture Owner**: [To be assigned]
- **Financial Domain Expert**: [To be assigned]
- **AI Systems Reviewer**: [To be assigned]
- **Tech Lead / Governance Owner**: [To be assigned]

## Governance Timeline

| Event | Date | Deadline |
|-------|------|----------|
| Constitution Ratified | 2026-09-28 | — |
| Architecture Team Training | 2026-09-30 | — |
| Developer Team Training | 2026-10-01 | — |
| Leadership Briefing | 2026-10-02 | — |
| All-Hands Ratification Meeting | 2026-10-05 | — |
| 100% Team Acknowledgment Target | — | 2026-10-28 |
| First Compliance Audit | 2026-10-01 | 2026-10-05 |
| Monthly Audits | Every month | 1st-5th business days |

## Governance Terminology

| Term | Meaning |
|------|---------|
| **Constitution** | The governance framework document defining 4 core principles |
| **Principle** | One of 4 mandatory governance standards (I, II, III, IV) |
| **Compliance Audit** | Monthly review of random PRs to verify governance adherence |
| **Violation** | Code that doesn't meet governance requirements |
| **Amendment** | Proposed change to constitution (through formal approval process) |
| **Acknowledgment** | Team member confirms understanding of governance framework |
| **Coverage** | % of code lines executed by automated tests (target: 80%) |
| **Audit Trail** | Log of all financial transactions for compliance review |
| **API Contract** | Defined request/response format for API endpoints |

## Common File Paths

```
.github/GOVERNANCE.md                        # Main governance entry point
.github/pull_request_template.md             # PR template with governance checklist
.github/ISSUE_TEMPLATE/governance-violation.md  # Violation reporting template
.specify/memory/constitution.md              # Core governance document
.specify/memory/amendments/                  # Amendment proposals
docs/governance/                             # Governance guides and procedures
COMPLIANCE/                                  # Audit records and tracking
specs/001-project-governance/contracts/      # Review checklists and specifications
```

## Parallel Work (by Principle)

| Principle | Reviewer | Focus |
|-----------|----------|-------|
| I (AI) | AI Systems Reviewer | Transparency, validation, auditability, configurability |
| II (Financial) | Financial Domain Expert | DECIMAL precision, audit trail, reconciliation |
| III (Architecture) | Architecture Owner | API contracts, migrations, integrity constraints |
| IV (Testing) | Tech Lead | Coverage %, test types, regression tests |

*Reviewers can work in parallel!*

## When to Ask for Help

| Situation | Who to Ask | How |
|-----------|-----------|-----|
| Governance question | Tech Lead | Slack/email |
| Specific principle unclear | Domain Expert | Slack/email or training |
| How to implement principle | Principle-specific guide | Read docs/governance/ |
| Governance violation found | Tech Lead | Create GitHub issue |
| Propose amendment | Tech Lead | Submit amendment proposal |
| Report audit finding | Tech Lead | Compliance audit procedures |

## One-Minute Cheat Sheet

**Before Writing Code**:
1. Which principles apply? → Read constitution sections
2. What's required? → Read principle-specific guide

**While Coding**:
1. Follow principle requirements
2. Write tests as you code (TDD)
3. Use DECIMAL for money, log AI decisions, document APIs

**Before Submitting PR**:
1. Use pre-PR checklist → [Developer Pre-PR Checklist](developer-pre-pr-checklist.md)
2. Verify 80% coverage
3. Mark which principles apply in PR template

**During Code Review**:
1. Check governance checklist
2. Request specialized reviewers if needed
3. Document any violations

**Each Month**:
1. Compliance audit (first 5 business days)
2. Update dashboard metrics
3. Remediate any violations found

---

**Last Updated**: 2026-09-28

For more details, see full [Constitution](../../.specify/memory/constitution.md)
