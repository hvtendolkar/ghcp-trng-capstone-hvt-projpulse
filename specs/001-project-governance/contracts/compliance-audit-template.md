# Template: Monthly Governance Compliance Audit

**Audit ID**: AUDIT-YYYYMM (e.g., AUDIT-202609)

**Audit Month**: YYYY-MM (e.g., 2026-09)

**Audit Date**: [Date audit conducted]

**Auditor Name**: [Name/username of team member conducting audit]

---

## Audit Summary

**Period**: [Month start date] through [Month end date]

**Total PRs Merged**: [Count from GitHub]

**Sample Size**: [Number to audit = 5-10% of total PRs]

**Sample Selection Method**: Deterministic random sampling using date-based seed for reproducibility

---

## Sampling Method

Use this algorithm to select reproducible random sample:

```
1. List all merged PRs for the month in chronological order
2. Seed = hash(YYYYMM + "governance-audit") % total_prs
3. Interval = ceil(total_prs / sample_size)
4. Start = seed
5. For each index in start, start+interval, start+2*interval, ...:
   - Add PR at that index to audit sample
6. Continue until sample_size reached or end of month
```

**Seed Used**: [Document actual seed value for reproducibility]

**Interval Used**: [Interval for sampling]

**PRs Selected for Audit**:
- PR #[number]: [title]
- PR #[number]: [title]
- [etc.]

---

## Audit Results

### Overall Statistics

| Metric | Value |
|--------|-------|
| Total PRs Audited | [ ] |
| PRs Passing All Checks | [ ] |
| PRs with Violations | [ ] |
| Pass Rate | [ ]% |
| Critical Violations | [ ] |
| Major Violations | [ ] |
| Minor Violations | [ ] |

---

## Individual PR Audit Records

### PR #[NUMBER]: [TITLE]

**PR Details**:
- Merged date: [date]
- Author: [GitHub username]
- Code type: [ ] General [ ] Financial [ ] AI [ ] Database/API [ ] Multiple
- Lines changed: [approx count]

**Compliance Status**: [ ] PASS  [ ] FAIL

**Governance Checklist Items Verified**:

**General Principles (All PRs)**:
- [ ] PR has test coverage ≥80% for business logic
- [ ] All automated tests passing (CI/CD green)
- [ ] Code follows project style (linting pass)

**If Financial Code**:
- [ ] Currency amounts use DECIMAL type (verified in code review)
- [ ] Financial calculation has single authoritative source
- [ ] Audit trail logging implemented (all changes logged)
- [ ] Edge cases tested (negative, rounding, large numbers)

**If AI Code**:
- [ ] AI insights marked as AI-generated in output
- [ ] Confidence levels displayed to users
- [ ] Fallback logic present (rule-based when confidence low)
- [ ] AI decisions logged with parameters and timestamp
- [ ] Mock responses tested before real API integration

**If Database/API Code**:
- [ ] API contract documented (OpenAPI/Pydantic)
- [ ] Foreign keys enforced (if schema change)
- [ ] Prepared statements used (no SQL injection risk)
- [ ] Backward compatibility maintained

**Violations Found** (if FAIL):

| Violation | Principle | Severity | Details |
|-----------|-----------|----------|---------|
| [Violation description] | [Principle I/II/III/IV] | CRITICAL/MAJOR/MINOR | [Specific details and code reference] |
| [ ] | [ ] | [ ] | [ ] |

**Corrective Action Required**:
- [ ] No action required
- [ ] Guidance provided (advisory)
- [ ] Minor fix needed (minor violation)
- [ ] Significant rework required (major violation)
- [ ] Must revert PR (critical violation)

**Corrective Action Details**:
```
[Description of what needs to be fixed and why]
[Reference to specific code locations if applicable]
[Timeline for correction]
```

**Follow-up Date**: [Date by which corrective action must be completed]

---

### [Repeat Audit Record for each PR in sample]

---

## Violation Summary by Category

### Principle I: AI-Driven Financial Intelligence

| PR # | Violation | Severity | Status |
|------|-----------|----------|--------|
| [ ] | [ ] | [ ] | OPEN/RESOLVED |

**Total Principle I violations**: [ ]

---

### Principle II: Financial Data Integrity

| PR # | Violation | Severity | Status |
|------|-----------|----------|--------|
| [ ] | [ ] | [ ] | OPEN/RESOLVED |

**Total Principle II violations**: [ ]

---

### Principle III: Scalable API Architecture

| PR # | Violation | Severity | Status |
|------|-----------|----------|--------|
| [ ] | [ ] | [ ] | OPEN/RESOLVED |

**Total Principle III violations**: [ ]

---

### Principle IV: Test-Driven Development

| PR # | Violation | Severity | Status |
|------|-----------|----------|--------|
| [ ] | [ ] | [ ] | OPEN/RESOLVED |

**Total Principle IV violations**: [ ]

---

## Trends & Observations

**Violation Trends**:
- Most common violation category: [Principle X - describe]
- Recurring issues: [What types of issues appear repeatedly]
- Improvement areas: [Where to focus team coaching]

**Positive Observations**:
- Strengths in compliance: [What team is doing well]
- Teams with high compliance: [Teams consistently passing]

**Recommendations for Next Month**:
1. [Actionable recommendation based on audit findings]
2. [Recommendation to prevent violations]
3. [Process improvement suggestion]

---

## Corrective Action Follow-up

This section completed 2-3 weeks after initial audit, verifying that corrective actions were completed.

### Open Violations Status

| PR # | Violation | Original Due Date | Actual Resolution Date | Status |
|------|-----------|-------------------|----------------------|--------|
| [ ] | [ ] | [ ] | [ ] | RESOLVED/OVERDUE/WAIVED |

**Violations Resolved**: [ ] of [ ]

**Violations Overdue**: [ ]

**Notes on Overdue Items**:
```
[Explanation for any violations not resolved by due date]
[Plan to resolve overdue items]
```

---

## Audit Sign-Off

**Audit Conducted By**: [Name/username]

**Audit Completed Date**: [Date]

**Reviewed By**: [Architecture Lead or Governance Owner - name/username]

**Review Completed Date**: [Date]

**Approved**: [ ] Yes  [ ] No

**Approval Notes**: [If any concerns or special circumstances]

---

## Distribution

- [ ] Audit results shared with development team
- [ ] Audit results shared with project leadership
- [ ] Audit results archived in COMPLIANCE/monthly-audits/ directory
- [ ] Corrective action items added to backlog/project management
- [ ] Next audit scheduled for [Next month date]

---

## References

- Constitution: [.specify/memory/constitution.md](../../.specify/memory/constitution.md)
- General Governance Checklist: [general-governance-checklist.md](./general-governance-checklist.md)
- Data Model: [../data-model.md](../data-model.md)
