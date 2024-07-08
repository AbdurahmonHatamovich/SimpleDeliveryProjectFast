from pydantic import BaseModel
from typing import List, Optional

class SignUp(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
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
    username: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = '24084df22271e59fa98e57a3ae3cf18315e80c8dbb5748b8792ce4db86f73f6'