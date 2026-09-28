# Financial Code Developer Guide: Principle II Implementation

## Overview

As a developer implementing financial features, you must follow **Principle II: Financial Data Integrity & Compliance** to ensure accurate financial data, audit trails, and reconciliation.

This guide shows HOW to implement Principle II in your code.

## The Core Rule: Use DECIMAL for All Money

### Why Not Float?

```python
# ❌ WRONG - Float loses precision
amount1 = 0.1
amount2 = 0.2
total = amount1 + amount2
print(total)  # Outputs: 0.30000000000000004 ❌

# Worse: In financial loops, errors compound
invoices = [9.99, 9.99, 9.99]
total = sum(invoices)
print(total)  # May not equal 29.97
```

### The Decimal Solution

```python
# ✅ CORRECT - Decimal preserves precision
from decimal import Decimal

amount1 = Decimal("0.1")
amount2 = Decimal("0.2")
total = amount1 + amount2
print(total)  # Outputs: Decimal('0.3') ✅ EXACT

# Financial loops work correctly
invoices = [Decimal("9.99"), Decimal("9.99"), Decimal("9.99")]
total = sum(invoices, Decimal("0"))
print(total)  # Exactly Decimal('29.97') ✅
```

**Critical**: Always convert to Decimal from STRING, never from float.

## Principle II Requirements

### 1. Use DECIMAL Type Everywhere

**Database Schema**:
```sql
-- ✅ CORRECT
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    amount DECIMAL(15,2),  -- Allows up to 999,999,999,999.99
    tax_amount DECIMAL(15,2),
    total DECIMAL(15,2)
);

-- ❌ WRONG - Do NOT use FLOAT
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    amount FLOAT,  -- Will have precision errors
    tax_amount FLOAT,
    total FLOAT
);
```

**Python Code**:
```python
from decimal import Decimal, ROUND_HALF_UP

# ✅ Read from database as Decimal
invoice = db.query("SELECT amount, tax FROM invoices WHERE id = ?", [id])
amount = invoice.amount  # Already Decimal from db.Column(DECIMAL)
tax = invoice.tax  # Already Decimal

# ✅ Perform calculations
total = amount + tax

# ✅ Store back as Decimal
invoice.total = total
db.commit()

# ✅ Return to API as string (Decimal can't be JSON serialized)
return {"amount": str(amount), "total": str(total)}
```

**Configuration**:
```python
# In config.py
TAX_RATE = Decimal("0.08")  # 8% tax, not float!
ROUNDING_MODE = ROUND_HALF_UP  # Consistent rounding
DEFAULT_CURRENCY = "USD"
DECIMAL_PLACES = 2  # Always 2 for cents
```

### 2. Single Source of Truth for Calculations

**Problem**: Invoice totals calculated in multiple places
```python
# ❌ BAD - Total calculated twice
def get_invoice_subtotal(invoice_id):
    lines = db.query("SELECT amount FROM invoice_lines WHERE invoice_id = ?")
    return sum(line.amount for line in lines)  # Calculated here

def get_invoice_from_cache(invoice_id):
    return cache.get(f"invoice:{invoice_id}")  # Cached total might differ!

# Now they're out of sync!
```

**Solution**: Calculate once, cache/store result
```python
# ✅ GOOD - Total calculated in ONE place
class InvoiceService:
    def calculate_total(invoice):
        """Single source of truth for invoice totals"""
        subtotal = sum(
            line.amount for line in invoice.lines,
            Decimal("0")
        )
        tax = subtotal * TAX_RATE
        total = subtotal + tax
        return {
            "subtotal": subtotal,
            "tax": tax,
            "total": total
        }
    
    def save_invoice_totals(invoice):
        """Store calculated totals for fast retrieval"""
        totals = self.calculate_total(invoice)
        invoice.subtotal = totals["subtotal"]
        invoice.tax = totals["tax"]
        invoice.total = totals["total"]
        db.commit()
        return totals
    
    def get_invoice(invoice_id):
        """Retrieve pre-calculated totals"""
        return db.query("SELECT * FROM invoices WHERE id = ?", [invoice_id])
        # If totals change, recalculate via save_invoice_totals()
```

**Key**: Lines calculate amounts; only ONE place computes invoice total.

### 3. Immutable Audit Trail Logging

**What to Log**:
- WHO made the change (user_id, username)
- WHEN it was made (timestamp)
- WHAT changed (before value, after value, field name)
- WHY it changed (reason/justification)

