# Financial Data Compliance Guide: Principle II Enforcement

## Overview

As a financial domain expert, you enforce **Principle II: Financial Data Integrity & Compliance** during code review and operations.

Principle II requires:
- **Precise Representation**: DECIMAL currency (never float/double)
- **Single Source of Truth**: No duplicate calculations
- **Complete Audit Trail**: All transactions logged (who, when, what, why)
- **Reconciliation**: Monthly validation of calculations vs. source data
- **Input Validation**: All financial inputs checked for valid ranges and formats

## Critical Rule: NEVER Use Float for Money

### The Float Problem

```python
# ❌ DANGEROUS: Float arithmetic is unreliable
amount1 = 0.1
amount2 = 0.2
total = amount1 + amount2
# Result: 0.30000000000000004 (not exactly 0.3!)

# Even worse in financial calculations:
invoice_lines = [0.1, 0.2, 0.3, 0.4]
total = sum(invoice_lines)  # May not equal 1.0
```

### The Decimal Solution

```python
# ✅ CORRECT: Use Decimal for exact representation
from decimal import Decimal

amount1 = Decimal("0.1")
amount2 = Decimal("0.2")
total = amount1 + amount2
# Result: 0.3 (exactly correct)

# Financial calculations:
from decimal import Decimal, ROUND_HALF_UP
invoice_lines = [Decimal("0.10"), Decimal("0.20"), Decimal("0.30"), Decimal("0.40")]
total = sum(invoice_lines, Decimal("0"))  # Exactly 1.00
```

**Rule**: Any time you touch financial data, use DECIMAL type. No exceptions.

## Review Checklist for Principle II

### Type Safety for Money

- [ ] **All currency uses DECIMAL** (database column type: DECIMAL, not FLOAT)
  - Python: `Decimal` type
  - Database: `DECIMAL(p,s)` e.g., `DECIMAL(19,4)` for $999,999,999,999.9999
  - API: Returned as string or Decimal, not float
  - Configuration: All money amounts in config files as strings

- [ ] **No float coercion** anywhere
  - Check: No `float(amount)` conversions
  - Check: No `int(amount * 100)` tricks (use Decimal arithmetic instead)
  - Check: JSON serialization preserves Decimal precision

### Single Source of Truth

- [ ] **No duplicate calculations**
  - Example problem: Invoice total calculated in 2 places (could differ)
  - Example problem: Portfolio value calculated in multiple modules
  - Solution: Calculation in one place, queried elsewhere

- [ ] **Calculation owner identified**
  - Example: "Invoice Service owns invoice total calculation"
  - Example: "Portfolio Service owns total value calculation"
  - Documentation: Comments explain where each financial figure comes from

### Audit Trail Logging

- [ ] **All transaction changes logged**
  - Example: Invoice status change must log: who, when, from-amount, to-amount, reason
  - Example: Portfolio rebalance must log: who, when, trades executed, balances before/after
  - Format: Structured logging (JSON), not free text

- [ ] **Audit trail immutable**
  - Audit entries never deleted (only marked obsolete if needed)
  - Audit entries include user context (who made change, what time, from which IP/system)
  - Audit entries queryable (can filter by user, date, transaction type)

### Input Validation

- [ ] **Currency code validation**
  - Only accepted currencies allowed (USD, EUR, GBP, etc.)
  - Reject unknown currencies
  - Fail loudly if currency mixing detected

- [ ] **Amount range validation**
  - Reject negative amounts (if not allowed for transaction type)
  - Reject amounts exceeding portfolio size
  - Reject unrealistic amounts (e.g., $1M when portfolio is $10K)
  - Provide clear error messages

- [ ] **Calculation validation**
  - Totals match line items exactly
  - Percentages add to 100% (or specified total)
  - Dates are logical (payment date ≥ invoice date)

### Reconciliation Process

- [ ] **Reconciliation defined**
  - How often? (Monthly, weekly, daily)
  - By whom? (Finance team, automated script)
  - Against what? (Source ledger, bank statements)
  - What's accepted variance? (Usually 0.00, or ±$0.01 for rounding)

- [ ] **Reconciliation automated**
  - Scheduled reconciliation script/job
  - Reconciliation reports generated automatically
  - Reconciliation failures alert finance team
  - Reconciliation logs kept for audit

