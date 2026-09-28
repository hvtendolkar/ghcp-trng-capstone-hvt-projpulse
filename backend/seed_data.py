#!/usr/bin/env python3
"""
Script to seed the database with mock data for testing
"""
import sys
from datetime import datetime, date, timedelta
from decimal import Decimal
from database import SessionLocal, engine, Base
from models import (
    Project, Resource, ResourceAllocation, Invoice, BilledHours, 
    Milestone, WBSCode, FinancialInsight, User, ProjectStatus, 
    EngagementType, InvoiceStatus
)

def create_mock_data():
    """Create and insert mock data into the database"""
    db = SessionLocal()
    
    try:
        # Get the admin user
        admin_user = db.query(User).filter(User.email == "admin@company.com").first()
        if not admin_user:
            print("Admin user not found. Please run the setup first.")
            return
        
        admin_id = admin_user.user_id
        
        # Create Resources
        print("Creating resources...")
        resources = [
            Resource(
                name="John Smith",
                email="john.smith@company.com",
                designation="Senior Manager",
                default_billable_rate=Decimal("350.00"),
                cost_rate=Decimal("150.00"),
                skills=["Project Management", "Strategic Planning", "Risk Management"]
            ),
            Resource(
                name="Sarah Johnson",
                email="sarah.johnson@company.com",
                designation="Senior Consultant",
                default_billable_rate=Decimal("280.00"),
                cost_rate=Decimal("120.00"),
                skills=["Data Analysis", "Financial Planning", "Consulting"]
            ),
            Resource(
                name="Mike Chen",
                email="mike.chen@company.com",
                designation="Consultant",
                default_billable_rate=Decimal("200.00"),
                cost_rate=Decimal("85.00"),
                skills=["Financial Analysis", "Process Improvement", "Training"]
            ),
            Resource(
                name="Lisa Martinez",
                email="lisa.martinez@company.com",
                designation="Analyst",
                default_billable_rate=Decimal("150.00"),
                cost_rate=Decimal("60.00"),
                skills=["Analysis", "Reporting", "Data Management"]
            ),
        ]
        db.add_all(resources)
        db.commit()
        print(f"Created {len(resources)} resources")
        
        # Create Projects
        print("Creating projects...")
        today = date.today()
        projects = [
            Project(
                name="Digital Transformation Initiative",
                code="PROJ-001",
                description="Comprehensive digital transformation for Fortune 500 client",
                status=ProjectStatus.ACTIVE,
                engagement_type=EngagementType.TIME_MATERIAL,
                start_date=today - timedelta(days=90),
                end_date=today + timedelta(days=90),
                contract_value=Decimal("500000.00"),
                budget=Decimal("500000.00"),
                available_funding=Decimal("250000.00"),
                client_name="Acme Corporation",
                billing_manager="John Smith",
                created_by=admin_id
            ),
            Project(
                name="Cloud Migration Project",
                code="PROJ-002",
                description="Migration of on-premise infrastructure to AWS cloud",
                status=ProjectStatus.ACTIVE,
                engagement_type=EngagementType.FIXED_COST,
                start_date=today - timedelta(days=60),
                end_date=today + timedelta(days=120),
                contract_value=Decimal("350000.00"),
                budget=Decimal("350000.00"),
                available_funding=Decimal("175000.00"),
                client_name="Tech Solutions Inc",
                billing_manager="Sarah Johnson",
                created_by=admin_id
            ),
            Project(
                name="Financial Systems Optimization",
                code="PROJ-003",
                description="ERP system optimization and consolidation",
                status=ProjectStatus.ACTIVE,
                engagement_type=EngagementType.TIME_MATERIAL,
                start_date=today - timedelta(days=30),
                end_date=today + timedelta(days=180),
                contract_value=Decimal("450000.00"),
                budget=Decimal("450000.00"),
                available_funding=Decimal("300000.00"),
                client_name="Global Finance Ltd",
                billing_manager="Mike Chen",
                created_by=admin_id
            ),
            Project(
                name="Business Process Automation",
                code="PROJ-004",
                description="RPA implementation for back-office operations",
                status=ProjectStatus.ACTIVE,
                engagement_type=EngagementType.RETAINER,
                start_date=today - timedelta(days=45),
                end_date=today + timedelta(days=270),
                contract_value=Decimal("300000.00"),
                budget=Decimal("300000.00"),
                available_funding=Decimal("150000.00"),
                client_name="Enterprise Solutions Group",
                billing_manager="Lisa Martinez",
                created_by=admin_id
            ),
        ]
        db.add_all(projects)
        db.commit()
        print(f"Created {len(projects)} projects")
        
        # Create Resource Allocations
        print("Creating resource allocations...")
        allocations = [
            ResourceAllocation(
                project_id=projects[0].project_id,
                resource_id=resources[0].resource_id,
                designation="Project Lead",
                monthly_hours_allocation=Decimal("160"),
                start_date=today - timedelta(days=90),
                end_date=today + timedelta(days=90),
                total_allocated_hours=Decimal("800"),
                ytd_billed_hours=Decimal("650")
            ),
            ResourceAllocation(
                project_id=projects[0].project_id,
                resource_id=resources[1].resource_id,
                designation="Senior Analyst",
                monthly_hours_allocation=Decimal("120"),
                start_date=today - timedelta(days=90),
                end_date=today + timedelta(days=90),
                total_allocated_hours=Decimal("600"),
                ytd_billed_hours=Decimal("520")
            ),
            ResourceAllocation(
                project_id=projects[1].project_id,
                resource_id=resources[1].resource_id,
                designation="Technical Lead",
                monthly_hours_allocation=Decimal("160"),
                start_date=today - timedelta(days=60),
                end_date=today + timedelta(days=120),
                total_allocated_hours=Decimal("560"),
                ytd_billed_hours=Decimal("420")
            ),
            ResourceAllocation(
                project_id=projects[1].project_id,
                resource_id=resources[2].resource_id,
                designation="Developer",
                monthly_hours_allocation=Decimal("120"),
                start_date=today - timedelta(days=60),
                end_date=today + timedelta(days=120),
                total_allocated_hours=Decimal("420"),
                ytd_billed_hours=Decimal("280")
            ),
            ResourceAllocation(
                project_id=projects[2].project_id,
                resource_id=resources[2].resource_id,
                designation="Financial Analyst",
                monthly_hours_allocation=Decimal("160"),
                start_date=today - timedelta(days=30),
                end_date=today + timedelta(days=180),
                total_allocated_hours=Decimal("1040"),
                ytd_billed_hours=Decimal("340")
            ),
            ResourceAllocation(
                project_id=projects[3].project_id,
                resource_id=resources[3].resource_id,
                designation="RPA Specialist",
                monthly_hours_allocation=Decimal("80"),
                start_date=today - timedelta(days=45),
                end_date=today + timedelta(days=270),
                total_allocated_hours=Decimal("1040"),
                ytd_billed_hours=Decimal("240")
            ),
        ]
        db.add_all(allocations)
        db.commit()
        print(f"Created {len(allocations)} resource allocations")
        
        # Create WBS Codes
        print("Creating WBS codes...")
        wbs_codes = [
            WBSCode(
                project_id=projects[0].project_id,
                code="PROJ-001-001",
                description="Discovery and Assessment",
                allocated_hours=Decimal("200"),
                allocated_budget=Decimal("75000.00")
            ),
            WBSCode(
                project_id=projects[0].project_id,
                code="PROJ-001-002",
                description="Solution Design",
                allocated_hours=Decimal("300"),
                allocated_budget=Decimal("125000.00")
            ),
            WBSCode(
                project_id=projects[0].project_id,
                code="PROJ-001-003",
                description="Implementation",
                allocated_hours=Decimal("500"),
                allocated_budget=Decimal("250000.00")
            ),
            WBSCode(
                project_id=projects[1].project_id,
                code="PROJ-002-001",
                description="Infrastructure Planning",
                allocated_hours=Decimal("150"),
                allocated_budget=Decimal("80000.00")
            ),
            WBSCode(
                project_id=projects[1].project_id,
                code="PROJ-002-002",
                description="Cloud Setup and Migration",
                allocated_hours=Decimal("400"),
                allocated_budget=Decimal("200000.00")
            ),
        ]
        db.add_all(wbs_codes)
        db.commit()
        print(f"Created {len(wbs_codes)} WBS codes")
        
        # Create Invoices
        print("Creating invoices...")
        invoices = [
            Invoice(
                invoice_number="INV-2026-001",
                project_id=projects[0].project_id,
                invoice_date=today - timedelta(days=45),
                due_date=today - timedelta(days=15),
                total_amount=Decimal("125000.00"),
                tax_amount=Decimal("10000.00"),
                tax_rate=Decimal("8.00"),
                net_amount=Decimal("135000.00"),
                status=InvoiceStatus.PAID,
                payment_date=today - timedelta(days=20),
                payment_method="Wire Transfer",
                created_by=admin_id
            ),
            Invoice(
                invoice_number="INV-2026-002",
                project_id=projects[0].project_id,
                invoice_date=today - timedelta(days=15),
                due_date=today + timedelta(days=15),
                total_amount=Decimal("150000.00"),
                tax_amount=Decimal("12000.00"),
                tax_rate=Decimal("8.00"),
                net_amount=Decimal("162000.00"),
                status=InvoiceStatus.SENT,
                created_by=admin_id
            ),
            Invoice(
                invoice_number="INV-2026-003",
                project_id=projects[1].project_id,
                invoice_date=today - timedelta(days=30),
                due_date=today,
                total_amount=Decimal("100000.00"),
                tax_amount=Decimal("8000.00"),
                tax_rate=Decimal("8.00"),
                net_amount=Decimal("108000.00"),
                status=InvoiceStatus.OVERDUE,
                created_by=admin_id
            ),
            Invoice(
                invoice_number="INV-2026-004",
                project_id=projects[1].project_id,
                invoice_date=today - timedelta(days=5),
                due_date=today + timedelta(days=30),
                total_amount=Decimal("120000.00"),
                tax_amount=Decimal("9600.00"),
                tax_rate=Decimal("8.00"),
                net_amount=Decimal("129600.00"),
                status=InvoiceStatus.SENT,
                created_by=admin_id
            ),
            Invoice(
                invoice_number="INV-2026-005",
                project_id=projects[2].project_id,
                invoice_date=today,
                due_date=today + timedelta(days=30),
                total_amount=Decimal("95000.00"),
                tax_amount=Decimal("7600.00"),
                tax_rate=Decimal("8.00"),
                net_amount=Decimal("102600.00"),
                status=InvoiceStatus.DRAFT,
                created_by=admin_id
            ),
            Invoice(
                invoice_number="INV-2026-006",
                project_id=projects[3].project_id,
                invoice_date=today - timedelta(days=60),
                due_date=today - timedelta(days=30),
                total_amount=Decimal("45000.00"),
                tax_amount=Decimal("3600.00"),
                tax_rate=Decimal("8.00"),
                net_amount=Decimal("48600.00"),
                status=InvoiceStatus.PAID,
                payment_date=today - timedelta(days=35),
                payment_method="ACH",
                created_by=admin_id
            ),
        ]
        db.add_all(invoices)
        db.commit()
        print(f"Created {len(invoices)} invoices")
        
        # Create Billed Hours
        print("Creating billed hours...")
        billed_hours_list = [
            BilledHours(
                allocation_id=allocations[0].allocation_id,
                wbs_id=wbs_codes[0].wbs_id,
                invoice_id=invoices[0].invoice_id,
                hours_logged=Decimal("40"),
                date_logged=today - timedelta(days=40),
                description="Discovery phase - stakeholder interviews",
                cost_amount=Decimal("6000.00"),
                status="Billed"
            ),
            BilledHours(
                allocation_id=allocations[0].allocation_id,
                wbs_id=wbs_codes[1].wbs_id,
                invoice_id=invoices[1].invoice_id,
                hours_logged=Decimal("50"),
                date_logged=today - timedelta(days=20),
                description="Solution design and architecture",
                cost_amount=Decimal("7500.00"),
                status="Billed"
            ),
            BilledHours(
                allocation_id=allocations[1].allocation_id,
                wbs_id=wbs_codes[0].wbs_id,
                invoice_id=invoices[0].invoice_id,
                hours_logged=Decimal("35"),
                date_logged=today - timedelta(days=38),
                description="Requirements gathering",
                cost_amount=Decimal("5600.00"),
                status="Billed"
            ),
            BilledHours(
                allocation_id=allocations[2].allocation_id,
                wbs_id=wbs_codes[3].wbs_id,
                invoice_id=invoices[2].invoice_id,
                hours_logged=Decimal("60"),
                date_logged=today - timedelta(days=25),
                description="Infrastructure planning and design",
                cost_amount=Decimal("9600.00"),
                status="Billed"
            ),
            BilledHours(
                allocation_id=allocations[3].allocation_id,
                wbs_id=wbs_codes[4].wbs_id,
                invoice_id=invoices[3].invoice_id,
                hours_logged=Decimal("45"),
                date_logged=today - timedelta(days=10),
                description="Cloud migration setup",
                cost_amount=Decimal("6750.00"),
                status="Billed"
            ),
        ]
        db.add_all(billed_hours_list)
        db.commit()
        print(f"Created {len(billed_hours_list)} billed hours records")
        
        # Create Financial Insights
        print("Creating financial insights...")
        insights = [
            FinancialInsight(
                project_id=projects[0].project_id,
                insight_type="WIP_AGING",
                title="High WIP Aging",
                description="Project A has invoices over 60 days old totaling $162,000. Recommend immediate follow-up with client.",
                severity="Critical",
                recommendation="Contact client immediately to secure payment and discuss payment terms."
            ),
            FinancialInsight(
                project_id=projects[1].project_id,
                insight_type="MARGIN_EROSION",
                title="Margin Erosion Warning",
                description="Project B margin has declined 5% this month due to scope creep. Current margin is 35%, target is 40%.",
                severity="Warning",
                recommendation="Review project scope and consider change order for additional work."
            ),
            FinancialInsight(
                project_id=projects[2].project_id,
                insight_type="INVOICING_OPPORTUNITY",
                title="Invoicing Opportunity",
                description="Project C has completed 40% of work but only 25% has been invoiced. $75,000 in uninvoiced revenue available.",
                severity="Opportunity",
                recommendation="Prepare and issue invoice for completed work to improve cash flow."
            ),
        ]
        db.add_all(insights)
        db.commit()
        print(f"Created {len(insights)} financial insights")
        
        print("\n✅ Mock data successfully created!")
        print(f"\nSummary:")
        print(f"  - Projects: {len(projects)}")
        print(f"  - Resources: {len(resources)}")
        print(f"  - Resource Allocations: {len(allocations)}")
        print(f"  - WBS Codes: {len(wbs_codes)}")
        print(f"  - Invoices: {len(invoices)}")
        print(f"  - Billed Hours: {len(billed_hours_list)}")
        print(f"  - Financial Insights: {len(insights)}")
        
    except Exception as e:
        print(f"❌ Error creating mock data: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    create_mock_data()
