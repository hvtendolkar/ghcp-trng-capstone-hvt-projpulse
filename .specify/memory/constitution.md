---
version: 1.0.0
title: ProjectPulse AI Governance Constitution
ratified_date: 2026-09-28
effective_date: 2026-09-28
last_amended_date: 2026-09-28
next_amendment_due: null
amendment_count: 0
amendment_history:
  - version: 1.0.0
    ratified_date: 2026-09-28
    effective_date: 2026-09-28
    description: Initial governance constitution ratification
maintenance_schedule: Monthly review, amendment proposals annually
---

# ProjectPulse AI Constitution

A governance framework for building intelligent financial portfolio analysis for Big 4 consulting partners and leadership.

## Core Principles

### I. AI-Driven Financial Intelligence (MANDATORY)

Every feature that provides financial insights MUST leverage the Gemma AI engine for analysis, pattern detection, or prediction. AI-generated insights must be:
- **Transparent**: Clearly marked as AI-generated with confidence levels and reasoning disclosed
- **Validated**: Cross-checked against raw financial data; anomaly detection must have fallback rules when AI confidence < threshold
- **Auditable**: All AI decisions logged with input parameters and decision timestamps for compliance review
- **Configurable**: Parameters and model versions tracked; ability to replay historical analyses with different model versions

Rationale: ProjectPulse AI's core value proposition is intelligent financial analysis. Without AI-driven insights at every major decision point, the product becomes a standard dashboard. Financial accuracy for Big 4 firms requires transparency and auditability.

### II. Financial Data Integrity & Compliance (NON-NEGOTIABLE)

All financial data flowing through the system MUST maintain accuracy, traceability, and regulatory compliance:
- **Single Source of Truth**: Each financial metric has one authoritative calculation point; no conflicting calculations across endpoints
- **Immutable Audit Trail**: All data modifications logged with user, timestamp, justification, and pre/post values
- **Precision**: Currency amounts stored with proper precision (DECIMAL type, never float); calculations follow Big 4 accounting standards
- **Reconciliation**: Monthly reconciliation checks between WIP, invoicing, and revenue recognition; discrepancies trigger alerts
- **Data Validation**: Input validation at API boundary; no unvalidated financial figures stored in database

Rationale: Portfolio managers at Big 4 firms make multi-million-dollar decisions based on this data. Accuracy and compliance are non-negotiable; a single reconciliation error damages trust and exposes the firm to audit risk.

### III. Scalable API-First Architecture

The backend MUST be designed as a clean, layered FastAPI service with clear separation of concerns:
- **Stateless & Stateful Services**: Stateless request handlers for scalability; state stored only in PostgreSQL with consistent schema versioning
- **Well-Defined Contracts**: Every endpoint has documented request/response schemas (OpenAPI/Pydantic); backward compatibility MUST be maintained for 2+ minor versions
- **Modular Design**: Business logic organized by domain (Projects, Resources, Invoicing, AI Insights) with clear boundaries and minimal coupling
- **Database Integrity**: Foreign key constraints enforced; schema migrations tested before deployment; rollback procedures documented

Rationale: ProjectPulse AI must scale to handle hundreds of concurrent portfolio managers across multiple Big 4 offices. API contracts and database integrity ensure teams can work in parallel without breaking each other's work.

### IV. Test-Driven Development & Quality Gates

All code contributions MUST follow strict testing discipline:
- **Unit Test Coverage**: Minimum 80% coverage for business logic; financial calculation tests MUST verify edge cases (negative amounts, rounding, currency conversion)
- **Integration Tests**: All API endpoints have happy-path and error-case tests; AI engine calls tested with mock responses before real API integration
- **Database Tests**: Schema migrations tested in isolation; transaction rollback scenarios covered
- **Manual Review Gate**: PRs cannot merge without passing automated tests AND manual review from a financial-domain expert or AI systems reviewer
- **Regression Prevention**: Every bug fix includes a test that fails before the fix and passes after

Rationale: Financial systems are unforgiving; bugs in margin calculations or WIP tracking directly impact business decisions. Test discipline prevents costly reconciliation issues and maintains system reliability.

## Technology Stack Requirements

**Frontend**: React + TypeScript for type-safe dashboard development; Zustand or Redux for state management (confirm during implementation)

**Backend**: FastAPI (Python 3.10+) with async support; Pydantic for schema validation and OpenAPI documentation

**Database**: PostgreSQL 14+ with proper indexing on financial metrics tables; prepared statements MUST be used for all dynamic queries

**AI Integration**: Google Gemma AI API (via official SDK); rate limiting and retry logic MUST be implemented; fallback to rule-based analysis if API unavailable

**DevOps**: Docker containerization for reproducible environments; GitHub Actions for CI/CD; staging environment MUST mirror production schema and data volumes

## Development Workflow

1. **Planning**: Features defined in spec-kit `/speckit-specify` command; acceptance criteria tied to financial accuracy requirements
2. **Implementation**: Code reviewed against constitution principles; AI features validated against expected confidence levels
3. **Testing**: All tests MUST pass locally before PR submission; CI pipeline enforces automated gate
4. **Review**: PR requires approval from architecture owner + at least one financial-domain reviewer for money-related code
5. **Deployment**: Staged rollout; production deployments MUST include database backup and rollback procedure
6. **Monitoring**: Production dashboards track API response time, error rates, and AI model inference latency; financial calculation anomalies trigger alerts

## Governance

**Constitution Supremacy**: This constitution supersedes informal team practices. When guidance conflicts with code standards or previous decisions, constitution rules apply.

**Amendment Process**: Proposed changes to core principles MUST include:
- Written justification explaining why existing principle is insufficient
- Impact analysis on existing features and commitments
- Migration plan for affected systems
- Approval from tech lead + at least one AI/financial systems expert

**Compliance Review**: All PRs checked for compliance; violations flagged in code review. Monthly constitution compliance audit of random merged PRs (sample size: 5-10% of PRs from prior month).

**Version Bumping**: 
- MAJOR: Removal/redefinition of core principle (rare; requires explicit approval)
- MINOR: New principle/section added or existing guidance significantly expanded
- PATCH: Clarifications, wording fixes, non-semantic refinements

**Runtime Guidance**: Detailed implementation patterns documented separately in `.instructions.md` and skill-specific guides. This constitution states the "what and why"; instructions state the "how."

---

**Version**: 1.0.0 | **Ratified**: 2026-09-28 | **Last Amended**: 2026-09-28