**Database Schema**:
```sql
-- Audit trail table (append-only)
CREATE TABLE audit_log (
    audit_id SERIAL PRIMARY KEY,
    entity_type VARCHAR(50),  -- 'invoice', 'payment', etc.
    entity_id INTEGER,
    action VARCHAR(20),  -- 'created', 'updated', 'deleted'
    change_type VARCHAR(50),  -- 'amount_adjustment', 'status_change'
    
    old_value DECIMAL(15,2),
    new_value DECIMAL(15,2),
    field_name VARCHAR(50),
    
    user_id INTEGER,
    timestamp TIMESTAMP DEFAULT NOW(),
    justification TEXT,
    
    CONSTRAINT immutable_audit CHECK (true)  -- Never delete
);

-- Create trigger to prevent deletion
CREATE TRIGGER prevent_audit_deletion
BEFORE DELETE ON audit_log
FOR EACH ROW
EXECUTE FUNCTION raise_audit_error();
```

**Python Code**:
```python
from datetime import datetime
import logging

class AuditTrail:
    def log_financial_change(self, entity_type, entity_id, change):
        """Log financial change to audit trail"""
        log_entry = {
            "entity_type": entity_type,  # 'invoice'
            "entity_id": entity_id,  # invoice_id
            "action": change["action"],  # 'updated'
            "change_type": change["type"],  # 'amount_adjustment'
            "old_value": str(change["old_value"]),  # '100.00' as string
            "new_value": str(change["new_value"]),  # '99.00' as string
            "field_name": change["field"],  # 'amount'
            "user_id": current_user.id,
            "timestamp": datetime.utcnow(),
            "justification": change["reason"],  # 'Customer discount approved'
        }
        
        # Insert into immutable audit table
        db.execute("""
            INSERT INTO audit_log 
            (entity_type, entity_id, action, change_type, old_value, new_value, 
             field_name, user_id, timestamp, justification)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            log_entry["entity_type"],
            log_entry["entity_id"],
            log_entry["action"],
            log_entry["change_type"],
            log_entry["old_value"],
            log_entry["new_value"],
            log_entry["field_name"],
            log_entry["user_id"],
            log_entry["timestamp"],
            log_entry["justification"]
        ))
        db.commit()
        
        # Also log to application logger
        logging.info({
            "event": "financial_change",
            "entity": f"{entity_type}:{entity_id}",
            "change": f"{change['old_value']} → {change['new_value']}",
            "user": current_user.id,
            "reason": change["reason"]
        })

# Usage
audit_trail = AuditTrail()
audit_trail.log_financial_change("invoice", 42, {
    "action": "updated",
    "type": "amount_adjustment",
    "old_value": Decimal("100.00"),
    "new_value": Decimal("99.00"),
    "field": "amount",
    "reason": "Customer early payment discount approved"
})
```

### 4. Input Validation

**Validate Currency Codes**:
```python
ALLOWED_CURRENCIES = {"USD", "EUR", "GBP"}

def validate_currency(currency):
    if currency not in ALLOWED_CURRENCIES:
        raise ValueError(f"Invalid currency: {currency}. Allowed: {ALLOWED_CURRENCIES}")
    return currency

# Usage
currency = validate_currency("USD")  # ✅
currency = validate_currency("BITCOIN")  # ❌ Raises error
```

**Validate Amount Ranges**:
```python
def validate_amount(amount, min_val=Decimal("0"), max_val=None):
    """Validate financial amounts"""
    if not isinstance(amount, Decimal):
        raise TypeError(f"Amount must be Decimal, not {type(amount)}")
    
    if amount < min_val:
        raise ValueError(f"Amount {amount} below minimum {min_val}")
    
    if max_val and amount > max_val:
        raise ValueError(f"Amount {amount} exceeds maximum {max_val}")
    
    # Check decimal places (currency typically 2)
    if amount.as_tuple().exponent < -2:
        raise ValueError(f"Amount {amount} has too many decimal places")
    
    return amount

# Usage
amount = validate_amount(Decimal("99.99"))  # ✅
amount = validate_amount(Decimal("99.999"))  # ❌ Too many decimal places
amount = validate_amount(Decimal("-10"))  # ❌ Negative (if not allowed)
```

**Validate Calculations**:
```python
def validate_invoice_totals(invoice):
    """Verify invoice calculation correctness"""
    # Verify line items sum to subtotal
    line_sum = sum(line.amount for line in invoice.lines, Decimal("0"))
    if line_sum != invoice.subtotal:
        raise ValueError(f"Line items ({line_sum}) don't match subtotal ({invoice.subtotal})")
    
    # Verify tax calculation
    expected_tax = invoice.subtotal * TAX_RATE
    if abs(invoice.tax - expected_tax) > Decimal("0.01"):  # Allow 1 cent rounding difference
        raise ValueError(f"Tax ({invoice.tax}) doesn't match calculation ({expected_tax})")
    
    # Verify total
    expected_total = invoice.subtotal + invoice.tax
    if invoice.total != expected_total:
        raise ValueError(f"Total ({invoice.total}) doesn't match calculation ({expected_total})")
    
    return True
```

