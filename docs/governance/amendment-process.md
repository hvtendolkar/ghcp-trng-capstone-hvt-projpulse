# Amendment Process

This guide explains how to propose, review, and approve changes to the ProjectPulse AI Governance Constitution.

## When to Propose an Amendment

Consider proposing an amendment if:
- Current principle is unclear or conflicts with another principle
- Implementation experience shows principle needs adjustment
- New technology or practice requires governance update
- Team consensus emerges around a needed change
- Business requirements shift

## The Amendment Process

### Phase 1: Proposal (Timeline: 1-2 days)

**1. Prepare Your Proposal**
- Use amendment template: `.specify/memory/amendments/amendment-template.md`
- Copy the current constitution text you want to change
- Propose the new text clearly
- Explain rationale: Why is this change needed?
- Identify affected principle(s)

**2. Impact Analysis**
- How does this affect each team (Architecture, Development, Finance, AI)?
- What's the effort to adopt? (High/Medium/Low)
- Timeline: How long will adoption take?
- Migration plan: How do existing projects transition?

**3. Submit for Review**
- Create GitHub issue with label `governance-amendment-proposal`
- Attach your amendment proposal as markdown
- Link to any supporting documentation

### Phase 2: Review & Approval (Timeline: 5-10 business days)

Amendment must be approved by:
- **Tech Lead or CTO** (mandatory)
- **Relevant Domain Expert** (depends on principle affected):
  - Principle I (AI) → AI Systems Reviewer
  - Principle II (Financial) → Financial Domain Expert
  - Principle III (Architecture) → Architecture Owner
  - Principle IV (Testing) → Tech Lead

**Review Criteria**:
- Does amendment clarify or improve governance without weakening standards?
- Is impact analysis complete and realistic?
- Is migration plan feasible?
- Does amendment conflict with other principles?
- Is timeline reasonable for team adoption?

**Approval Workflow**:
1. Tech Lead reviews - checks feasibility and overall fit
2. Domain Expert reviews - checks principle-specific impact
3. Team Leads review - assess adoption timeline
4. CTO approval (if Principle I/II affected or major change)

### Phase 3: Implementation (Timeline: 1-2 weeks post-approval)

Once approved:
1. Freeze amendments for 2-day cool-off period
2. Announce amendment to full team
3. Train impacted teams on new requirement
4. Update constitution.md with new text
5. Update version number (semantic versioning)
6. Document in amendment history

### Phase 4: Adoption & Enforcement (Timeline: 2-4 weeks)

- **New PRs** use updated principles immediately
- **Existing code** transitions according to migration plan
- **Code reviews** enforce updated requirements
- **Compliance audits** verify adoption

## Amendment Timeline

```
Day 1-2:    Proposal preparation and submission
Day 3-12:   Review and approval (5-10 business days)
Day 13-14:  Cool-off and announcement
Day 15-30:  Implementation and training
Day 31+:    Enforcement and compliance tracking
```

**Target**: Amendment from proposal to enforcement in 2 weeks

## Version Numbering

Constitution version follows semantic versioning:

- **MAJOR**: Breaking change (e.g., new mandatory requirement)
- **MINOR**: Non-breaking addition (e.g., clarification, new optional practice)
- **PATCH**: Typo fix or clarification with no impact

**Examples**:
- `1.0.0` → `2.0.0` (new mandatory principle or major overhaul)
- `1.0.0` → `1.1.0` (new guidance added, all current code still complies)
- `1.0.0` → `1.0.1` (clarification, no changes to requirements)

## Amendment Approval Checklist

**Tech Lead Reviews**:
- [ ] Amendment proposal is complete (rationale, impact, migration plan)
- [ ] No conflicts with other principles
- [ ] Timeline is realistic (target 2-week total cycle)
- [ ] No new dependencies or tool requirements
- [ ] Can be enforced in code review process

