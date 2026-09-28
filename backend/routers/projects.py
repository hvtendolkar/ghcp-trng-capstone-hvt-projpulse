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
    
    return ProjectList(
        items=[
            ProjectResponse(
                **p.__dict__,
                margin=40.0 + (hash(p.project_id) % 20),  # Mock margin data
                wip=50000 + (hash(p.project_id) % 100000)  # Mock WIP data
            )
            for p in projects
        ],
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
    return ProjectResponse(**db_project.__dict__)

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
