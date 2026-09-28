# Governance FAQ

**Frequently Asked Questions about ProjectPulse AI Governance**

---

## General Governance Questions

### Q1: What is governance and why do we have it?

**A**: Governance is a framework of rules and procedures that ensure:
- Financial data is always precise and auditable
- AI decisions are transparent and configurable
- Architecture is scalable and modular
- Code quality is high (tested and reviewed)

We have governance because ProjectPulse AI deals with financial data that must be accurate, auditable, and compliant. The governance framework gives us confidence that our code meets these standards.

### Q2: Do the governance principles apply to all code?

**A**: Yes. Principle IV (Testing) applies to 100% of code. The other principles apply when:
- **Principle I (AI)**: Your code involves AI models, inference, confidence scores
- **Principle II (Financial)**: Your code touches money, calculations, audit trails
- **Principle III (Architecture)**: Your code changes APIs, database schemas, system structure

But everyone must write tests and pass code review.

### Q3: Who enforces governance?

**A**: 
- **Reviewers**: Verify governance in code reviews using the checklists
- **Tech Lead**: Oversees governance adoption and handles escalations
- **Domain Experts**: Verify their principle (Finance, AI, Architecture experts)
- **Compliance Audits**: Monthly audits verify overall compliance

Governance is everyone's responsibility.

### Q4: What happens if my PR violates governance?

**A**: 
1. Reviewer identifies violation using governance checklist
2. Reviewer requests changes with specific guidance
3. You fix the code to comply
4. Reviewer approves and merges
5. If pattern emerges, escalate to Tech Lead

Violations are learning opportunities, not punishments. We help you fix them.

### Q5: Can I propose changes to governance?

**A**: Yes! See [Amendment Process](amendment-process.md). You can propose changes if:
- Principle is unclear
- Implementation shows need for adjustment
- New practice emerges
- Team consensus around change

Amendment takes ~2 weeks from proposal to enforcement.

---

## Principle I: AI-Driven Financial Intelligence

### Q1: Why document the model?

**A**: So we know:
- Which model made a decision (for debugging/verification)
- Whether it's the version we intended to use
- Whether we have the right license (legal compliance)
- Whether we trained it on the right data (correctness)

Without documentation, we can't audit AI decisions.

### Q2: What's a confidence score?

