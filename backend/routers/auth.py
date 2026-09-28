from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user, create_access_token, get_password_hash, verify_password
from models import User
from schemas import UserLogin, TokenResponse, UserResponse
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

# Demo user
DEMO_USER = {
    "email": "admin@company.com",
    "password_hash": "$2b$12$kZLV1gVYCF4o1pj7SkKlK.Oj.RZU2XUbYplJhNGGlRvLxFVqB2N8u",  # bcrypt hash of "password123"
    "full_name": "Admin User",
    "role": "Admin"
}

@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    # Check demo credentials
    if credentials.email == DEMO_USER["email"]:
        if verify_password(credentials.password, DEMO_USER["password_hash"]):
            access_token = create_access_token(
                data={"sub": "demo-user-id"},
                expires_delta=timedelta(hours=24)
            )
            return TokenResponse(
                access_token=access_token,
                user=UserResponse(
                    user_id="demo-user-id",
                    email=DEMO_USER["email"],
                    full_name=DEMO_USER["full_name"],
                    role=DEMO_USER["role"]
                )
            )
    
    # Try to find user in database
    user = db.query(User).filter(User.email == credentials.email).first()
    if user and verify_password(credentials.password, user.hashed_password):
        access_token = create_access_token(
            data={"sub": user.user_id},
            expires_delta=timedelta(hours=24)
        )
        return TokenResponse(
            access_token=access_token,
            user=UserResponse(
                user_id=user.user_id,
                email=user.email,
                full_name=user.full_name,
                role=user.role
            )
        )
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password"
    )

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return UserResponse(
        user_id=current_user.user_id,
        email=current_user.email,
        full_name=current_user.full_name,
        role=current_user.role
    )

@router.post("/logout")
async def logout():
    return {"message": "Logout successful"}