**Domain Expert Reviews**:
- [ ] Amendment improves or clarifies their principle
- [ ] Impact analysis on their domain is accurate
- [ ] Migration plan is feasible for their domain
- [ ] Training materials will be needed (plan them)

**Team Lead Reviews**:
- [ ] Adoption timeline works for their team
- [ ] Training time is budgeted
- [ ] No conflicts with ongoing projects
- [ ] Can be implemented without major disruption

**CTO Reviews** (for major or cross-principle amendments):
- [ ] Aligns with business goals
- [ ] No regulatory or compliance conflicts
- [ ] Approved for immediate enforcement

## Amendment Approval Sign-Off Template

```markdown
## Amendment Approvals

- [x] Tech Lead Approved: [Name] (Date)
- [x] Domain Expert Approved: [Name] (Date)
- [x] Team Leads Approved: [Names] (Date)
- [x] CTO Approved: [Name] (Date)

Approved for implementation starting [DATE]
Enforcement begins [DATE]
```

## Constitution Update

Once approved, amend constitution.md:

1. **Update YAML Frontmatter**:
   ```yaml
   version: 1.1.0
   last_amended_date: 2026-10-15
   amendment_count: 1
   ```

2. **Update Amendment History**:
   ```yaml
   amendment_history:
     - version: 1.1.0
       amended_date: 2026-10-15
       description: Clarified Principle II reconciliation frequency
       amendment_id: AMEND-001
   ```

3. **Update Modified Sections**: Edit the principle text directly in constitution

## Common Amendment Scenarios

### Scenario 1: Clarify Unclear Requirement

**Example**: Principle II mentions "reconciliation" but timing is unclear

**Amendment**: Specify "monthly reconciliation, within first 10 business days of following month"

**Version**: MINOR (1.0.0 → 1.1.0) - clarification, existing code complies

**Timeline**: 1 week

### Scenario 2: Adjust Coverage Requirement

**Example**: 80% coverage is too strict for legacy code module

**Amendment**: "Minimum 80% coverage for new modules and refactored code; legacy modules target 70% coverage during gradual modernization"

**Version**: MINOR (1.1.0 → 1.2.0) - adds exception, doesn't break existing

**Timeline**: 1 week

### Scenario 3: Add New Principle

**Example**: Security governance not currently covered

**Amendment**: Add Principle V: "Security-First Data Protection" alongside existing 4

**Version**: MAJOR (1.2.0 → 2.0.0) - breaking change, new requirement for all code

**Timeline**: 3 weeks (more training needed)

## Escalation Path

If amendment is stuck in review:
- **After 1 week**: Tech lead follows up with reviewers
- **After 2 weeks**: Escalate to CTO for decision
- **Alternative**: Propose simpler, narrower amendment
- **Last resort**: Call all-hands discussion to resolve disagreement

## FAQ: Amendments

**Q: How do I propose an amendment?**
A: Use `.specify/memory/amendments/amendment-template.md`, fill out completely, submit GitHub issue with label `governance-amendment-proposal`

**Q: How long does approval take?**
A: Target 2 weeks from proposal to enforcement (5-10 days review, 2-4 days cool-off/announcement, 3-5 days training)

**Q: Can I propose multiple amendments?**
A: Yes, submit them one at a time. Complex proposals should be broken into smaller, focused amendments.

**Q: What if team disagrees with my amendment?**
A: Discuss in review process. If still stuck, escalate to CTO. Can always re-propose after gathering more evidence.

**Q: Who decides if amendment is approved?**
A: Tech Lead + relevant Domain Experts + CTO (for major changes). Consensus required.

## Amendment Records

All amendments stored in:
- **Amendment proposals**: `.specify/memory/amendments/` (AMEND-### files)
- **Constitution history**: `.specify/memory/constitution.md` (YAML frontmatter + inline notes)
- **GitHub issues**: Labeled `governance-amendment-proposal` for team visibility

---

**Next Amendment Target**: [To be determined by team]

For help proposing amendment, contact your Tech Lead.
