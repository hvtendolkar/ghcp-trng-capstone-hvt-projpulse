from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Project, Resource, ResourceAllocation, Invoice, Milestone, BilledHours, WBSCode, FinancialInsight
from schemas import ProjectCreate, ProjectUpdate, ResourceCreate, ResourceAllocationCreate, InvoiceCreate
from decimal import Decimal
from datetime import date

class ProjectService:
    @staticmethod
    def get_all_projects(db: Session, skip: int = 0, limit: int = 100):
        projects = db.query(Project).offset(skip).limit(limit).all()
        total = db.query(func.count(Project.project_id)).scalar()
        return projects, total
    
    @staticmethod
    def get_project(db: Session, project_id: str):
        return db.query(Project).filter(Project.project_id == project_id).first()
    
    @staticmethod
    def create_project(db: Session, project: ProjectCreate, user_id: str):
        db_project = Project(
            **project.dict(),
            created_by=user_id
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    
    @staticmethod
    def update_project(db: Session, project_id: str, project_data: ProjectUpdate):
        db_project = db.query(Project).filter(Project.project_id == project_id).first()
        if db_project:
            for key, value in project_data.dict(exclude_unset=True).items():
                setattr(db_project, key, value)
            db.commit()
            db.refresh(db_project)
        return db_project

class ResourceService:
    @staticmethod
    def get_all_resources(db: Session):
        return db.query(Resource).all()
    
    @staticmethod
    def get_resource(db: Session, resource_id: str):
        return db.query(Resource).filter(Resource.resource_id == resource_id).first()
    
    @staticmethod
    def create_resource(db: Session, resource: ResourceCreate):
        db_resource = Resource(**resource.dict())
        db.add(db_resource)
        db.commit()
        db.refresh(db_resource)
        return db_resource

class FinancialCalculationService:
    @staticmethod
    def calculate_project_wip(db: Session, project_id: str) -> Decimal:
        """Calculate Work In Progress for a project"""
        # Get all invoiced hours that haven't been billed
        wip_records = db.query(func.sum(BilledHours.cost_amount)).filter(
            BilledHours.allocation_id.in_(
                db.query(ResourceAllocation.allocation_id).filter(
                    ResourceAllocation.project_id == project_id
                )
            ),
            BilledHours.status.in_(['Draft', 'Approved'])
        ).scalar()
        return wip_records or Decimal("0")
    
    @staticmethod
    def calculate_project_margin(db: Session, project_id: str) -> float:
        """Calculate margin percentage for a project"""
        project = db.query(Project).filter(Project.project_id == project_id).first()
        if not project:
            return 0.0
        
        # Get revenue (contract value or T&M revenue)
        if project.engagement_type == "Fixed-Cost":
            revenue = project.contract_value or Decimal("0")
        else:
            # T&M: sum of all billed hours
            revenue = db.query(func.sum(BilledHours.cost_amount)).filter(
                BilledHours.allocation_id.in_(
                    db.query(ResourceAllocation.allocation_id).filter(
                        ResourceAllocation.project_id == project_id
                    )
                ),
                BilledHours.status.in_(['Approved', 'Billed', 'Invoiced'])
            ).scalar() or Decimal("0")
        
        # Get cost
        cost = db.query(func.sum(ResourceAllocation.ytd_billed_hours * 
                    func.coalesce(ResourceAllocation.billable_rate_override, 
                                  Resource.default_billable_rate))).join(Resource).filter(
            ResourceAllocation.project_id == project_id
        ).scalar() or Decimal("0")
        
        if revenue == 0:
            return 0.0
        
        margin = float((revenue - cost) / revenue * 100)
        return round(margin, 2)
    
    @staticmethod
    def calculate_invoice_total(db: Session, invoice_id: str) -> Decimal:
        """Calculate invoice total based on line items"""
        total = db.query(func.sum(BilledHours.cost_amount)).filter(
            BilledHours.invoice_id == invoice_id
        ).scalar() or Decimal("0")
        return total

class AIInsightService:
    @staticmethod
    def generate_project_insights(db: Session, project_id: str) -> List[FinancialInsight]:
        """Generate AI insights for a project using Gemma"""
        try:
            import google.generativeai as genai
            from config import settings
            
            # Get project data
            project = db.query(Project).filter(Project.project_id == project_id).first()
            if not project:
                return []
            
            # Get financial metrics
            wip = FinancialCalculationService.calculate_project_wip(db, project_id)
            margin = FinancialCalculationService.calculate_project_margin(db, project_id)
            
            # Prepare prompt
            prompt = f"""
            Analyze the following project financial health and provide insights:
            
            Project: {project.name}
            Status: {project.status}
            Engagement Type: {project.engagement_type}
            Budget: ${project.budget}
            Current WIP: ${wip}
            Current Margin: {margin}%
            
            Provide 3-5 key insights, anomalies, and recommendations in JSON format.
            Focus on financial risks, opportunities, and actionable recommendations.
            """
            
            # Call Gemma API (mock implementation - replace with real API call)
            insights_text = f"Project is operating at {margin}% margin. WIP aging detected at ${wip}."
            
            # Create and store insights
            insights = []
            if margin < 30:
                insight = FinancialInsight(
                    project_id=project_id,
                    insight_type="Anomaly",
                    title="Low Margin Alert",
                    description=f"Project margin at {margin}% is below target of 35%",
                    severity="High",
                    recommendation="Review resource allocation and billing rates",
                    created_by_model="Gemma"
                )
                db.add(insight)
                insights.append(insight)
            
            if wip > Decimal("100000"):
                insight = FinancialInsight(
                    project_id=project_id,
                    insight_type="Risk",
                    title="High WIP Aging",
                    description=f"Project has ${wip} in Work in Progress",
                    severity="High",
                    recommendation="Prioritize invoice generation and payment collection",
                    created_by_model="Gemma"
                )
                db.add(insight)
                insights.append(insight)
            
            db.commit()
            return insights
        except Exception as e:
            print(f"Error generating AI insights: {e}")
            return []
