# Architecture Team Kickoff: Governance Framework Adoption

## Meeting Objectives

By end of this session, architecture team will:
1. ✅ Understand 4 core governance principles and why they matter for ProjectPulse AI
2. ✅ Know how to apply Principle III (architecture) in code reviews
3. ✅ Be able to use governance checklist to enforce standards
4. ✅ Ask clarifying questions before enforcement begins
5. ✅ Commit to governance adoption starting Oct 1, 2026

## Slide Outline

### Slide 1: Welcome & Agenda (5 min)
- **Title**: ProjectPulse AI Governance Framework Adoption
- **Subtitle**: Architecture Team Kickoff - Sept 28, 2026
- **Agenda**:
  1. Why governance matters (5 min)
  2. The 4 core principles (10 min)
  3. Principle III: Your role (10 min)
  4. How to enforce in code review (10 min)
  5. Q&A and commitment (5 min)

### Slide 2: Why Governance Matters (5 min)
- **Context**: ProjectPulse AI manages Big 4 portfolio analysis
  - Financial data must be accurate and auditable
  - AI insights must be transparent and explainable
  - Architecture must scale reliably
  - Code must be thoroughly tested

- **Risk**: Without governance:
  - Financial errors accumulate ($$ impact)
  - AI decisions unexplainable (regulatory risk)
  - Architecture becomes unmaintainable
  - Bugs reach production

- **Solution**: Governance framework prevents these risks through:
  - Clear requirements in code review
  - Systematic compliance verification
  - Team training and acknowledgment
  - Monthly audits and trend analysis

### Slide 3: The 4 Core Principles (10 min)

**Principle I: AI-Driven Financial Intelligence**
- Requirement: AI insights must be transparent, validated, auditable, configurable
- Who enforces: AI Systems Reviewer
- Example: Model used documented, confidence score calculated, decisions logged

**Principle II: Financial Data Integrity & Compliance**
- Requirement: Money uses DECIMAL (never float), single source of truth, audit trail, reconciliation
- Who enforces: Financial Domain Expert
- Example: Invoice totals calculated once, all changes logged, monthly reconciliation

**Principle III: Scalable API-First Architecture** 🎯 **YOUR ROLE**
- Requirement: APIs documented, backward compatible, migrations used, integrity enforced
- Who enforces: Architecture Owner (you)
- Example: Endpoint schemas defined, 2+ version compatibility, database migrations tested

**Principle IV: Test-Driven Development & Quality Gates**
- Requirement: 80%+ coverage, unit+integration+database tests, code reviewed
- Who enforces: All reviewers (cross-cutting)
- Example: Coverage verified, regression tests written, checklist completed

### Slide 4: Principle III Detailed (10 min)

**Your Role as Architecture Reviewer**:

| Aspect | What to Check | Why It Matters |
|--------|--------------|--------|
| **API Contracts** | Request/response schemas documented (OpenAPI/Pydantic) | Clients need to know what to expect |
| **Backward Compatibility** | Old clients still work (maintain 2+ versions) | Smooth upgrades, no breaking changes |
| **Database Migrations** | Schema changes use migrations (not direct ALTER TABLE) | Safe rollbacks if deployment fails |
| **Constraints Enforcement** | Foreign keys, checks defined | Prevents invalid data entering system |
| **Domain Boundaries** | Business logic organized by domain | Minimal coupling, testable in isolation |

### Slide 5: Enforcement Process (10 min)

**When reviewing a PR** marked with Principle III:

1. **Check PR template**: Does it mark applicable principles? (Should include Principle III)
2. **Review API contract**: Run through [Architecture Reviewer Checklist](../../docs/governance/architecture-reviewer-guide.md)
   - [ ] Schemas documented?
   - [ ] Backward compatible?
   - [ ] Migrations present?
   - [ ] Constraints enforced?
3. **Assess against governance**: Use general-governance-checklist.md Principle III section
4. **Identify violations**: Document if issues found (CRITICAL/MAJOR/MINOR)
5. **Request changes**: Ask author to fix before approval
6. **Approve**: Once checklist passed, approve PR with "✅ Architecture Review - Principle III APPROVED"

### Slide 6: Example PR Review (5 min)

**Sample PR**: "Add portfolio analysis API endpoint"

```
PR Title: Add /api/v1/portfolio/analysis endpoint
PR Author: [Developer]
Principles: I, III, IV

Architecture Review Checklist:
- [ ] API Contracts: OpenAPI schema defined
- [ ] Backward Compat: New endpoint at v1, doesn't break v0
- [ ] Database: Migration tested for new columns
- [ ] Constraints: Foreign keys enforced
- [ ] Testing: 85% coverage, integration tests included

ACTION: ✅ Approved - Principle III requirements met
```

