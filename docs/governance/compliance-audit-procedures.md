# Compliance Audit Procedures

This guide explains how to conduct monthly compliance audits of governance adherence.

## Overview

**Compliance audits verify** that code merged into main branch meets governance principles.

- **Frequency**: Monthly, first 5 business days of following month
- **Audit Period**: Previous calendar month (e.g., October audit = September PRs)
- **Sample Size**: 5-10 random PRs from audit period
- **Target**: 95% compliance rate

## Pre-Audit Preparation

### 1. Set Audit Date

Schedule audit for first 5 business days of month following audit period:
- October 2026 audit: October 1-5 (audits September PRs)
- November 2026 audit: November 1-5 (audits October PRs)

### 2. Get Audit Template

Location: `COMPLIANCE/monthly-audits/YYYY-MM-governance-audit-template.md`

Copy template to `COMPLIANCE/monthly-audits/YYYY-MM-governance-audit.md`

### 3. Gather Team

Audit team should include:
- **Lead Auditor**: Tech Lead or Governance Owner
- **Principle Reviewers**: Domain experts for each principle
  - Principle I (AI) → AI Systems Reviewer
  - Principle II (Financial) → Financial Domain Expert
  - Principle III (Architecture) → Architecture Owner
  - Principle IV (Testing) → Development Lead

### 4. Identify PR Population

Get list of all PRs merged during audit period:
- Query GitHub: merged PRs in date range
- Example: `is:pr is:merged merged:2026-09-01..2026-09-30`

**Count total PRs** in audit period for sampling calculations

## Sampling Methodology

### Deterministic Random Sampling

Use **deterministic random sampling** to select audit sample:

**Algorithm**:
```
seed = YYYYMM (e.g., 202609 for September audit)
sample_size = 5 to 10 PRs (configurable)
total_prs_merged = [count from GitHub query]
index = (seed hash) % total_prs_merged
select PR at index + subsequent (sample_size - 1) PRs
```

**Why deterministic?**
- Reproducible: Same seed always produces same sample
- Verifiable: Anyone can recalculate and verify sample selection
- Unbiased: Random but not truly random (prevents gaming)

**Example**:
- September 2026 audit: seed = 202609
- 43 PRs merged in September
- Hash(202609) = 12345 (example)
- 12345 % 43 = 15
- Sample: PRs 15, 16, 17, 18, 19 (5-PR sample starting at index 15)

### Sample Selection Process

1. Get all merged PRs for audit period from GitHub
2. Sort PRs by number (ascending)
3. Calculate starting index using seed algorithm
4. Select 5-10 consecutive PRs starting from calculated index
5. Document sample selection in audit report

## The Audit Process

### Step 1: PR Overview

For each sampled PR:
- [ ] PR number and title
- [ ] Merge date
- [ ] PR author(s)
- [ ] Files modified
- [ ] Governance principles involved

### Step 2: Governance Checklist

Apply general governance checklist to each PR:

Reference: `specs/001-project-governance/contracts/general-governance-checklist.md`

**Pre-Review Checks**:
- [ ] CI/CD passed at merge time
- [ ] PR description filled out
- [ ] Governance section completed

**Principle I (AI) - if applicable**:
- [ ] Model used documented
- [ ] Confidence score calculated/available
- [ ] Reasoning/decisions logged
- [ ] Parameters configurable

**Principle II (Financial) - if applicable**:
- [ ] Currency uses DECIMAL (not float)
- [ ] Single source of truth maintained
- [ ] Audit trail logging present
- [ ] Reconciliation process defined
- [ ] Input validation present

**Principle III (Architecture) - if applicable**:
- [ ] API contracts documented/maintained
- [ ] Backward compatibility 2+ versions
- [ ] Database migrations used (not direct changes)
- [ ] Schema integrity/constraints enforced

**Principle IV (Testing) - always applicable**:
- [ ] Test coverage >= 80%
- [ ] Unit tests present
- [ ] Integration tests present
- [ ] Database tests (if applicable)
- [ ] Regression tests (if bug fix)

### Step 3: Violation Documentation

For each violation found:

**Violation Record** (in audit report):
- Violation ID: VIOL-YYYY-MM-###
- Principle: (I/II/III/IV)
- PR number
- Description: What governance requirement was not met?
- Evidence: Code snippet or example
- Severity: CRITICAL / MAJOR / MINOR
- Corrective Action: How to fix this?
- Timeline: When should fix be complete? (CRITICAL: immediate, MAJOR: 2 weeks, MINOR: next sprint)

### Step 4: Severity Assessment

**CRITICAL** - Prevents PR merge or enables significant risk
- Examples: Float used for currency, missing audit trail, broken API contract, zero test coverage
- Timeline: Immediate correction required (before next PR merge)
- Next Action: Create GitHub violation issue, author corrects immediately

**MAJOR** - Significant governance gap requiring remediation
- Examples: Insufficient coverage (< 80%), missing integration tests, inadequate validation
- Timeline: Corrective action within 2 weeks
- Next Action: Create GitHub violation issue, author plans remediation

**MINOR** - Minor gap to address in future PRs
- Examples: Documentation incomplete, configuration not optimal, edge case not tested
- Timeline: Corrective action within current sprint
- Next Action: Document in audit, author addresses in next opportunity

