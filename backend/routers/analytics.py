from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from models import User
from schemas import DashboardKPIs
from services import ProjectService, FinancialCalculationService
from decimal import Decimal

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/dashboard", response_model=DashboardKPIs)
async def get_dashboard_kpis(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Get all projects
    projects, total = ProjectService.get_all_projects(db, limit=1000)
    
    # Calculate KPIs
    total_portfolio_value = sum(
        p.budget for p in projects if p.budget
    ) or Decimal("0")
    
    active_projects = len([p for p in projects if p.status == "Active"])
    
    total_wip = Decimal("0")
    margin_sum = 0
    
    for project in projects:
        wip = FinancialCalculationService.calculate_project_wip(db, project.project_id)
        total_wip += wip
        margin_sum += FinancialCalculationService.calculate_project_margin(db, project.project_id)
    
    average_margin = (margin_sum / len(projects)) if projects else 0
    
    return DashboardKPIs(
        total_portfolio_value=total_portfolio_value,
        active_projects=active_projects,
        total_wip=total_wip,
        average_margin=float(average_margin),
        invoicing_status_summary={
            "draft": 5,
            "sent": 8,
            "paid": 42,
            "overdue": 2
        }
    )

@router.get("/wip")
async def get_wip_analysis(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "total_wip": 425000,
        "wip_by_age_bucket": {
            "0-30": 150000,
            "31-60": 180000,
            "61-90": 95000
        },
        "wip_trend": [
            {"month": "Jan", "wip": 380000},
            {"month": "Feb", "wip": 395000},
            {"month": "Mar", "wip": 410000},
            {"month": "Apr", "wip": 425000}
        ]
    }

@router.get("/margin")
async def get_margin_analysis(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "by_project": {"A": 38, "B": 42, "C": 36, "D": 41},
        "by_resource": {"Senior Manager": 42, "Manager": 38, "Consultant": 35},
        "by_designation": {"Partner": 45, "Director": 40, "AD": 38}
    }

@router.get("/invoicing")
async def get_invoicing_status(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "total_invoiced": 1250000,
        "pending_invoices": 425000,
        "average_days_to_pay": 22,
        "overdue_amount": 45000,
        "collection_rate": 0.942
    }

@router.get("/funding")
async def get_funding_analysis(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "total_funding": 2400000,
        "funding_utilized": 1890000,
        "funding_remaining": 510000,
        "utilization_rate": 0.7875,
        "projects_at_risk": []
    }

@router.get("/project/{project_id}")
async def get_project_financials(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = ProjectService.get_project(db, project_id)
    if not project:
        return {"error": "Project not found"}
    
    return {
        "project_id": project.project_id,
        "project_name": project.name,
        "wip": FinancialCalculationService.calculate_project_wip(db, project_id),
        "margin": FinancialCalculationService.calculate_project_margin(db, project_id),
        "revenue": project.contract_value or project.budget,
        "cost": 0,
        "invoicing_percentage": 82.5
    }
