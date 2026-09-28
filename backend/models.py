from sqlalchemy import Column, String, Integer, Numeric, DateTime, Enum, Boolean, Text, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from decimal import Decimal
from datetime import datetime
import uuid
import enum

class ProjectStatus(str, enum.Enum):
    OPPORTUNITY = "Opportunity"
    ACTIVE = "Active"
    ON_HOLD = "On-Hold"
    COMPLETED = "Completed"
    ARCHIVED = "Archived"

class EngagementType(str, enum.Enum):
    TIME_MATERIAL = "Time & Material"
    FIXED_COST = "Fixed-Cost"
    RETAINER = "Retainer"

class InvoiceStatus(str, enum.Enum):
    DRAFT = "Draft"
    ISSUED = "Issued"
    SENT = "Sent"
    PARTIALLY_PAID = "Partially Paid"
    PAID = "Paid"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String, default="Viewer")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    code = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.ACTIVE)
    engagement_type = Column(Enum(EngagementType))
    start_date = Column(Date)
    end_date = Column(Date)
    contract_value = Column(Numeric(15, 2), nullable=True)
    budget = Column(Numeric(15, 2))
    available_funding = Column(Numeric(15, 2))
    currency = Column(String, default="USD")
    client_name = Column(String)
    billing_manager = Column(String)
    created_by = Column(String, ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    resources = relationship("ResourceAllocation", back_populates="project")
    invoices = relationship("Invoice", back_populates="project")
    milestones = relationship("Milestone", back_populates="project")
    wbs_codes = relationship("WBSCode", back_populates="project")

class Resource(Base):
    __tablename__ = "resources"
    
    resource_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    email = Column(String, unique=True)
    designation = Column(String)
    default_billable_rate = Column(Numeric(10, 2))
    cost_rate = Column(Numeric(10, 2))
    availability_status = Column(String, default="Available")
    skills = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    allocations = relationship("ResourceAllocation", back_populates="resource")

class ResourceAllocation(Base):
    __tablename__ = "resource_allocations"
    
    allocation_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.project_id"))
    resource_id = Column(String, ForeignKey("resources.resource_id"))
    designation = Column(String)
    billable_rate_override = Column(Numeric(10, 2), nullable=True)
    monthly_hours_allocation = Column(Numeric(10, 2))
    start_date = Column(Date)
    end_date = Column(Date)
    total_allocated_hours = Column(Numeric(10, 2))
    ytd_billed_hours = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    project = relationship("Project", back_populates="resources")
    resource = relationship("Resource", back_populates="allocations")

class WBSCode(Base):
    __tablename__ = "wbs_codes"
    
    wbs_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.project_id"))
    code = Column(String)
    description = Column(String)
    allocated_hours = Column(Numeric(10, 2))
    allocated_budget = Column(Numeric(15, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    project = relationship("Project", back_populates="wbs_codes")

class BilledHours(Base):
    __tablename__ = "billed_hours"
    
    billed_hours_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    allocation_id = Column(String, ForeignKey("resource_allocations.allocation_id"))
    wbs_id = Column(String, ForeignKey("wbs_codes.wbs_id"), nullable=True)
    invoice_id = Column(String, ForeignKey("invoices.invoice_id"), nullable=True)
    hours_logged = Column(Numeric(10, 2))
    date_logged = Column(Date)
    description = Column(String)
    cost_amount = Column(Numeric(15, 2))
    status = Column(String, default="Draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Milestone(Base):
    __tablename__ = "milestones"
    
    milestone_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.project_id"))
    name = Column(String)
    description = Column(Text, nullable=True)
    trigger_type = Column(String)
    trigger_value = Column(String)
    invoice_percentage = Column(Numeric(5, 2))
    invoice_amount = Column(Numeric(15, 2), nullable=True)
    target_date = Column(Date)
    actual_date = Column(Date, nullable=True)
    status = Column(String, default="Pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    project = relationship("Project", back_populates="milestones")

class Invoice(Base):
    __tablename__ = "invoices"
    
    invoice_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    invoice_number = Column(String, unique=True, index=True)
    project_id = Column(String, ForeignKey("projects.project_id"))
    milestone_id = Column(String, ForeignKey("milestones.milestone_id"), nullable=True)
    invoice_date = Column(Date)
    due_date = Column(Date)
    total_amount = Column(Numeric(15, 2))
    tax_amount = Column(Numeric(15, 2))
    tax_rate = Column(Numeric(5, 2))
    discount_amount = Column(Numeric(15, 2), nullable=True)
    net_amount = Column(Numeric(15, 2))
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.DRAFT)
    payment_date = Column(Date, nullable=True)
    payment_method = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    attachment_url = Column(String, nullable=True)
    created_by = Column(String, ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    project = relationship("Project", back_populates="invoices")

class FinancialInsight(Base):
    __tablename__ = "financial_insights"
    
    insight_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.project_id"), nullable=True)
    insight_type = Column(String)
    title = Column(String)
    description = Column(Text)
    severity = Column(String)
    recommendation = Column(Text, nullable=True)
    created_by_model = Column(String, default="Gemma-4-26b")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    ttl = Column(Integer, nullable=True)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    audit_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    entity_type = Column(String)
    entity_id = Column(String)
    action = Column(String)
    change_type = Column(String, nullable=True)
    old_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    justification = Column(Text, nullable=True)
