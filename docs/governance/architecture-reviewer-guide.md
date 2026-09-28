# Architecture Reviewer Guide: Principle III Enforcement

## Overview

As an architecture reviewer, you enforce **Principle III: Scalable API-First Architecture** during code review.

Principle III requires:
- **Stateless & Stateful Services**: Clean separation, scalable design
- **Well-Defined Contracts**: Documented OpenAPI/Pydantic schemas
- **Modular Design**: Business logic by domain, minimal coupling
- **Database Integrity**: Migrations, constraints, rollback procedures

## Review Checklist for Principle III

### API Contract Compliance

- [ ] **OpenAPI/Pydantic Schemas**: All endpoints have documented schemas
  - Request format clearly specified
  - Response format clearly specified
  - Error responses documented
  - Example payloads provided

- [ ] **Backward Compatibility**: Changes maintain 2+ major version compatibility
  - No breaking changes to existing endpoints
  - New fields are optional or have defaults
  - Deprecated fields have migration path
  - Deprecation timeline communicated

### Database Design & Integrity

- [ ] **Schema Migrations**: Changes use migrations, not direct alterations
  - Migration files created and tested
  - Rollback procedures documented
  - Data migration handled safely
  - No data loss on rollback

- [ ] **Constraints & Integrity**: Foreign keys and checks enforced
  - Foreign key constraints defined
  - Check constraints for business rules
  - Cascade behaviors specified
  - No orphaned records possible

### Modular Architecture

- [ ] **Domain Boundaries**: Business logic organized by domain
  - Projects domain: project management
  - Resources domain: resource allocation
  - Invoicing domain: billing and revenue
  - AI Insights domain: model predictions
  - Clear separation of concerns

- [ ] **Minimal Coupling**: Domains interact through defined interfaces
  - No direct database access across domains
  - API calls between domains documented
  - Circular dependencies prevented
  - Testable in isolation

### Deployment & Rollback

- [ ] **Deployment Readiness**: Changes deployable with zero downtime
  - Schema migrations backward compatible
  - Code rollback doesn't corrupt data
  - Feature flags for major changes
  - Rollback procedure tested

## Common Architecture Violations

### CRITICAL

**Violation**: Float/double used for monetary amounts (Principle II spillover)
- Fix: Replace with DECIMAL type
- Impact: Causes financial precision loss

**Violation**: Breaking API change without deprecation period
- Fix: Maintain backward compatibility, deprecate old version
- Impact: Breaks client integrations

### MAJOR

**Violation**: Direct schema modification instead of migration
- Fix: Create migration file, test rollback
- Impact: Can't rollback if deployment fails

**Violation**: Foreign key missing (data integrity risk)
- Fix: Add foreign key constraint
- Impact: Orphaned records can exist

**Violation**: Circular domain dependencies
- Fix: Refactor to break cycle
- Impact: Increases coupling, harder to test

### MINOR

**Violation**: API documentation outdated
- Fix: Update schema documentation
- Impact: Confusion about API usage

**Violation**: Deployment procedure not documented
- Fix: Document in PR or wiki
- Impact: Manual deployment error risk

## Sample PR Review Workflow

**Example PR**: Add financial portfolio analysis endpoint

1. **Check OpenAPI Contract**:
   ```python
   # ✅ Good: Pydantic schema documented
   class PortfolioAnalysisRequest(BaseModel):
       portfolio_id: str
       include_recommendations: bool = False
   
   # ✅ Good: Response schema clear
   class PortfolioAnalysisResponse(BaseModel):
       portfolio_id: str
       total_value: Decimal
       risk_score: float
       recommendations: List[str]
   ```

2. **Verify Backward Compatibility**:
   - Old clients can still call endpoint? ✅
   - New fields have defaults? ✅
   - Deprecated fields handled? ✅

3. **Check Database Changes**:
   - Migration file created? ✅
   - Foreign keys added? ✅
   - Rollback tested? ✅

4. **Verify Modular Design**:
   - Uses Portfolio domain service? ✅
   - Doesn't bypass API layer? ✅
   - No circular dependencies? ✅

5. **Approval**:
   ```markdown
   ✅ Architecture Review - Principle III APPROVED
   
   - OpenAPI contracts well-defined
   - Backward compatibility maintained
   - Database migration tested
   - Modular design clean
   - Ready for merge
   ```

## When to Request Changes

Request changes if:
- API contract not documented
- Breaking change without deprecation
- Direct schema modification instead of migration
- Foreign key constraints missing
- Circular domain dependencies
- Feature cross-cuts multiple domains without clear interface

## When to Request Architecture Redesign

Escalate for redesign if:
- Fundamental architectural flaw
- Significant coupling between domains
- Database schema design poor
- Performance implications unclear
- Scalability concerns

## Resources

- [Constitution Principle III](../../.specify/memory/constitution.md#iii-scalable-api-first-architecture)
- [General Governance Checklist](../../specs/001-project-governance/contracts/general-governance-checklist.md)
- [Reviewer Procedures](reviewer-procedures.md)
- [OpenAPI Specification](https://swagger.io/specification/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Questions?

Contact Architecture Owner or Tech Lead.
