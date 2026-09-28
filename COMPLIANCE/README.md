# COMPLIANCE Directory

This directory contains governance compliance records, audit reports, and violation documentation for the ProjectPulse AI governance framework.

## Directory Structure

```
COMPLIANCE/
├── README.md                              # This file
├── team-governance-acknowledgment.csv     # Team member acknowledgment tracking
├── monthly-audits/                        # Monthly compliance audit records
│   ├── 2026-10-governance-audit.md       # October 2026 audit
│   ├── 2026-11-governance-audit.md       # November 2026 audit
│   └── ...
├── violations/                            # Governance violation records
│   ├── 2026-10-violation-001.md          # Violation found during audit
│   └── ...
└── [YYYY-MM-DD-]meeting-notes.md         # Training and meeting documentation
    ├── 2026-09-28-architecture-kickoff-notes.md
    ├── 2026-09-28-developer-tdd-training-notes.md
    └── ...
```

## Compliance Audit Structure

### Audit Records

Monthly compliance audit records are stored in `monthly-audits/` directory with filename pattern: `YYYY-MM-governance-audit.md`

**Audit Timing**: 
- Conducted during the first 5 business days of each month
- Audit period: Previous calendar month (e.g., October audit covers September PRs)
- Sample size: 5-10 random PRs from the audit period

**Sampling Methodology**:
- Deterministic random sampling using YYYYMM as seed (ensures reproducibility)
- Seed formula: `hash(YYYYMM) % total_prs_in_month = index` (adjustable for different sample sizes)
- Example: October 2026 audit uses seed 202610 to select random PRs from September

### Audit Contents

Each monthly audit includes:
- **Audit Date**: When the audit was conducted
- **Audit Period**: PRs merged during this period
- **Sample Details**: Which PRs were audited (5-10 random samples)
- **Governance Checklist**: Verification against 4 principles
- **Violations Found**: By principle and severity
- **Corrective Actions**: For each violation, required fix and timeline
- **Compliance Rate**: % of audited PRs meeting governance requirements
- **Audit Sign-Off**: Tech lead and governance owner approval

**Target Compliance Rate**: 95% of PRs meeting governance requirements

### Violation Tracking

#### Violation Records

Violations found during audit or code review are documented in `violations/` directory.

**Severity Levels**:
- **CRITICAL**: Governance violation that prevents PR merge or requires immediate corrective action (e.g., missing audit trail for financial transaction, float used for monetary amount)
- **MAJOR**: Significant governance issue that requires remediation within 2 weeks (e.g., insufficient test coverage, architectural contract broken)
- **MINOR**: Minor governance gap that should be addressed in future PRs (e.g., documentation incomplete, configuration not optimal)

**Violation Information**:
- Violation ID (VIOL-YYYY-MM-###)
- Principle affected (I/II/III/IV)
- PR number and link
- Violation description
- Impact assessment
- Corrective action required
- Timeline for remediation (typically 2-3 weeks for MAJOR violations)
- Status (Open / In Progress / Resolved / Waived)

#### Corrective Action Procedure

1. **Violation Found**: During audit or code review, violation documented
2. **Author Notification**: PR author notified of violation and required fix
3. **Remediation Window**: 2-3 weeks to implement corrective action
4. **Verification**: Tech lead verifies fix addresses violation
5. **Status Update**: Violation marked as Resolved
6. **Trend Analysis**: Audit procedure tracks violations by principle and severity

## Meeting Documentation

### Training Sessions

Training sessions and kickoff meetings are documented in meeting notes:
- `[YYYY-MM-DD]-[role]-training-notes.md`
- Example: `2026-09-28-developer-tdd-training-notes.md`

**Contents**:
- Date and time
- Attendees
- Principles covered
- Q&A summary
- Team commitments
- Next steps

### All-Hands Meetings

Project-wide governance ratification and status meetings:
- `[YYYY-MM-DD]-all-hands-governance-meeting-notes.md`
- Example: `2026-09-28-all-hands-governance-meeting-notes.md`

**Contents**:
- Ratification vote or adoption confirmation
- Questions and answers from team
- Commitments and timelines
- Acknowledgment form collection status

## Team Acknowledgment Tracking

**File**: `team-governance-acknowledgment.csv`

Tracks team member completion of governance acknowledgment form, confirming understanding of constitution and adoption of principles.

**Columns**:
- Name: Team member name
- Role: Developer / Reviewer / Architect / Finance / AI
- Date-Acknowledged: When acknowledgment form was submitted
- Constitution-Version: Constitution version acknowledged
- Acknowledged-Sections: Which principles confirmed understood
- Status: Complete / Pending / Escalated
- Notes: Any follow-up items

**30-Day Adoption Target**: All team members should complete acknowledgment within 30 days of governance ratification (by 2026-10-28)

## Compliance Dashboards

Monthly governance impact dashboard tracking key metrics:
- Overall PR compliance rate (target: 95%)
- Compliance by principle (I/II/III/IV)
- Violations found and remediated
- Team adoption rate
- Training completion rate

**Dashboard Updated**: Monthly, as part of audit completion

## Amendment Records

Approved amendments to the constitution are recorded in:
- `.specify/memory/constitution.md` - Amendment history in YAML frontmatter
- `.specify/memory/amendments/` - Individual amendment proposal files

Each approved amendment updates the constitution version and effective date.

## Regulatory Compliance

This directory maintains the compliance audit trail required for:
- Financial system governance (Big 4 audit readiness)
- Code review enforcement documentation
- Governance amendment tracking
- Team adoption and training records

**Retention Policy**: All compliance records retained for minimum 7 years (per financial audit requirements)

## Access Control

Compliance records should be accessible to:
- Tech Lead / Governance Owner
- CTO and Leadership
- Financial domain experts (for financial violations)
- AI systems reviewers (for AI violations)
- Architecture team (for architecture violations)

## Getting Help

- For questions about compliance audits, see `docs/governance/compliance-audit-procedures.md`
- For amendment procedures, see `docs/governance/amendment-process.md`
- For governance violations, see `.github/ISSUE_TEMPLATE/governance-violation.md` to report
