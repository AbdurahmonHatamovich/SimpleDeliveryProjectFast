from pydantic import BaseModel, EmailStr, Field, validator
from typing import List, Optional
from datetime import datetime

class SignUp(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    password: str
    is_active: bool
    is_staff: bool

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "username": "abdurahmon",
                "email": "abu.doe@example.com",
                "password": "abdu200400",
                "is_active": True,
                "is_staff": False,
            }
        }

class Login(BaseModel):
    username_or_email: str
    password: str
