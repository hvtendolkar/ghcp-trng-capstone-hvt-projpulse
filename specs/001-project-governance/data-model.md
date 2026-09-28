# Data Model: Project Governance Framework

**Phase**: Phase 1 (Design)

**Created**: 2026-09-28

**Purpose**: Define the governance entities, relationships, and data structures needed to implement the governance framework

## Core Governance Entities

### 1. Constitution Document

**What it represents**: The authoritative governance document defining mandatory principles, technology stack, and development workflow

**Attributes**:
- `version` (string, semantic versioning): Current version (e.g., "1.0.0")
- `ratified_date` (date): When constitution was ratified and became effective
- `last_amended_date` (date): Date of most recent amendment
- `core_principles` (array of Principle objects): 4+ mandatory principles defining project governance
- `technology_stack` (object): Required technologies and versions
- `development_workflow` (array of Stage objects): Development stages with gates and reviewer requirements
- `governance_section` (object): Amendment process, compliance review, version bumping rules

**Relationships**:
- Referenced by all PRs during review (compliance verification)
- Updated through amendment process (AmendmentProposal → Amendment)

**Validation Rules**:
- Version must follow MAJOR.MINOR.PATCH format
- Core principles must include: AI-Driven Insights, Data Integrity, API Architecture, TDD/Quality Gates
- Each principle must have: name, description, rationale, required constraints
- Technology stack must specify: languages, versions, databases, AI services
- Development workflow must include: Planning, Implementation, Testing, Review, Deployment stages
- Each stage must specify: required gates, reviewer roles, approval requirements

---

### 2. Core Principle

**What it represents**: A mandatory constraint that governs all ProjectPulse AI development work

**Attributes**:
- `name` (string): Principle name (e.g., "AI-Driven Financial Intelligence")
- `mandatory` (boolean): Whether this is non-negotiable (true) or flexible (false)
- `description` (text): What the principle requires
- `rationale` (text): Why this principle is necessary
- `required_constraints` (array): Specific requirements developers must follow
- `reviewer_authority` (string): Team responsible for verifying compliance (e.g., "architecture-team", "financial-domain-expert")
- `version_introduced` (string): Constitution version when principle was established

**Example**:
```
name: "AI-Driven Financial Intelligence"
mandatory: true
description: "Every feature providing financial insights MUST leverage Gemma AI"
rationale: "Core value proposition requires AI analysis; without it, product becomes standard dashboard"
required_constraints:
  - "AI insights must be marked as AI-generated"
  - "Confidence levels must be disclosed to users"
  - "Fallback to rule-based analysis when AI confidence < threshold"
  - "All AI decisions must be logged with input/output for auditability"
reviewer_authority: "ai-systems-reviewer"
version_introduced: "1.0.0"
```

---

### 3. Development Workflow Stage

**What it represents**: A phase in the development lifecycle with specific quality gates and reviewer requirements

**Attributes**:
- `stage_name` (string): Phase identifier (e.g., "Planning", "Implementation", "Testing", "Review", "Deployment")
- `description` (text): What happens in this stage
- `entry_criteria` (array): What must be true to enter this stage
- `exit_criteria` (array): What must be true to exit this stage
- `required_gates` (array of Gate objects): Quality checks that must pass
- `required_reviewers` (array of Reviewer Role objects): Who must approve before proceeding
- `approval_threshold` (integer): Number of reviewers required for approval

**Example - Review Stage**:
```
stage_name: "Review"
description: "Code review and compliance verification"
entry_criteria:
  - "All tests passing in CI pipeline"
  - "Code coverage meets minimum 80% threshold"
  - "PR created with governance checklist completed"
exit_criteria:
  - "Approved by architecture owner"
  - "Approved by domain expert (financial or AI as applicable)"
  - "No unresolved governance violations"
required_gates:
  - Gate: Governance principle compliance
  - Gate: Test coverage verification
  - Gate: Financial audit trail (if financial code)
  - Gate: AI transparency (if AI code)
required_reviewers:
  - Role: "architecture-owner" (required: 1)
  - Role: "financial-domain-expert" (required: 1 if financial code)
  - Role: "ai-systems-reviewer" (required: 1 if AI code)
approval_threshold: 2  # At least 2 reviewers from required roles
```

---

### 4. Review Checklist

**What it represents**: A governance verification checklist applied during PR review

**Attributes**:
- `checklist_name` (string): Name identifying the checklist (e.g., "General Governance Review")
- `applicable_to` (array): Code types this applies to (e.g., ["all"], ["financial"], ["ai"], ["database"])
- `review_items` (array of ChecklistItem objects): Specific items to verify
- `required_approver_role` (string): Minimum expertise required to approve (e.g., "code-reviewer", "financial-domain-expert")
- `auto_fail_violations` (array): Violations that automatically block merge

**Checklist Items**:
- Each item has: description, principle(s) it verifies, verification method, severity (blocking/warning)

**Example Financial Checklist Item**:
```
description: "Currency amounts use DECIMAL type, not float"
principle: "Financial Data Integrity - Precision"
verification_method: "Review database schema and code; check variable types"
severity: "blocking"  # Prevents merge
```

---

### 5. Amendment Proposal

**What it represents**: A proposed change to the constitution

**Attributes**:
- `proposal_id` (string): Unique identifier (e.g., "AMEND-001")
- `proposed_by` (string): Name/username of proposer
- `proposal_date` (date): When proposal submitted
- `proposed_change` (text): What is being changed and why
- `justification` (text): Why existing principle is insufficient
- `impact_analysis` (text): How change affects existing features
- `migration_plan` (text): Plan for updating existing code if needed
- `status` (enum): "DRAFT", "UNDER_REVIEW", "APPROVED", "REJECTED", "IMPLEMENTED"
- `approver_tech_lead` (string): Tech lead approval (name, date)
- `approver_domain_expert` (string): Domain expert approval (name, date)
- `effective_date` (date): When approved amendment takes effect

