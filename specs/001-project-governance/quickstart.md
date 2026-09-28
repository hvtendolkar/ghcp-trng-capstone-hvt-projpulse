# Quickstart: Applying the Governance Framework

**Purpose**: Practical guide for teams to apply and verify ProjectPulse AI governance framework

**Audience**: All developers, reviewers, and project leadership

---

## Part 1: Understanding the Framework (15 minutes)

### Step 1: Read the Constitution

Start here to understand governance principles:

**File**: [.specify/memory/constitution.md](../../.specify/memory/constitution.md)

**What to understand**:
- Core Principles (4): What they require and why
- Technology Stack: Required languages, frameworks, databases
- Development Workflow: 5 stages (Planning → Deployment)
- Governance: Amendment process and compliance review

**Minimal read** (5 min): Read Introduction through Core Principles section

**Full read** (15 min): Read entire document including Technology Stack and Development Workflow

### Step 2: Understand Your Role

Identify your role and what governance means for you:

**As a Developer**:
- Review [Principle IV: Test-Driven Development](../../.specify/memory/constitution.md#iv-test-driven-development--quality-gates) - you must write tests for all code
- Review [Principle II: Financial Data Integrity](../../.specify/memory/constitution.md#ii-financial-data-integrity--compliance) if you work on financial features
- Review [Principle I: AI-Driven Financial Intelligence](../../.specify/memory/constitution.md#i-ai-driven-financial-intelligence) if you work on AI integration

**As a Code Reviewer**:
- Read [Development Workflow: Review Stage](../../.specify/memory/constitution.md#development-workflow)
- Use the [General Governance Checklist](./contracts/general-governance-checklist.md) when reviewing PRs
- Understand your specialized reviewer role (architecture, financial, AI)

**As Project Leadership**:
- Read [Summary](../../.specify/memory/constitution.md#core-principles) to understand risk mitigation
- Review [Development Workflow](../../.specify/memory/constitution.md#development-workflow) to understand quality gates
- Plan monthly compliance audits (governance audit process described below)

---

## Part 2: Applying Governance to Your Work (Depends on Role)

### For Developers: Before You Create a PR

**1. Plan Your Work Against Constitution** (5 min)

Before starting implementation, answer these questions:

- [ ] Does my feature affect financial data? → Must follow Principle II (Financial Data Integrity)
- [ ] Does my feature provide financial insights? → Must use AI and follow Principle I (AI-Driven Insights)
- [ ] Am I modifying API endpoints or database? → Must follow Principle III (API Architecture)
- [ ] All code has tests? → Must follow Principle IV (TDD - 80% coverage min)

**2. Development Checklist**

Follow this process:

```
1. Write tests first (TDD)
   - Tests define what you're building
   - Tests catch bugs before code review
   - Target: ≥80% coverage for business logic

2. Implement code
   - Follow architecture/modular design principles
   - Use Decimal type for currency (not float)
   - Implement audit logging for financial changes
   - Add AI transparency markers if using Gemma API

3. Run all tests locally
   - Ensure coverage ≥80% (tools: pytest/coverage, Jest/Istanbul, etc.)
   - All tests pass

4. Self-review against governance checklist
   - Check: [General Governance Checklist](./contracts/general-governance-checklist.md)
   - Identify which principles apply to your code
   - Verify each checklist item

5. Create PR with checklist completed in description
   - Copy checklist items from contracts/ that apply to your code
   - Mark items as complete as you review your own code
   - Note any items that don't apply (e.g., "N/A - no financial data changes")
```

**3. Create PR with Completed Governance Checklist**

Include this in your PR description (see example below):

```markdown
## Governance Compliance

**Principles Applied**: 
- [ ] Principle I: AI-Driven Insights (if applicable)
- [ ] Principle II: Financial Data Integrity (if applicable)
- [ ] Principle III: API Architecture (if applicable)
- [x] Principle IV: TDD & Quality Gates (all PRs)

**Checklist** (items completed during development):
- [x] Test coverage ≥80%
- [x] All tests passing locally
- [x] Code reviewed against relevant governance principles
- [x] Financial data uses DECIMAL type (N/A - no financial changes)
- [x] AI insights marked as AI-generated (N/A - no AI code)

**Constitution Reference**: See [.specify/memory/constitution.md]
```

---

### For Reviewers: When Reviewing a PR

**1. Verify Pre-flight Gates** (1-2 min)

- [ ] GitHub Actions CI pipeline passes (green checkmark)
- [ ] No security warnings (secret scanning clean)
- [ ] Governance checklist completed in PR description

**2. Check Code Against Governance** (5-15 min, depending on complexity)

Use the [General Governance Checklist](./contracts/general-governance-checklist.md):

```
For all PRs:
  → Check Principle IV (TDD): Is test coverage ≥80%? Tests cover edge cases?

If financial code:
  → Check Principle II: Currency uses DECIMAL? Audit trail logged? Edge cases tested?
  → Requires: Financial Domain Expert approval

If AI code:
  → Check Principle I: AI marked as AI-generated? Confidence shown? Logged?
  → Requires: AI Systems Reviewer approval

If API/database code:
  → Check Principle III: API documented? Schema integrity? Backward compat?
  → Requires: Architecture Owner approval
```

**3. Approve or Request Changes**

- If all governance checks pass: **Approve**
  - Comment example: "✅ Governance compliance verified. Principle II & IV gates pass."
  
- If violations found: **Request Changes**
  - Comment example: "⚠️ Currency amounts should use DECIMAL type, not float (Principle II). Please update line 42."
  - Reference specific principle and required fix

- If specialized review needed: **Request Review from Specialist**
  - If financial: add financial-domain-expert as reviewer
  - If AI: add ai-systems-reviewer as reviewer
  - If architecture: add architecture-owner as reviewer

**4. Merge Only When All Gates Pass**

- [ ] All automated tests passing (CI/CD)
- [ ] Governance checklist verified by reviewers
- [ ] Specialist approvals received (if needed)
- [ ] No unresolved comments

---

### For Leadership: Conducting Monthly Compliance Audits

**Timeline**: Conduct audit within first 5 business days of following month

**Steps**:

**1. Prepare** (10 min)

- [ ] Gather list of all PRs merged in the previous month from GitHub
- [ ] Count total: e.g., "42 PRs merged in September"
- [ ] Calculate sample size: 5-10% = 2-4 PRs to audit
- [ ] Use deterministic random sampling (see [compliance-audit-template.md](./contracts/compliance-audit-template.md) for algorithm)

**2. Audit Each PR** (15-20 min per PR)

For each sampled PR, use the [Compliance Audit Template](./contracts/compliance-audit-template.md):

```
For each PR:
  1. Check if passing governance checklist
  2. Verify tests passed in CI
  3. Review code against applicable principles
  4. Document any violations
  5. Assess severity: CRITICAL (block merge) / MAJOR (fix required) / MINOR (advisory)
```

**3. Generate Report** (20 min)

Complete the [Compliance Audit Template](./contracts/compliance-audit-template.md):
- [ ] List all PRs audited
- [ ] Document violations by principle
- [ ] Calculate pass rate
- [ ] Identify trends (e.g., "Financial PRs consistently missing audit trail logging")
- [ ] Recommendations for next month

**4. Share Results** (10 min)

- [ ] Email report to development team with findings and improvement areas
- [ ] Share with project leadership showing compliance status
- [ ] Archive report in `COMPLIANCE/monthly-audits/202609-governance-audit.md`
- [ ] Schedule corrective action follow-up for end of month

**5. Track Corrective Actions** (ongoing)

- [ ] Violations with "corrective action required" → added to backlog
- [ ] Follow up in 2-3 weeks to verify corrections completed
- [ ] Document resolution in audit follow-up section

---

## Part 3: Proposing Changes to Governance (Constitution Amendments)

If you believe the constitution needs updating:

**1. Check Amendment Process** (5 min)

Read [Amendment Process](../../.specify/memory/constitution.md#amendment-process):
- Written justification required
- Impact analysis required
- Migration plan required
- Approval from tech lead + domain expert required

**2. Write Proposal** (30-60 min)

Create a proposal document with:
- What is being changed and why
- Why existing principle is insufficient
- How it affects existing features
- Plan to update existing code
- Timeline (should complete within 2 weeks)

**3. Submit for Review** (ongoing)

- Proposal ID: AMEND-### (get next number from governance team)
- Share with tech lead and domain experts
- Get feedback and iterate
- Target approval in 2 weeks

**4. Implement** (post-approval)

- Update constitution document with amendment
- Version bump (MAJOR/MINOR/PATCH as appropriate)
- Update code/processes affected by change
- Document amendment in constitution history

---

## Part 4: Verification Scenarios

These scenarios demonstrate the governance framework working end-to-end:

### Scenario 1: Financial Feature PR Review (15 min end-to-end)

**Setup**: Developer creates PR adding expense tracking calculation

**Developer Side** (before creating PR):
- Writes tests for expense calculation (edge cases: negative, rounding, currency conversion)
- Implements DECIMAL type for currency storage
- Adds audit trail logging (who, when, what, before/after values)
- Runs tests locally: 82% coverage ✓
- Completes Principle II & IV checklist items
- Creates PR with governance checklist marked complete

**Reviewer Side** (when PR submitted):
- Sees CI passing and governance checklist ✓
- Checks Principle II items: DECIMAL type ✓, audit trail ✓, edge cases ✓
- Requests financial-domain-expert reviewer
- Approves code review: "Principle II & IV gates pass"

**Finance Reviewer Side**:
- Reviews financial calculation logic
- Confirms edge cases appropriate for financial use
- Approves: "Financial integrity verified"

**Result**: PR merged after all gates pass ✓

---

### Scenario 2: AI Feature PR Review (20 min end-to-end)

**Setup**: Developer creates PR adding AI-powered portfolio recommendation

**Developer Side** (before creating PR):
- Writes tests with mock Gemma API responses (no real API calls yet)
- Implements AI insight marking in API response: `"insights": [{"value": "...", "source": "ai", "confidence": 0.87, "reasoning": "..."}]`
- Implements fallback to rule-based recommendation when confidence < 0.75
- Logs all AI decisions: timestamp, input, model version, confidence, decision
- Runs tests: 83% coverage ✓
- Completes Principle I & IV checklist items
- Creates PR with governance checklist marked complete

**Reviewer Side** (when PR submitted):
- Sees CI passing and governance checklist ✓
- Checks Principle I items: AI marked ✓, confidence shown ✓, fallback logic ✓
- Requests ai-systems-reviewer
- Approves code: "Principle I & IV gates pass"

**AI Systems Reviewer Side**:
- Verifies transparency of AI reasoning
- Confirms logging includes decision audit trail
- Confirms mock tests before real API integration
- Approves: "AI transparency and auditability verified"

**Result**: PR merged after all gates pass ✓

---

### Scenario 3: Monthly Compliance Audit (60 min for complete audit)

**Month**: September 2026 | Total PRs merged: 42 | Sample size: 5%

**Audit Process**:
- [ ] Select 2-3 random PRs from September (using deterministic seed)
- [ ] Review each PR against governance checklist
- [ ] PR #487 (financial): ✓ Passes all checks
- [ ] PR #491 (AI): ⚠️ Missing confidence level in logging (Principle I violation - MAJOR)
  - Action: Request corrective PR adding confidence to logs
  - Due: 1 week
- [ ] Generate report: 66% pass rate (2 pass, 1 fail)
- [ ] Share with team: Highlight need for confidence logging in AI features
- [ ] Follow up 1 week later: Verify corrective action completed ✓

---

## Quick Reference

### Governance Checklist Quick Links

- [General Governance Checklist](./contracts/general-governance-checklist.md) - Use when reviewing all PRs
- [Compliance Audit Template](./contracts/compliance-audit-template.md) - Use for monthly audits
- [Constitution Document](../../.specify/memory/constitution.md) - Full reference

### Key Contacts

- **Architecture Questions**: [Architecture Owner contact]
- **Financial Questions**: [Financial Domain Expert contact]
- **AI Questions**: [AI Systems Reviewer contact]
- **Governance Questions**: [Governance Owner contact]

### Timeline

- **30 days after ratification**: 90% of team acknowledges constitution
- **Monthly**: Governance compliance audit conducted (5 business days into month)
- **2 weeks**: Amendment proposals should complete review cycle
- **Continuous**: All PRs verified against governance before merge

---

## Success Criteria

After governance framework is applied, you should see:

✓ All PRs reference governance principles in description  
✓ 90% team acknowledges constitution understanding  
✓ Monthly audits show ≥95% PRs passing governance checks  
✓ Financial code consistently uses DECIMAL type  
✓ AI code consistently marked as AI-generated  
✓ Test coverage stays ≥80% for business logic  
✓ Zero critical violations in compliance audits  
✓ Corrective actions completed within 5 business days  

---

## Getting Help

**Questions about a principle?** → Read constitution section and reach out to relevant expert

**Not sure if your code meets governance?** → Include draft PR, ask in team chat, get feedback before final submission

**Found a governance violation?** → Document in audit, schedule corrective action, follow up

**Want to change a principle?** → Propose amendment following process in constitution