### Slide 7: Common Violations to Look For (5 min)

| Violation | Severity | Example | Fix |
|-----------|----------|---------|-----|
| Breaking API change | CRITICAL | Remove required field | Maintain backward compat |
| Direct schema modification | MAJOR | ALTER TABLE without migration | Use database migration |
| Missing foreign key | MAJOR | Invoice refs non-existent customer | Add FK constraint |
| No API documentation | MINOR | Endpoint added but no schema | Document with OpenAPI |

### Slide 8: Enforcement Timeline (5 min)

**When enforcement begins**:
- **Oct 1**: All new PRs must reference governance principles
- **Oct 1-5**: First compliance audit (sample 5-10 PRs)
- **Oct 6+**: Reviews enforce Principle III for all architecture-related PRs

**What to expect**:
- Architecture team reviews ~20% of PRs (those with Principle III)
- Each review includes governance checklist (adds ~5-10 min to review)
- Some violations found and fixed initially (learning phase)
- Compliance rate should reach 95% by month 2

### Slide 9: Your Role & Responsibilities (5 min)

**As Architecture Reviewer**, you commit to:

1. ✅ Read `docs/governance/` materials (constitution overview, architecture-reviewer-guide.md, quick-reference.md)
2. ✅ Complete `governance-acknowledgment-form.md` confirming understanding
3. ✅ Apply governance checklist in all architecture-related PR reviews
4. ✅ Document violations when found (create GitHub issue if needed)
5. ✅ Participate in monthly compliance audits
6. ✅ Ask questions if any principle is unclear

### Slide 10: FAQ (5 min)

**Q: What if a developer doesn't agree with violation?**
A: Discuss in PR. If disagreement persists, Tech Lead mediates. Goal is fixing to safe code.

**Q: What if this takes too long?**
A: Initial reviews may be slower (learning). Should normalize within 2-3 weeks.

**Q: Can I request changes for things other than principles?**
A: Yes! Governance checklist is added to regular code review checklist, not replacing it.

**Q: What if architecture needs exception to principle?**
A: Propose to Tech Lead + CTO with business rationale. Exceptions rare and always documented.

**Q: When do I enforce this?**
A: Starting Oct 1, 2026. Gentle enforcement first week (education), strict from week 2.

### Slide 11: Resources (2 min)

**Key Documents**:
- [Constitution](../../.specify/memory/constitution.md) - Core governance document
- [Architecture Reviewer Guide](../../docs/governance/architecture-reviewer-guide.md) - How to enforce Principle III
- [General Governance Checklist](../../specs/001-project-governance/contracts/general-governance-checklist.md) - What to verify
- [Quick Reference](../../docs/governance/quick-reference.md) - 1-page summary
- [FAQ](../../docs/governance/FAQ.md) - Answers to common questions

**Contact**:
- Tech Lead: [To be assigned]
- Architecture Owner: [To be assigned]

### Slide 12: Commitment & Next Steps (5 min)

**Commitment**:
- [ ] I understand the 4 governance principles
- [ ] I can apply Principle III checklist in code review
- [ ] I commit to enforcing governance starting Oct 1, 2026
- [ ] I will ask for help if anything is unclear

**Next Steps**:
1. Complete governance-acknowledgment-form.md (today/tomorrow)
2. Review architecture-reviewer-guide.md (by Sept 30)
3. Use checklist in first PR review (starting Oct 1)
4. Participate in monthly audits (first one Oct 1-5)

**Questions?** [Open floor for discussion]

---

## Facilitator Notes

**Total Time**: 45-50 minutes including Q&A

**Required Materials**:
- This slide deck
- Printouts of architecture-reviewer-guide.md and general-governance-checklist.md
- Links to governance documents

**Before Meeting**:
- [ ] Send attendees governance overview + quick reference
- [ ] Share links to all docs
- [ ] Have acknowledgment forms ready

**During Meeting**:
- [ ] Go through each slide
- [ ] Allow questions throughout
- [ ] Have Tech Lead available for escalations
- [ ] Take notes on any confusion or concerns

**After Meeting**:
- [ ] Collect signed acknowledgment forms
- [ ] Send recorded session to team (if recorded)
- [ ] Follow up on any outstanding questions
- [ ] Schedule one-on-one reviews if needed

---

**This is a template.** Facilitator should adapt to team size, experience level, and specific questions.

**Execution Date**: September 28, 2026 (before enforcement begins Oct 1)
