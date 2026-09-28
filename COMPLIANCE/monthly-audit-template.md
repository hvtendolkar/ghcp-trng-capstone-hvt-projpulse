# Monthly Governance Audit Report Template

**Audit Period**: [YYYY-MM]

**Report Date**: [YYYY-MM-DD]

---

## Audit Metadata

- **Audit Period**: [E.g., September 2026 (2026-09-01 to 2026-09-30)]
- **Report Prepared**: [Date report created]
- **Lead Auditor**: [Name]
- **Principle Reviewers**: 
  - Principle I (AI): [Name]
  - Principle II (Financial): [Name]
  - Principle III (Architecture): [Name]
  - Principle IV (Testing): [Name]
- **Total PRs Merged in Period**: [X PRs]
- **Sample Size**: [X PRs selected for audit]
- **Sampling Seed**: [YYYYMM]
- **Sampling Algorithm**: Deterministic random (details in [compliance-audit-procedures.md](compliance-audit-procedures.md))

---

## Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| **Compliance Rate** | [X]% | ✅ PASS / ⚠️ CAUTION / ❌ FAIL |
| **PRs Audited** | [X] | — |
| **Violations Found** | [X] | — |
| **CRITICAL Violations** | [X] | — |
| **MAJOR Violations** | [X] | — |
| **MINOR Violations** | [X] | — |
| **All Violations Resolved** | Yes / No | — |

**Compliance Target**: 95% or higher

---

## Compliance by Principle

### Principle I: AI-Driven Financial Intelligence

| Aspect | Status | Notes |
|--------|--------|-------|
| Model Documentation | ✅/⚠️/❌ | [Notes] |
| Confidence Scores | ✅/⚠️/❌ | [Notes] |
| Audit Logging | ✅/⚠️/❌ | [Notes] |
| Parameter Configurability | ✅/⚠️/❌ | [Notes] |

**AI Compliance Rate**: [X]% of audited AI PRs compliant

### Principle II: Financial Data Integrity & Compliance

| Aspect | Status | Notes |
|--------|--------|-------|
| DECIMAL Usage | ✅/⚠️/❌ | [Notes] |
| Single Source of Truth | ✅/⚠️/❌ | [Notes] |
| Audit Trail Logging | ✅/⚠️/❌ | [Notes] |
| Input Validation | ✅/⚠️/❌ | [Notes] |
| Reconciliation Process | ✅/⚠️/❌ | [Notes] |

**Financial Compliance Rate**: [X]% of audited financial PRs compliant

### Principle III: Scalable API-First Architecture

| Aspect | Status | Notes |
|--------|--------|-------|
| API Contract Documentation | ✅/⚠️/❌ | [Notes] |
| Backward Compatibility | ✅/⚠️/❌ | [Notes] |
| Database Migrations | ✅/⚠️/❌ | [Notes] |
| Constraint Enforcement | ✅/⚠️/❌ | [Notes] |

**Architecture Compliance Rate**: [X]% of audited architecture PRs compliant

### Principle IV: Test-Driven Development & Quality Gates

| Aspect | Status | Notes |
|--------|--------|-------|
| Coverage >= 80% | ✅/⚠️/❌ | [Notes] |
| Unit Tests Present | ✅/⚠️/❌ | [Notes] |
| Integration Tests | ✅/⚠️/❌ | [Notes] |
| Database Tests | ✅/⚠️/❌ | [Notes] |
| Regression Tests | ✅/⚠️/❌ | [Notes] |

**Testing Compliance Rate**: [X]% of audited PRs meet testing requirements

---

## Audited PRs

### PR Summary Table

| # | PR | Author | Principles | Status | Issues |
|---|----|----|------------|--------|--------|
| 1 | #[PR] | [Author] | [I/II/III/IV] | ✅/❌ | [Count] |
| 2 | #[PR] | [Author] | [I/II/III/IV] | ✅/❌ | [Count] |
| 3 | #[PR] | [Author] | [I/II/III/IV] | ✅/❌ | [Count] |
| ... | ... | ... | ... | ... | ... |

### Detailed PR Findings

#### PR #[Number]: [Title]

**Metadata**:
- Author: [Name]
- Merged Date: [Date]
- Principles Involved: [I/II/III/IV]

**Governance Checklist Results**:

**Principle I** (if applicable):
- [ ] Model documented: ✅/❌
- [ ] Confidence scores: ✅/❌
- [ ] Audit logging: ✅/❌
- [ ] Configurable parameters: ✅/❌
- Notes: [Any issues found]

**Principle II** (if applicable):
- [ ] DECIMAL usage: ✅/❌
- [ ] Single source of truth: ✅/❌
- [ ] Audit trail: ✅/❌
- [ ] Input validation: ✅/❌
- Notes: [Any issues found]

**Principle III** (if applicable):
- [ ] API contracts: ✅/❌
- [ ] Backward compatibility: ✅/❌
- [ ] Database migrations: ✅/❌
- [ ] Constraints: ✅/❌
- Notes: [Any issues found]

**Principle IV** (always):
- [ ] Coverage >= 80%: ✅/❌ (Actual: [X]%)
- [ ] Unit tests: ✅/❌
- [ ] Integration tests: ✅/❌
- [ ] Database tests: ✅/❌
- [ ] Regression tests: ✅/❌ (if applicable)
- Notes: [Any issues found]

**Overall Assessment**: ✅ PASS / ❌ FAIL

---

## Violations Found

### CRITICAL Violations

| ID | PR | Principle | Description | Evidence | Impact | Resolution | Timeline |
|----|----|-----------|-------------|----------|--------|------------|----------|
| VIOL-YYYY-MM-001 | #[PR] | [I/II/III/IV] | [What was wrong] | [Code example] | [Why matters] | [How to fix] | Immediate |

