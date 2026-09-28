from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
from models import User, Project
from schemas import ProjectCreate, ProjectResponse, ProjectList, ProjectUpdate
from services import ProjectService
from datetime import date

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("", response_model=ProjectList)
async def get_projects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    projects, total = ProjectService.get_all_projects(db, skip=skip, limit=limit)
    
    project_responses = []
    for p in projects:
        # Convert SQLAlchemy object to dict using from_attributes
        proj_dict = {
            "project_id": p.project_id,
            "name": p.name,
            "code": p.code,
            "description": p.description,
            "engagement_type": p.engagement_type,
            "start_date": p.start_date,
            "end_date": p.end_date,
            "budget": p.budget,
            "available_funding": p.available_funding,
            "client_name": p.client_name,
            "billing_manager": p.billing_manager,
            "status": p.status,
            "contract_value": p.contract_value,
            "currency": p.currency,
            "created_at": p.created_at,
            "updated_at": p.updated_at,
            "margin": 40.0 + (hash(p.project_id) % 20),  # Mock margin data
            "wip": 50000 + (hash(p.project_id) % 100000),  # Mock WIP data
            "invoicing_status": "On Track"
        }
        project_responses.append(ProjectResponse(**proj_dict))
    
    return ProjectList(
        items=project_responses,
        total=total,
        limit=limit,
        offset=skip
    )

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = ProjectService.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_project = ProjectService.create_project(db, project, current_user.user_id)
    proj_dict = {
        "project_id": db_project.project_id,
        "name": db_project.name,
        "code": db_project.code,
        "description": db_project.description,
        "engagement_type": db_project.engagement_type,
        "start_date": db_project.start_date,
        "end_date": db_project.end_date,
        "budget": db_project.budget,
        "available_funding": db_project.available_funding,
        "client_name": db_project.client_name,
        "billing_manager": db_project.billing_manager,
        "status": db_project.status,
        "contract_value": db_project.contract_value,
        "currency": db_project.currency,
        "created_at": db_project.created_at,
        "updated_at": db_project.updated_at,
        "margin": 40.0,
        "wip": 50000,
        "invoicing_status": "On Track"
    }
    return ProjectResponse(**proj_dict)

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: str,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_project = ProjectService.update_project(db, project_id, project_data)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = ProjectService.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return None

@router.patch("/{project_id}/status")
async def update_project_status(
    project_id: str,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = ProjectService.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.status = status
    db.commit()
    return {"message": "Status updated"}
