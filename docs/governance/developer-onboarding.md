# Developer Onboarding: Understanding Governance

Welcome to ProjectPulse AI! This guide explains how the governance framework applies to your work.

## What is Governance?

Governance = **Shared principles that guide how we write code together**

The governance framework establishes 4 mandatory principles:
- **Principle I**: AI insights must be transparent and auditable
- **Principle II**: Financial data must be precise and auditable  
- **Principle III**: Architecture must be clean and scalable
- **Principle IV**: All code must follow TDD discipline

## Reading the Constitution

Start with [Constitution](../../.specify/memory/constitution.md) - it's the source of truth for all governance principles.

**Time commitment**: 15 minutes to read and understand

Each principle explains:
- What it requires
- Why it matters for ProjectPulse AI
- How it affects your work

## How Governance Applies to Different Roles

### Backend Developers
- Write code that follows **Principle III** (API contracts, database integrity)
- Write tests that achieve **Principle IV** (80% coverage minimum)
- Follow **Principle II** requirements if touching financial data (DECIMAL precision, audit trails)
- Follow **Principle I** requirements if integrating AI features (transparency, auditability)

### Frontend Developers
- Write tests that achieve **Principle IV** (80% coverage minimum)
- Follow API contracts defined by **Principle III**
- Understand how backend data integrity (**Principle II**) impacts frontend data display

### QA Engineers
- Write integration tests that verify **Principle IV** test requirements
- Verify that financial calculations follow **Principle II** (precision, reconciliation)
- Test AI features for **Principle I** compliance (transparency, confidence scores, audit logs)
- Verify architecture team's **Principle III** enforcement

### Tech Lead / Architects
- Enforce all principles during code review
- Approve architectural decisions against **Principle III** standards
- Coordinate with domain experts for **Principle I** and **Principle II** reviews
- Ensure **Principle IV** testing standards are met

## Applying Governance to Your Code

### Before You Start Coding

1. **Identify which principles apply to your feature**
   - Does it involve AI? → **Principle I**
   - Does it involve financial data? → **Principle II**
   - Does it change API/database? → **Principle III**
   - All code? → **Principle IV** (always applies)

2. **Read principle-specific guides**
   - See `docs/governance/` for guides by principle
   - Ask your tech lead if you're unsure

### While You're Coding

1. **Follow principle requirements in your implementation**
   - Use DECIMAL for financial amounts (Principle II)
   - Add confidence scores and logging to AI code (Principle I)
   - Maintain API backwards compatibility (Principle III)
   - Write unit and integration tests as you code (Principle IV)

2. **Use the developer pre-PR checklist**
   - See [Developer Pre-PR Checklist](developer-pre-pr-checklist.md)
   - Verify your code meets governance requirements before submitting PR

### When You Submit a PR

1. **Fill out the PR template**
   - The template includes governance checklist sections
   - Mark which principles apply to your changes
   - Reference principle-specific requirements you followed

2. **Expect governance review**
   - Architecture team will review for **Principle III** compliance
   - Financial domain expert will review for **Principle II** compliance (if applicable)
   - AI systems reviewer will review for **Principle I** compliance (if applicable)
   - Tech lead will verify **Principle IV** testing standards

3. **Address governance feedback**
   - Reviewer feedback helps ensure consistency
   - Ask for clarification if guidance is unclear
   - Implement requested changes and resubmit

## Key Governance Concepts

### Principle I: AI-Driven Insights
- AI models must be documented (which model? which version?)
- Confidence scores must be calculated and exposed
- AI decisions must be logged for audit
- Parameters must be configurable (not hardcoded)

**Example**: Financial prediction feature logs: `{"model": "financial-model-v2", "confidence": 0.87, "prediction": 2.5M, "threshold": 0.80, "timestamp": ...}`

### Principle II: Financial Data Integrity
- Use DECIMAL type (never float/double) for currency
- Every financial change must be logged (who, when, why, before/after values)
- Calculations must reconcile to authoritative sources
- All financial inputs must be validated (range checks, currency validation)

**Example**: Transaction service logs: `{"operation": "calculate_revenue", "amount": DECIMAL("1234.56"), "user": "alice", "timestamp": "2026-09-28T10:15:00Z", "audit_trail_id": "audit-123456"}`

### Principle III: Scalable Architecture
- Every API endpoint must have documented request/response schemas
- Database schema changes must be migrations (not migrations)
- API contracts must be maintained for 2+ major versions
- Foreign keys and integrity constraints must be enforced

**Example**: Endpoints define schemas in `docs/api/endpoints.md`, migrations in `database/migrations/`, and backward compatibility documented.

### Principle IV: Test-Driven Development
- Minimum 80% code coverage for business logic
- Unit tests for individual functions
- Integration tests for full request/response workflows
- Database tests for migrations and transactions
- Financial calculation tests must cover edge cases (negative amounts, rounding, currency conversion)

**Example**: Test coverage verified by CI/CD pipeline before merge, reported in PR.

## Common Questions

**Q: What if my code doesn't meet governance requirements?**
A: Reviewer will request changes. You'll update your code to comply and resubmit for review.

**Q: Can I get an exception to governance principles?**
A: Exceptions are rare. Talk to your tech lead. If needed, follow the amendment process in [Amendment Process](amendment-process.md) to propose a change.

**Q: Who do I ask for help with governance?**
A: Your tech lead is your first stop. Also see [FAQ](FAQ.md).

**Q: How often will compliance be checked?**
A: Every PR goes through compliance review. Plus, monthly audits sample 5-10 random PRs to verify ongoing compliance.

## Next Steps

1. **Read the Constitution**: [.specify/memory/constitution.md](../../.specify/memory/constitution.md) - 15 minutes
2. **Read Your Role-Specific Guide**: Check `docs/governance/` for your discipline (developer, architect, tester)
3. **Review Pre-PR Checklist**: [Developer Pre-PR Checklist](developer-pre-pr-checklist.md) before your next PR
4. **Attend Training**: Scheduled training sessions by role and principle
5. **Ask Questions**: If anything is unclear, ask your tech lead

## Support

- **Questions**: See [FAQ](FAQ.md) or ask your tech lead
- **Need Governance Help**: Message tech lead in team chat
- **Report a Violation**: Use GitHub [governance-violation template](../../.github/ISSUE_TEMPLATE/governance-violation.md)
- **Propose Amendment**: See [Amendment Process](amendment-process.md)

Welcome to the team! 🚀