### MAJOR Violations

| ID | PR | Principle | Description | Evidence | Impact | Resolution | Timeline |
|----|----|-----------|-------------|----------|--------|------------|----------|
| VIOL-YYYY-MM-002 | #[PR] | [I/II/III/IV] | [What was wrong] | [Code example] | [Why matters] | [How to fix] | 2 weeks |

### MINOR Violations

| ID | PR | Principle | Description | Evidence | Impact | Resolution | Timeline |
|----|----|-----------|-------------|----------|--------|------------|----------|
| VIOL-YYYY-MM-003 | #[PR] | [I/II/III/IV] | [What was wrong] | [Code example] | [Why matters] | [How to fix] | Current sprint |

---

## Violation Corrective Actions

### Outstanding Violations

| ID | Status | Author | Target Date | Plan | Progress |
|----|----|--------|-------------|------|----------|
| VIOL-YYYY-MM-001 | ⏳ In Progress | [Name] | [Date] | [What will fix it] | [% complete] |
| VIOL-YYYY-MM-002 | ⏳ In Progress | [Name] | [Date] | [What will fix it] | [% complete] |

### Resolved Since Last Audit

| ID | Status | Author | Resolved Date | Resolution |
|----|--------|--------|---------------|------------|
| [Previous] | ✅ Resolved | [Name] | [Date] | [Summary] |

---

## Compliance Trends

### Month-to-Month Comparison

| Month | Compliance Rate | Trend | Status |
|-------|---|---|---|
| [M-3] | [X]% | — | ✅/⚠️/❌ |
| [M-2] | [X]% | [↑/↓] | ✅/⚠️/❌ |
| [M-1] | [X]% | [↑/↓] | ✅/⚠️/❌ |
| [Current] | [X]% | [↑/↓] | ✅/⚠️/❌ |

**Trend Analysis**: [Are we improving? Declining? Stable?]

### Violations by Principle (Cumulative)

| Principle | Month | Total | Trend |
|-----------|-------|-------|-------|
| I (AI) | [M-1] | [X] | [↑/↓] |
| I (AI) | [Current] | [X] | [↑/↓] |
| II (Financial) | [M-1] | [X] | [↑/↓] |
| II (Financial) | [Current] | [X] | [↑/↓] |
| III (Architecture) | [M-1] | [X] | [↑/↓] |
| III (Architecture) | [Current] | [X] | [↑/↓] |
| IV (Testing) | [M-1] | [X] | [↑/↓] |
| IV (Testing) | [Current] | [X] | [↑/↓] |

**Analysis**: [Which principles improving? Which need focus?]

### Violations by Team (Current Month)

| Team | Members | Violations | Rate | Trend |
|------|---------|-----------|------|-------|
| Architecture | [N] | [X] | [X]% | [↑/↓] |
| Development | [N] | [X] | [X]% | [↑/↓] |
| Finance | [N] | [X] | [X]% | [↑/↓] |
| AI | [N] | [X] | [X]% | [↑/↓] |

**Analysis**: [Which teams need additional support?]

---

## Root Cause Analysis

### Key Findings

1. **Finding 1**: [What pattern did we notice?]
   - Affected PRs: [#PR, #PR]
   - Principle: [I/II/III/IV]
   - Root Cause: [Why is this happening?]
   - Recommended Action: [Training? Process change? Clarification?]

2. **Finding 2**: [What pattern did we notice?]
   - Affected PRs: [#PR, #PR]
   - Principle: [I/II/III/IV]
   - Root Cause: [Why is this happening?]
   - Recommended Action: [Training? Process change? Clarification?]

### Areas of Strength

- [What went well?]
- [What improved since last month?]
- [Best examples of governance compliance?]

### Areas for Improvement

- [What needs focus?]
- [What's the biggest gap?]
- [Where can we improve most?]

---

## Corrective Action Plan

**If compliance >= 95%**: ✅ Maintain current standards

**If 90% <= compliance < 95%**: ⚠️ Monitor closely, increase vigilance

**If compliance < 90%**: ❌ Implement corrective actions

### Recommended Actions

1. **Action 1**: [What should we do?]
   - Owner: [Who?]
   - Timeline: [When?]
   - Success Metric: [How do we know it worked?]

2. **Action 2**: [What should we do?]
   - Owner: [Who?]
   - Timeline: [When?]
   - Success Metric: [How do we know it worked?]

### Next Audit Focus

Areas to particularly focus on in next audit:
- [Principle/area 1]
- [Principle/area 2]
- [Teams/people to spot-check]

---

## Approval & Sign-Off

### Audit Approval

- **Lead Auditor**: _________________________ Date: _________
- **Tech Lead**: _________________________ Date: _________
- **Governance Owner**: _________________________ Date: _________

### Executive Summary for Leadership

**Status**: ✅ COMPLIANT / ⚠️ CAUTION / ❌ NON-COMPLIANT

**Headline**: [One-sentence summary of compliance status]

**Key Metrics**:
- Compliance Rate: [X]% (Target: 95%)
- PRs Audited: [X]
- Violations Found: [X]
- All Critical Violations Resolved: Yes/No

**Key Risks** (if any): [What should leadership know?]

**Next Steps**: [What happens next?]

---

## Document Information

- **Template Version**: 1.0
- **Report Document**: `COMPLIANCE/monthly-audits/[YYYY-MM]-governance-audit.md`
- **Previous Audit**: [Link to previous month report]
- **Next Audit Scheduled**: [Date for next month]

---

**End of Report**

For detailed procedures, see [compliance-audit-procedures.md](compliance-audit-procedures.md)