- [ ] **Discrepancy handling**
  - Procedure for resolving reconciliation differences
  - Root cause analysis requirements
  - Adjustment process (if discrepancy legitimate)
  - Prevention measures for future

## Common Financial Violations

### CRITICAL

**Violation**: Float used for currency calculation
```python
# ❌ CRITICAL: Causes precision loss
def calculate_portfolio_value(holdings):
    total = 0.0  # Using float!
    for holding in holdings:
        total += holding.shares * holding.price
    return total

# ✅ FIX: Use Decimal
from decimal import Decimal
def calculate_portfolio_value(holdings):
    total = Decimal("0")
    for holding in holdings:
        total += holding.shares * Decimal(str(holding.price))
    return total
```

**Violation**: Duplicate calculation (multiple sources of truth)
```python
# ❌ CRITICAL: Invoice total calculated in 2 places
class InvoiceService:
    def get_total(invoice):
        return sum(line.amount for line in invoice.lines)

class BillingService:
    def get_invoice_total(invoice_id):
        return db.query("SUM(amount) FROM invoice_lines WHERE invoice_id=?")

# ✅ FIX: Single source of truth
class InvoiceService:
    def get_total(invoice):
        return invoice.total  # Calculated once, stored/cached

class BillingService:
    def get_invoice_total(invoice_id):
        return InvoiceService.get_total(invoice_by_id(invoice_id))  # Single source
```

**Violation**: No audit trail for financial changes
- Fix: Log all transaction changes with timestamp, user, amounts, reason
- Impact: Can't audit who did what and when

### MAJOR

**Violation**: Input validation missing
- Fix: Add validation for currency, amount ranges, logical dates
- Impact: Invalid financial data can enter system

**Violation**: Reconciliation not documented
- Fix: Document monthly reconciliation process and timeline
- Impact: Can't verify calculations are correct

## Sample PR Review Workflow

**Example PR**: Calculate portfolio rebalancing recommendations

1. **Check Decimal Type**:
   ```python
   # ✅ Good: Decimal used for calculations
   def calculate_rebalance_amounts(portfolio, target_allocation):
       total_value = sum(
           Decimal(holding.shares) * Decimal(str(holding.price))
           for holding in portfolio.holdings
       )
       rebalance_amounts = {}
       for asset_class, target_pct in target_allocation.items():
           current_value = # ... Decimal calculation
           rebalance_amounts[asset_class] = target_value - current_value
       return rebalance_amounts
   ```

2. **Verify Single Source of Truth**:
   - Portfolio value calculation in one place? ✅
   - Rebalance amounts flow through single calculation? ✅
   - No recalculation of same amounts elsewhere? ✅

3. **Check Audit Logging**:
   - Rebalance operations logged? ✅
   - Log includes: who, when, before/after values? ✅
   - Log immutable and queryable? ✅

4. **Verify Input Validation**:
   - Target allocation percentages validated? ✅
   - Asset classes validated against allowed list? ✅
   - Error handling clear if validation fails? ✅

5. **Approval**:
   ```markdown
   ✅ Financial Review - Principle II APPROVED
   
   - DECIMAL used for all calculations
   - Single source of truth for portfolio value
   - Audit logging comprehensive
   - Input validation present
   - Ready for merge
   ```

## Finance Team Review Responsibilities

| Responsibility | When | Who | Details |
|---|---|---|---|
| Principle II verification | Every PR | Finance Expert | Use checklist above |
| Calculation validation | Complex financial PRs | Finance Expert | Spot-check math |
| Reconciliation audit | Monthly | Finance Team | Verify calculations match source |
| Compliance reporting | Monthly | Finance Lead | Report to leadership |

## Escalation Path

Request changes if:
- Float used for currency
- Duplicate calculations detected
- Audit trail missing or incomplete
- Input validation insufficient
- Reconciliation process unclear

Escalate to Tech Lead if:
- Systematic financial issues across team
- Architecture prevents audit trail
- Reconciliation process can't be automated
- Data integrity risk identified

## Resources

- [Constitution Principle II](../../.specify/memory/constitution.md#ii-financial-data-integrity--compliance)
- [Python Decimal Documentation](https://docs.python.org/3/library/decimal.html)
- [General Governance Checklist](../../specs/001-project-governance/contracts/general-governance-checklist.md)
- [Compliance Audit Procedures](compliance-audit-procedures.md)

## Questions?

Contact Financial Domain Expert or Tech Lead.
