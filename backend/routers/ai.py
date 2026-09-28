from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from models import User, FinancialInsight
from schemas import AIAnalysisRequest, AIAnalysisResponse, AIInsightResponse
from services import AIInsightService
from typing import List
from datetime import datetime

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/analyze-project", response_model=AIAnalysisResponse)
async def analyze_project(
    request: AIAnalysisRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Analyze a project using AI (Gemma)"""
    insights = AIInsightService.generate_project_insights(db, request.project_id)
    return AIAnalysisResponse(
        insights=[
            AIInsightResponse(
                insight_id=insight.insight_id,
                project_id=insight.project_id,
                insight_type=insight.insight_type,
                title=insight.title,
                description=insight.description,
                severity=insight.severity,
                recommendation=insight.recommendation,
                created_at=insight.created_at
            )
            for insight in insights
        ],
        generated_at=datetime.utcnow()
    )

@router.post("/detect-anomalies", response_model=List[AIInsightResponse])
async def detect_anomalies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Detect financial anomalies across portfolio"""
    # Get all insights marked as anomalies
    anomalies = db.query(FinancialInsight).filter(
        FinancialInsight.insight_type == "Anomaly"
    ).all()
    return [
        AIInsightResponse(
            insight_id=insight.insight_id,
            project_id=insight.project_id,
            insight_type=insight.insight_type,
            title=insight.title,
            description=insight.description,
            severity=insight.severity,
            recommendation=insight.recommendation,
            created_at=insight.created_at
        )
        for insight in anomalies
    ]

@router.post("/recommendations")
async def get_recommendations(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get AI-generated recommendations for a project"""
    insights = db.query(FinancialInsight).filter(
        FinancialInsight.project_id == project_id,
        FinancialInsight.insight_type == "Recommendation"
    ).all()
    return {
        "project_id": project_id,
        "recommendations": [
            {
                "title": insight.title,
                "description": insight.description,
                "recommendation": insight.recommendation
            }
            for insight in insights
        ]
    }

@router.post("/predict-risks")
async def predict_risks(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Predict financial risks for a project"""
    risks = db.query(FinancialInsight).filter(
        FinancialInsight.project_id == project_id,
        FinancialInsight.insight_type.in_(["Risk", "Prediction"])
    ).all()
    return {
        "project_id": project_id,
        "risks": [
            {
                "title": risk.title,
                "description": risk.description,
                "severity": risk.severity,
                "recommendation": risk.recommendation
            }
            for risk in risks
        ]
    }

@router.get("/insights")
async def get_insights(
    project_id: str = None,
    insight_type: str = None,
    severity: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve stored AI insights with filters"""
    query = db.query(FinancialInsight)
    
    if project_id:
        query = query.filter(FinancialInsight.project_id == project_id)
    if insight_type:
        query = query.filter(FinancialInsight.insight_type == insight_type)
    if severity:
        query = query.filter(FinancialInsight.severity == severity)
    
    insights = query.order_by(FinancialInsight.created_at.desc()).all()
    
    return {
        "insights": [
            {
                "insight_id": insight.insight_id,
                "project_id": insight.project_id,
                "type": insight.insight_type,
                "title": insight.title,
                "description": insight.description,
                "severity": insight.severity,
                "recommendation": insight.recommendation,
                "created_at": insight.created_at
            }
            for insight in insights
        ],
        "total": len(insights)
    }
