from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user, create_access_token
from models import User
from schemas import UserLogin, TokenResponse, UserResponse
from datetime import timedelta
import bcrypt

router = APIRouter(prefix="/auth", tags=["auth"])

def verify_bcrypt_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password using bcrypt directly, bypassing passlib issues"""
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        return False

@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    # Try to find user in database
    user = db.query(User).filter(User.email == credentials.email).first()
    if user and verify_bcrypt_password(credentials.password, user.hashed_password):
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