**A**: A number (0.0-1.0) indicating how confident the model is in its prediction:
- **0.9-1.0**: Model very confident (usually use prediction)
- **0.5-0.9**: Model somewhat confident (use with caution)
- **0.0-0.5**: Model not confident (usually don't use, escalate to human)

Confidence tells downstream code whether to trust the prediction.

### Q3: What should I log for AI decisions?

**A**: Log:
- Model name and version used
- Confidence score of prediction
- Input data (or summary)
- Predicted output
- Key factors influencing decision
- Timestamp and user context

This allows us to audit why a decision was made and catch problems.

### Q4: Can I hardcode model parameters?

**A**: No. Parameters must be configurable (in config files), so we can:
- Adjust confidence thresholds without code change
- Switch model versions without code change
- Adjust fallback behavior without code change

Configuration allows experimentation and tuning.

### Q5: What if model confidence is too low?

**A**: Define fallback behavior:
- Return error (clear that decision can't be made)
- Escalate to human review (person makes decision)
- Use simpler fallback calculation
- Return "needs human input" status

Handle low-confidence gracefully, don't ignore it.

---

## Principle II: Financial Data Integrity & Compliance

### Q1: Why use DECIMAL instead of float?

**A**: Float arithmetic loses precision:
```python
0.1 + 0.2 = 0.30000000000000004  # Wrong!
```

DECIMAL preserves exact values:
```python
Decimal("0.1") + Decimal("0.2") = Decimal("0.3")  # Correct!
```

For money, precision is everything. $0.01 error matters in audit.

### Q2: How do I use Decimal in Python?

**A**:
```python
from decimal import Decimal

# ✅ Correct
amount = Decimal("10.50")
total = Decimal("0")
total += amount  # Still exact

# ❌ Wrong
amount = 10.50  # Float
total = 0.0
total += amount  # Loses precision
```

Always convert to Decimal from string, never from float.

### Q3: What's "single source of truth"?

**A**: Each financial value calculated in ONE place. Example:
- ❌ Invoice total calculated in 2 places → can drift
- ✅ Invoice total calculated once, cached/queried → always consistent

Single source means: same calculation always gives same result.

### Q4: How do I log financial changes?

**A**: Log:
- WHO made the change (user ID)
- WHEN it was made (timestamp)
- WHAT changed (from amount → to amount)
- WHY it changed (reason/description)
- Example: "User 42 adjusted invoice from $100.00→$99.99 on 2026-10-01 14:23 UTC: price correction"

Make logs queryable and immutable (can't be deleted).

### Q5: What's reconciliation?

**A**: Monthly verification that your calculations match source data:
- Sum all invoices → matches ledger? ✅
- Portfolio value calculated → matches holdings? ✅
- Tax calculations → match correct rules? ✅

Reconciliation catches errors early before compounding.

---

## Principle III: Scalable API-First Architecture

### Q1: What's an API contract?

**A**: Documented specification of what an API endpoint accepts and returns:
```python
# ✅ Good: Contract documented
class PortfolioRequest(BaseModel):
    portfolio_id: str
    include_recommendations: bool = False

class PortfolioResponse(BaseModel):
    portfolio_id: str
    total_value: Decimal
    holdings: List[Holding]
```

Contract ensures clients know what to expect.

### Q2: Why maintain backward compatibility?

**A**: So old clients still work when API changes:
- ❌ Remove field → breaks old clients
- ✅ Keep old field, add new optional field → old clients work, new clients get new feature

2+ version compatibility means smooth upgrades.

### Q3: What are database migrations?

**A**: SQL scripts that safely change database schema:
- ✅ Migration: Add column, set default, verify integrity
- ❌ Direct change: ALTER TABLE without rollback plan

Migrations are tested, reversible, and safe.

### Q4: Why enforce foreign keys?

**A**: So invalid data can't be created:
- ❌ Invoice references non-existent customer → data integrity broken
- ✅ Foreign key constraint → can't create invoice without valid customer

Constraints prevent bad data from entering system.

### Q5: How modular should architecture be?

**A**: Clear domain boundaries:
- **Portfolio Domain**: Manages portfolios and holdings
- **Invoice Domain**: Manages invoices and payments
- **AI Domain**: Manages AI predictions and recommendations

Domains interact through APIs, not direct database access.

---

## Principle IV: Test-Driven Development & Quality Gates

### Q1: Why 80% coverage?

**A**: 80% is high enough to:
- Catch most bugs early (less debugging)
- Provide confidence in code behavior
- Not so high it requires testing trivial code

80% means most important code is tested and safe.

### Q2: What if I can't reach 80%?

**A**: 
1. First: Write more tests (most common solution)
2. Ask: What code is hard to test? Refactor for testability
3. Last resort: Document why and get approval from Tech Lead

Don't ship code below 80% without explicit approval.

### Q3: What's a regression test?

**A**: A test that verifies a bug is fixed:
1. Write test that FAILS with the bug
2. Fix the bug
3. Verify test PASSES after fix
4. Keep the test in codebase so bug won't regress

Regression tests prevent fixing the same bug twice.

### Q4: Do I need integration tests?

**A**: Yes. Example:
- ❌ Unit test: Function works in isolation
- ✅ Integration test: Full request → database → response works end-to-end

Integration tests catch issues unit tests miss.

### Q5: What if PR is failing CI/CD tests?

**A**: Fix before submitting:
1. Run tests locally: `pytest`
2. Fix failing tests
3. Increase coverage if needed
4. Verify all tests pass
5. Then submit PR

Don't merge failing tests into main.

---

## Code Review & Compliance

### Q1: How long does code review take?

**A**: Usually 1-3 days. Depends on:
- Code complexity (simple: hours, complex: days)
- Reviewer availability
- Whether requested reviewers needed

Plan ahead for review time.

### Q2: What if I disagree with reviewer feedback?

**A**:
1. Discuss in PR comments
2. Explain your reasoning
3. Reviewer explains their concern
4. Find compromise or escalate to Tech Lead

Disagreement is normal. Goal is getting to safe code.

### Q3: What's a governance violation?

**A**: Code that doesn't meet a governance principle:
- Example: Using float for money
- Example: No test coverage
- Example: AI decision not logged

Violations documented and tracked for compliance audit.

### Q4: Can I merge if there's a governance violation?

**A**: No. Violations must be fixed before merge:
- CRITICAL violations: Fix immediately
- MAJOR violations: Fix within 2 weeks (but don't merge yet)
- MINOR violations: Fix in next PR (can still merge)

Governance is enforced at merge time.

### Q5: How do I request specialized reviewers?

**A**: In PR template, mark which principles apply:
- Principle I (AI) → Request AI Systems Reviewer
- Principle II (Financial) → Request Financial Domain Expert
- Principle III (Architecture) → Request Architecture Owner
- Principle IV (Testing) → Tech Lead reviews

System automatically suggests reviewers based on what you mark.

---

## Compliance & Audits

### Q1: What's a compliance audit?

**A**: Monthly review of random PRs to verify governance adherence:
- Audit 5-10 random PRs from last month
- Check each against governance checklist
- Document any violations
- Report compliance rate (target: 95%)

Audits verify we're actually following governance.

### Q2: How are PRs selected for audit?

**A**: Deterministic random sampling using month seed:
- Seed = YYYYMM (e.g., 202610)
- Same seed produces same sample every month
- Reproducible: Anyone can verify sample selection
- Prevents gaming (can't guess which PRs audited)

Sample selection is fair and verifiable.

### Q3: What happens if compliance rate drops?

**A**: 
1. If 90-95%: Note as concern, increase vigilance
2. If <90%: Escalate to Tech Lead
3. Conduct root cause analysis
4. Implement corrective action (training, process change)
5. Re-audit after 2 weeks to verify improvement

Compliance trending is monitored constantly.

### Q4: How long do I have to fix a violation?

**A**: Depends on severity:
- **CRITICAL**: Immediate (before next PR merge)
- **MAJOR**: 2 weeks from audit date
- **MINOR**: Current sprint

Timeline balances safety with reality of fixing things.

### Q5: Who receives audit reports?

**A**: 
- Tech Lead (oversight)
- Team Leads (their team violations)
- All team (summary/trends)
- Leadership (governance health)

Audits are transparent to whole organization.

---

## Training & Adoption

### Q1: Do I need training to follow governance?

**A**: Recommended:
1. Read constitution (20 min)
2. Read principle guides for your role (30-60 min)
3. Attend role-specific training session (1 hour)
4. Ask questions as you code

Training is invested upfront to save time later.

### Q2: What if I don't understand a principle?

**A**: 
1. Read principle section in constitution again
2. Read principle-specific guide (e.g., Developer onboarding)
3. Ask your Tech Lead
4. Request clarification during next training

Questions are encouraged! Governance only works if everyone understands.

### Q3: How long until governance is fully adopted?

**A**:
- Week 1: Training and acknowledgment (target: 100% by 2026-10-28)
- Week 2-4: Team applying principles in PRs
- Week 4+: Compliance audits verify adoption

Full adoption targeted for end of October 2026.

### Q4: Will governance slow down development?

**A**: Short term: Yes (learning curve). Long term: No.
- Initial: Learning takes time
- After 2-3 weeks: Speed increases (fewer bugs, easier review)
- Ongoing: Governance actually speeds up (clear standards, less back-and-forth)

Upfront investment pays off quickly.

### Q5: Can I get help implementing governance?

**A**: Yes!
- Read guides in `docs/governance/`
- Ask your Tech Lead
- Contact domain expert (Finance, AI, Architecture)
- Check FAQ (this document)
- Look at examples in merged PRs

Help available at every step.

---

## Violations & Escalation

### Q1: What if my PR has multiple violations?

**A**: Fix all violations before merge:
1. Reviewer documents all violations
2. You fix them one by one
3. Push updated code
4. Reviewer re-checks
5. Merge when all fixed

Multiple violations are OK if you fix them.

### Q2: What if same violation repeats in later PRs?

**A**: 
1. First violation: Learning opportunity, guidance provided
2. Second violation: Pattern noted, extra review requested
3. Third+ violations: Escalate to Tech Lead for 1-on-1 discussion

Patterns indicate need for additional training or support.

### Q3: What if I need exception to governance?

**A**: Exceptions exist but require approval:
1. Document why exception is needed
2. Propose alternative (how to stay mostly compliant)
3. Request approval from Tech Lead + relevant domain expert
4. If approved: Document exception and timeline for compliance

Exceptions rare and always documented.

### Q4: Can governance be changed?

**A**: Yes! See [Amendment Process](amendment-process.md):
1. Propose change with rationale
2. Get approval from Tech Lead + domain experts
3. 2-week implementation and training period
4. New rules take effect

Governance evolves based on experience.

### Q5: What if team disagrees on governance?

**A**: 
1. Discuss in team meeting or PR comments
2. Tech Lead facilitates decision
3. If still stuck, escalate to CTO
4. Decision documented for future reference

Disagreements are normal and resolved through discussion.

---

## For Reviewers

### Q1: How strict should I be with governance?

**A**: Consistently enforce checklist:
- CRITICAL violations: Always request changes
- MAJOR violations: Always request changes
- MINOR violations: Document but can approve if time-constrained

Consistency matters. Everyone held to same standard.

### Q2: What if code violates governance but is otherwise good?

**A**: Request changes anyway:
- Governance is mandatory, not optional
- Good code that violates governance → fix and re-submit
- Enforcement is how team learns standards

Governance non-negotiable.

### Q3: How do I know when to escalate?

**A**: Escalate to Tech Lead if:
- PR author disagrees with violation finding
- Violation pattern in multiple PRs
- Violation requires architectural change
- You're unsure about severity level

Escalation helps resolve disagreements and systemic issues.

### Q4: Should I review governance while reviewing code?

**A**: Yes. Use governance checklist:
1. Review code for quality
2. Check governance compliance
3. Request changes for both issues
4. Document which is which

Governance review is part of code review.

### Q5: What if I don't know a principle well?

**A**: 
- Read relevant principle guide
- Ask domain expert before approving
- Escalate to Tech Lead if unsure

Don't approve code you're not confident about.

---

## Leadership & Management

### Q1: How do I track governance adoption?

**A**: Use compliance audits:
- Monthly compliance rate (target: 95%)
- Violations by principle (which need more focus)
- Violations by team (who needs training)
- Trends over time (adoption improving?)

Audits provide data on governance health.

### Q2: How do I know if governance is working?

**A**: Monitor:
- Compliance rate: 95%+ = working
- Bug rate: Decreasing = working
- Code review time: Stabilizing = working
- Team satisfaction: Positive = working

Working governance = compliance + efficiency.

### Q3: What if my team is struggling with governance?

**A**: 
1. Identify which principles are hard
2. Provide additional training
3. Simplify or clarify requirements
4. Pair with domain expert
5. Escalate to Tech Lead for support

Struggle is normal during adoption.

### Q4: How do I communicate governance to leadership?

**A**: Use compliance dashboards:
- Compliance rate percentage (red/yellow/green)
- Risk areas (which principles struggling)
- Adoption trend (improving month-to-month)
- Business impact (bugs prevented, audits passed)

Data-driven communication to leadership.

### Q5: Can I modify governance for my team?

**A**: No. Governance is company-wide and consistent:
- All teams follow same principles
- Same review standards applied everywhere
- Same audit procedures for all

Consistency is crucial. For changes, use amendment process.

---

## Need More Help?

**If this FAQ doesn't answer your question:**

1. **Technical questions**: Contact Tech Lead or domain expert
2. **Process questions**: Read relevant procedure document
3. **Governance changes**: Follow [Amendment Process](amendment-process.md)
4. **Report issue**: Create GitHub issue with `governance` label

**Key Contacts:**
- Architecture Owner: [To be assigned]
- Financial Domain Expert: [To be assigned]
- AI Systems Reviewer: [To be assigned]
- Tech Lead: [To be assigned]

---

**Last Updated**: 2026-09-28

[← Back to Governance Main](../../.github/GOVERNANCE.md)
