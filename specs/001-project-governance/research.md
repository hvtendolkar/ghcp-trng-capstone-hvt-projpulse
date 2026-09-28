# Research: Project Governance Framework

**Phase**: Phase 0 (Research & Clarification)

**Created**: 2026-09-28

**Purpose**: Resolve unknowns from Technical Context and provide research-backed decisions for implementation planning

## Clarifications Resolved

### 1. Governance Document Format and Versioning

**Question**: How should the constitution document be versioned and updated?

**Research**:
- Constitution exists as `.specify/memory/constitution.md` (markdown format)
- Versioning specified in constitution: MAJOR (principle removal), MINOR (new principles), PATCH (clarifications)
- Amendment process requires: written justification, impact analysis, migration plan, approval from tech lead + domain expert
- Timeline: amendments should take no longer than 2 weeks

**Decision**: Use semantic versioning in constitution header with amendment log
- Constitution version tracked in YAML frontmatter: `version: 1.0.0`
- Amendment history maintained in separate `amendments/` directory in `.specify/memory/`
- Each amendment documented with proposal date, approver, effective date, and rationale

**Rationale**: Semantic versioning enables teams to reference specific constitution versions; amendment log provides traceability for governance changes

**Alternatives Considered**:
- Git commit history as version source: rejected because non-developers may not understand commit SHAs
- Separate versioning file: rejected because YAML frontmatter is standard for project documentation

---

### 2. PR Review Checklist Implementation

**Question**: How should governance principles be enforced during PR review?

**Research**:
- GitHub supports PR templates with checkboxes (markdown formatted)
- PR templates can be stored in `.github/pull_request_template.md` or `.github/PULL_REQUEST_TEMPLATE/`
- Templates can reference external documents and include conditional sections based on PR labels
- GitHub branch protection rules can require PR approval before merge; cannot directly enforce checklist completion but can be enforced via automation

**Decision**: Create multi-tier review checklist:
1. **Automated pre-flight checklist** (GitHub Actions): checks test coverage, code formatting, security scanning
2. **Reviewer checklist** (PR template): governance principle review items
3. **Specialized reviewer gates** (branch protection): financial code requires financial-domain reviewer; AI code requires AI systems reviewer

**Rationale**: Layered approach catches issues early (automated) while ensuring human expertise validates compliance (specialized reviewers)

**Alternatives Considered**:
- Single automated policy enforcement: rejected because governance principles include subjective judgment (e.g., "clearly marked as AI-generated")
- Entirely manual enforcement: rejected because error-prone and inconsistent

---

### 3. Monthly Compliance Audit Procedure

**Question**: How should monthly compliance audits be conducted and documented?

**Research**:
- Specification requires: monthly audit of 5-10% random sample of merged PRs
- Audit should document: compliance status, any violations, corrective actions
- Violations should include: which principle violated, PR number, severity, corrective action taken

**Decision**: Create audit procedure with:
- Random sampling algorithm (deterministic using date-based seed for reproducibility)
- Audit checklist template referencing constitution principles
- Audit record format: `COMPLIANCE/monthly-audits/YYYYMM-governance-audit.md`
- Automated report generation showing: total PRs merged, sample size, violations found, violation categories

**Rationale**: Structured audit procedure ensures consistency; audit records provide historical governance compliance data; automated sampling removes bias

**Alternatives Considered**:
- Continuous automated enforcement: rejected because constitutional compliance includes subjective judgment
- Quarterly audits: rejected because monthly cadence enables faster corrective action

---

### 4. AI Integration Governance Checklist

**Question**: What specific governance checks apply to AI integration PRs?

**Research**:
- Constitution Principle I defines: transparency (AI marking, confidence levels, reasoning), validation (fallback rules), auditability (decision logging), configurability (parameter tracking)
- ProjectPulse AI uses Gemma AI engine with fallback to rule-based analysis
- Confidence threshold and fallback behavior should be configurable

**Decision**: Create AI integration checklist:
- [ ] AI insights marked as AI-generated in UI/API response
- [ ] Confidence level displayed to user with explanation
- [ ] Reasoning for AI decision is documented/logged
- [ ] Fallback to rule-based analysis when confidence < threshold
- [ ] All AI decisions logged with: timestamp, input parameters, model version, confidence score, decision
- [ ] AI model parameters tracked and versioned for replay capability
- [ ] Mock responses tested before real Gemma API integration

**Rationale**: Specific checklist items translate constitutional principles into verifiable PR review criteria

---

### 5. Financial Data Integrity Governance Checklist

**Question**: What specific governance checks apply to financial code PRs?

**Research**:
- Constitution Principle II defines: single source of truth, immutable audit trail, precision (DECIMAL type), reconciliation, input validation
- Financial calculations are business-critical; errors directly impact Big 4 firm decisions

**Decision**: Create financial data integrity checklist:
- [ ] Currency amounts use DECIMAL type (PostgreSQL) or Decimal (Python), not float
- [ ] Calculation has single authoritative endpoint (no duplicate logic in multiple places)
- [ ] All financial data modifications logged: user, timestamp, justification, pre/post values
- [ ] Audit trail immutable (use PostgreSQL triggers or event sourcing)
- [ ] Monthly reconciliation checks implemented: WIP vs. invoicing vs. revenue recognition
- [ ] Input validation at API boundary: no unvalidated financial figures stored
- [ ] Edge cases tested: negative amounts, rounding, currency conversion, large numbers
- [ ] Financial-domain reviewer approval required before merge

**Rationale**: Specific checklist ensures financial code meets constitutional integrity standards; required reviewer approval adds human expertise layer

---

## Decisions Summary

| Area | Decision | Rationale |
|------|----------|-----------|
| Document Format | Markdown in `.specify/memory/constitution.md` with YAML versioning | Standard format, version tracking, amendment history |
| Enforcement | Multi-tier (automated pre-flight + reviewer checklist + specialized gates) | Catches issues early; ensures human expertise for judgment calls |
| Audits | Monthly sampling (5-10%) with structured records and automated reporting | Consistent, reproducible, provides historical compliance data |
| AI Checklist | Specific verification items for transparency, validation, auditability, configurability | Enables consistent AI integration reviews |
| Financial Checklist | Specific verification items for precision, auditability, reconciliation, validation | Prevents costly reconciliation bugs; requires domain expertise |

## Implementation Dependencies

None of the Phase 0 research findings require external libraries or infrastructure changes. All decisions are based on GitHub's native features and markdown documentation practices.

## Ready for Phase 1

✅ All technical context items clarified

✅ Constitution Check passed

✅ Research findings enable Phase 1 design artifacts
