from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
from models import User, Resource, ResourceAllocation
from schemas import ResourceCreate, ResourceResponse, ResourceAllocationCreate, ResourceAllocationResponse
from services import ResourceService

router = APIRouter(prefix="/resources", tags=["resources"])

@router.get("", response_model=List[ResourceResponse])
async def get_resources(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resources = ResourceService.get_all_resources(db)
    return resources

@router.get("/{resource_id}", response_model=ResourceResponse)
async def get_resource(
    resource_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resource = ResourceService.get_resource(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.post("", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
async def create_resource(
    resource: ResourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_resource = ResourceService.create_resource(db, resource)
    return db_resource

@router.delete("/{resource_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_resource(
    resource_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resource = ResourceService.get_resource(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(resource)
    db.commit()
    return None

@router.get("/utilization/heatmap")
async def get_utilization_heatmap(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "data": [
            {"resource": "John Smith", "project_a": 40, "project_b": 20, "project_c": 0},
            {"resource": "Sarah Johnson", "project_a": 0, "project_b": 35, "project_c": 25},
            {"resource": "Mike Chen", "project_a": 30, "project_b": 10, "project_c": 40}
        ]
    }
