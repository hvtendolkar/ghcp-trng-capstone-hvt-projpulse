from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from decimal import Decimal
from enum import Enum

# Auth Schemas
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: 'UserResponse'

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: str
    email: str
    full_name: str
    role: str
    
    class Config:
        from_attributes = True

# Project Schemas
class ProjectBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    engagement_type: str
    start_date: date
    end_date: date
    budget: Decimal
    available_funding: Decimal
    client_name: str
    billing_manager: str

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    budget: Optional[Decimal] = None
    available_funding: Optional[Decimal] = None

class ProjectResponse(ProjectBase):
    project_id: str
    status: str
    contract_value: Optional[Decimal]
    currency: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    margin: float = 40.0  # Placeholder
    wip: Decimal = Decimal("0")  # Placeholder
    invoicing_status: str = "On Track"  # Placeholder
    
    class Config:
        from_attributes = True

class ProjectList(BaseModel):
    items: List[ProjectResponse]
    total: int
    limit: int
    offset: int

# Resource Schemas
class ResourceBase(BaseModel):
    name: str
    email: str
    designation: str
    default_billable_rate: Decimal
    cost_rate: Decimal

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    resource_id: str
    availability_status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Resource Allocation Schemas
class ResourceAllocationBase(BaseModel):
    project_id: str
    resource_id: str
    designation: str
    monthly_hours_allocation: Decimal
    start_date: date
    end_date: date

class ResourceAllocationCreate(ResourceAllocationBase):
    total_allocated_hours: Optional[Decimal] = None

class ResourceAllocationResponse(ResourceAllocationBase):
    allocation_id: str
    billable_rate_override: Optional[Decimal]
    total_allocated_hours: Decimal
    ytd_billed_hours: Decimal
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Invoice Schemas
class InvoiceBase(BaseModel):
    project_id: str
    invoice_date: date
    due_date: date
    total_amount: Decimal
    tax_amount: Decimal
    tax_rate: Decimal
    discount_amount: Optional[Decimal] = None

class InvoiceCreate(InvoiceBase):
    milestone_id: Optional[str] = None

class InvoiceUpdate(BaseModel):
    status: Optional[str] = None
    payment_date: Optional[date] = None
    payment_method: Optional[str] = None

class InvoiceResponse(InvoiceBase):
    invoice_id: str
    invoice_number: str
    milestone_id: Optional[str]
    net_amount: Decimal
    status: str
    payment_date: Optional[date]
    payment_method: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Analytics Schemas
class DashboardKPIs(BaseModel):
    total_portfolio_value: Decimal
    active_projects: int
    total_wip: Decimal
    average_margin: float
    invoicing_status_summary: dict

class WIPAnalysis(BaseModel):
    total_wip: Decimal
    wip_by_age_bucket: dict
    wip_trend: list

class MarginAnalysis(BaseModel):
    by_project: dict
    by_resource: dict
    by_designation: dict

# AI Insights Schemas
class AIInsightResponse(BaseModel):
    insight_id: str
    project_id: Optional[str]
    insight_type: str
    title: str
    description: str
    severity: str
    recommendation: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class AIAnalysisRequest(BaseModel):
    project_id: str
    analysis_type: str = "project"  # project, portfolio, anomaly

class AIAnalysisResponse(BaseModel):
    insights: List[AIInsightResponse]
    generated_at: datetime