## Compliance Rate Calculation

**Compliance Rate** = (Audited PRs meeting all requirements / Total Audited PRs) × 100

**Target**: >= 95% compliance

**Examples**:
- 10 PRs audited, 10 meet requirements → 100% (✅ PASS)
- 10 PRs audited, 9 meet requirements → 90% (✅ PASS, but approaching target)
- 10 PRs audited, 8 meet requirements → 80% (❌ FAIL)

**Action if compliance < 95%**:
1. Identify common violations (which principle? which teams?)
2. Root cause analysis: Why are violations occurring?
3. Corrective action plan (training? process change? tools?)
4. Follow-up audit in 2 weeks to verify improvement

## Corrective Action Procedure

### For CRITICAL Violations

1. **Immediate**: Create GitHub issue with `governance-violation` template
2. **Author notification**: Flag PR author immediately with escalation
3. **Remediation**: Author corrects within 24-48 hours
4. **Verification**: Tech lead verifies fix
5. **Re-audit**: Include fixed code in quick re-check

### For MAJOR Violations

1. **Create GitHub issue**: Use `governance-violation` template
2. **Timeline**: Author has 2 weeks to implement corrective action
3. **Planning**: Author documents fix plan in violation issue
4. **Midpoint check** (1 week): Verify progress toward fix
5. **Verification**: Tech lead verifies corrective action complete
6. **Closure**: Mark violation as Resolved

### For MINOR Violations

1. **Document in audit**: Note in audit report
2. **Timeline**: Address in current sprint
3. **No GitHub issue needed** unless pattern emerges
4. **Next PR**: Expect this addressed in similar future code

## Post-Audit Compliance Dashboard

Once audit complete, update compliance dashboard (monthly):

**File**: `COMPLIANCE/[YYYY-MM-governance-audit.md]` (section: compliance summary)

| Metric | Value | Status |
|--------|-------|--------|
| PRs Audited | 10 | — |
| Compliance Rate | 95% | ✅ PASS |
| Violations Found | 1 MAJOR | — |
| Violations Remediated | 0 | — |
| Violations Outstanding | 1 | — |

**Principle Breakdown**:
- Principle I: 100% (all 2 AI PRs compliant)
- Principle II: 100% (all 3 financial PRs compliant)
- Principle III: 90% (8/10 architecture PRs compliant, 1 MAJOR)
- Principle IV: 100% (all 10 PRs meet coverage)

## Audit Report

### Report Components

**File**: `COMPLIANCE/monthly-audits/YYYY-MM-governance-audit.md`

1. **Audit Metadata**:
   - Audit date and period
   - Audit team members
   - Sample selection method and results

2. **Summary**:
   - Overall compliance rate
   - Violations by principle
   - Violations by severity
   - Key findings

3. **Detailed Findings**:
   - For each audited PR: Checklist results
   - For each violation: Description, evidence, corrective action

4. **Corrective Action Summary**:
   - Violations outstanding (with timeline)
   - Violations resolved since last audit
   - Follow-up audit date (if needed)

5. **Sign-Off**:
   - Lead Auditor approval
   - Tech Lead approval
   - CTO visibility

## Audit Sign-Off Template

```markdown
## Audit Approval & Sign-Off

**Lead Auditor**: [Name], [Date]
**Tech Lead**: [Name], [Date]
**Governance Owner**: [Name], [Date]

✅ Audit complete and verified
Target compliance (95%) met: YES / NO
Outstanding issues: [Count and summary]
Next audit scheduled: [Date]
```

## Communication & Escalation

### Monthly Compliance Report

After each audit:
1. **All-hands summary** (email/meeting): Key findings and trends
2. **Team leads** (email): Violations affecting their teams
3. **GitHub issues**: Violation issues for tracking
4. **Dashboard**: Update month-to-date metrics

### Escalation Criteria

Escalate to CTO if:
- Compliance rate drops below 90%
- CRITICAL violations found
- Same team/author has repeated violations
- Pattern indicates process breakdown
- Amendment to governance seems needed

## Tools & Resources

- **GitHub query**: `is:pr is:merged merged:YYYY-MM-01..YYYY-MM-31`
- **Audit checklist**: `specs/001-project-governance/contracts/general-governance-checklist.md`
- **Violation template**: `.github/ISSUE_TEMPLATE/governance-violation.md`
- **Audit template**: `COMPLIANCE/monthly-audits/audit-template-filled.md` (example from first audit)

## FAQ: Audits

**Q: How many PRs should I audit?**
A: 5-10 depending on monthly PR volume. Larger teams: 10 PRs. Smaller teams: 5 PRs.

**Q: What if audit shows 100% compliance?**
A: Great! Report positive outcome. Continue monitoring. No corrective actions needed.

**Q: What if a violation is too old to fix?**
A: Violations are fixed going forward. Past violations noted in audit but not retroactively corrected (unless they represent ongoing pattern).

**Q: Can I audit more than the random sample?**
A: Yes, but focus on random sample for objective measurement. Can supplement with targeted audits of high-risk areas.

**Q: Who approves violations as "resolved"?**
A: Tech Lead or Governance Owner verifies corrective action complete before marking Resolved.

---

**First Audit**: October 1-5, 2026 (audits September PRs)

For help with audits, contact Tech Lead or Governance Owner.