**Validation Rules**:
- Cannot remove core principle (requires special board approval, not in v1)
- Impact analysis must identify affected features
- Migration plan required if change affects existing code
- Both tech lead and at least one domain expert must approve
- Timeline: should complete within 2 weeks of proposal

---

### 6. Compliance Audit

**What it represents**: Monthly review of merged PRs for governance compliance

**Attributes**:
- `audit_id` (string): Unique identifier (e.g., "AUDIT-202609")
- `audit_month` (string): YYYYMM format (e.g., "202609")
- `audit_date` (date): Date audit was conducted
- `total_prs_merged` (integer): Total PRs merged in month
- `sample_size` (integer): Number of PRs sampled (5-10% of total)
- `prs_audited` (array of AuditRecord): Audit result for each sampled PR
- `violations_found` (integer): Total violations across sample
- `violation_summary` (object): By violation type and severity
- `auditor_name` (string): Who conducted audit
- `status` (enum): "COMPLETE", "IN_PROGRESS"

**Audit Record Structure**:
- `pr_number` (integer): GitHub PR number
- `pr_title` (string): PR title
- `compliance_status` (enum): "PASS", "FAIL"
- `violations` (array of Violation objects): Specific violations found
- `corrective_action` (text): Required fix (if violation found)
- `follow_up_date` (date): When corrective action must be completed

**Violation Record**:
- `principle_violated` (string): Which constitution principle
- `description` (text): What the violation is
- `severity` (enum): "CRITICAL" (blocks production), "MAJOR" (must fix), "MINOR" (advisory)
- `pr_number` (integer): Reference to PR
- `found_by` (string): Auditor name
- `resolved` (boolean): Whether corrective action completed
- `resolution_date` (date): When resolved

---

### 7. Developer Acknowledgment Record

**What it represents**: Proof that developer reviewed and understood constitution

**Attributes**:
- `developer_name` (string): Team member name/username
- `acknowledgment_date` (date): When acknowledged
- `constitution_version` (string): Version they acknowledged
- `acknowledged_sections` (array): Which sections they confirmed understanding
- `next_acknowledgment_due` (date): When they need to re-acknowledge (after major version bump)

**Validation Rules**:
- All active developers must acknowledge constitution within 30 days of ratification
- Re-acknowledgment required after MAJOR version bump
- Records kept for audit trail

---

## Data Relationships

```
Constitution Document
    ├── contains: Core Principle (1:many)
    │   └── referenced_by: Review Checklist (1:many)
    ├── contains: Development Workflow Stage (1:many)
    │   └── contains: Required Reviewers (1:many)
    └── amended_by: Amendment Proposal (0:many)
        └── leads_to: Amendment (when approved)
        
Compliance Audit (monthly)
    └── contains: Audit Record (multiple)
        └── may_generate: Violation Record (0:many)
            └── resolved_by: Amendment Proposal (optional)
            
Developer
    ├── creates: Amendment Proposal (0:many)
    ├── approves: Amendment Proposal (0:many)
    ├── conducts: Compliance Audit (0:many)
    └── has: Developer Acknowledgment Record
```

---

## State Transitions

### PR Review Flow
```
PR Created
  ↓
Automated Gate Check → FAIL → Requires fixes
  ↓ PASS
Review Checklist Applied
  ↓
Governance Compliance Check
  ├─ PASS → Financial/AI specialized review (if applicable)
  │           ├─ PASS → Approved
  │           └─ FAIL → Requires changes
  └─ FAIL → Blocked, corrective action required
  ↓
All Gates Pass → Can Merge
```

### Amendment Lifecycle
```
Proposal Created (DRAFT)
  ↓
Impact Analysis & Justification (DRAFT → UNDER_REVIEW)
  ↓
Tech Lead Review
  ├─ REJECTED → End
  └─ APPROVED → Awaiting Domain Expert
  ↓
Domain Expert Review
  ├─ REJECTED → End
  └─ APPROVED → Status = APPROVED, set effective_date
  ↓
Implementation (developers update code if needed)
  ↓
Status = IMPLEMENTED, Amendment recorded in constitution history
```

### Compliance Audit Cycle
```
Monthly Audit Scheduled
  ↓
Generate Random PR Sample
  ↓
Review Each PR Against Governance Checklist
  ├─ PASS → Record pass
  └─ FAIL → Document violation, identify corrective action
  ↓
Generate Audit Report
  ├─ Zero violations → Archive
  └─ Violations found → Create follow-up tasks, set resolution deadlines
  ↓
Follow-up verification (verify corrective actions completed)
  ↓
Audit Complete, Archive Record
```

---

## Constraints & Validation

1. **Immutability**: Constitution document is append-only (history through amendments)
2. **Audit Trail**: All governance decisions logged with timestamp and actor
3. **Consistency**: Amendment effective date cannot precede approval date
4. **Versioning**: Constitution version must increment; cannot have duplicate versions
5. **Coverage**: Monthly audits must sample at least 5% of merged PRs
6. **Completeness**: All active developers must have current acknowledgment record
7. **Authorization**: Only approved amendments can update constitution

---

## Success Metrics

- **Adoption**: 90% of developers acknowledge constitution within 30 days
- **Compliance**: 95% of audited PRs pass governance checklist
- **Amendment Speed**: Average 2 weeks from proposal to approval
- **Audit Efficiency**: Audits complete within 3 business days of month end