### 5. Reconciliation Process

**What to Reconcile**:
- Sum of all line items should equal invoice totals
- Sum of all invoices should equal revenue total
- Tax calculations should match formula
- Payments should match invoice amounts

**Implementation**:
```python
class ReconciliationService:
    def reconcile_invoices(self, start_date, end_date):
        """Monthly reconciliation of financial data"""
        
        # Reconcile line items to invoice totals
        invoices = db.query("""
            SELECT id, subtotal FROM invoices 
            WHERE created_date BETWEEN ? AND ?
        """, [start_date, end_date])
        
        discrepancies = []
        for invoice in invoices:
            lines_sum = db.query("""
                SELECT SUM(amount) as total FROM invoice_lines 
                WHERE invoice_id = ?
            """, [invoice.id])
            
            if lines_sum != invoice.subtotal:
                discrepancies.append({
                    "invoice_id": invoice.id,
                    "expected": lines_sum,
                    "actual": invoice.subtotal,
                    "difference": abs(lines_sum - invoice.subtotal)
                })
        
        if discrepancies:
            # Log discrepancies for investigation
            for disc in discrepancies:
                logging.error({
                    "event": "reconciliation_failure",
                    "invoice_id": disc["invoice_id"],
                    "difference": str(disc["difference"])
                })
            return {"status": "FAILED", "discrepancies": discrepancies}
        
        return {"status": "SUCCESS", "invoices_checked": len(invoices)}

# Usage - run monthly
reconciliation = ReconciliationService()
result = reconciliation.reconcile_invoices(
    start_date=datetime(2026, 10, 1),
    end_date=datetime(2026, 10, 31)
)
if result["status"] != "SUCCESS":
    # Alert finance team
    send_alert("Reconciliation failed", result)
```

## Testing Financial Code

### Unit Tests (Test Individual Calculations)

```python
import pytest
from decimal import Decimal

def test_invoice_total_calculation():
    """Test invoice total = subtotal + tax"""
    subtotal = Decimal("100.00")
    tax_rate = Decimal("0.08")
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    assert total == Decimal("108.00")
    assert tax == Decimal("8.00")

def test_decimal_precision_preserved():
    """Ensure Decimal doesn't lose precision"""
    amount1 = Decimal("0.1")
    amount2 = Decimal("0.2")
    result = amount1 + amount2
    
    assert result == Decimal("0.3")  # Exact, not 0.30000...

def test_negative_amounts_rejected():
    """Verify negative amounts are caught"""
    with pytest.raises(ValueError):
        validate_amount(Decimal("-10.00"))

def test_invalid_currency_rejected():
    """Verify invalid currencies are caught"""
    with pytest.raises(ValueError):
        validate_currency("BITCOIN")
```

### Integration Tests (Test Full Flows)

```python
def test_create_and_reconcile_invoice():
    """Full invoice creation and reconciliation"""
    # Create invoice with lines
    invoice = Invoice(id=1)
    invoice.add_line(Item(amount=Decimal("50.00")))
    invoice.add_line(Item(amount=Decimal("50.00")))
    invoice.calculate_totals()
    
    # Verify totals
    assert invoice.subtotal == Decimal("100.00")
    assert invoice.total == Decimal("108.00")  # With 8% tax
    
    # Save to database
    db.save(invoice)
    
    # Retrieve and reconcile
    service = ReconciliationService()
    result = service.reconcile_invoices(
        start_date=datetime.now().date(),
        end_date=datetime.now().date()
    )
    assert result["status"] == "SUCCESS"
```

## Code Review Checklist for Financial Code

Before submitting PR with financial changes:

- [ ] All currency uses DECIMAL type (database + code)
- [ ] Calculations happen in ONE place (single source of truth)
- [ ] All financial changes logged to audit trail
- [ ] Input validation present (currency, amounts, logic)
- [ ] Reconciliation process updated (if applicable)
- [ ] Unit tests for calculations (edge cases included)
- [ ] Integration tests for full workflows
- [ ] No float arithmetic for money
- [ ] Decimal conversions from strings, not floats

## Resources

- [Python Decimal Documentation](https://docs.python.org/3/library/decimal.html)
- [Constitution Principle II](../../.specify/memory/constitution.md#ii-financial-data-integrity--compliance)
- [Financial Compliance Guide](financial-compliance-guide.md)
- [Pre-PR Checklist](developer-pre-pr-checklist.md)

---

**Remember**: In financial code, precision is not optional. Use DECIMAL, audit trails, and reconciliation.

Questions? See FAQ.md or ask your Tech Lead.
