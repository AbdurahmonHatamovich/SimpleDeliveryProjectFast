from fastapi import APIRouter
from database import SessionLocal,engine
from schemas import SignUp,Login
from models import User
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi import status
import datetime
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from fastapi_jwt_auth import AuthJWT

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.get('/')
async def get_auth():
    return {'message': 'Authentication Successful!'}



@auth_router.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup(user : SignUp):
    session = SessionLocal()

    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return {'message': 'Email already registered!'}
    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return {'message': 'Username already registered!'}
    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff

    )
    session.add(new_user)
    return {'message': 'User created!', 'new_user': new_user}


async def login(user: Login, Authorize: AuthJWT=Depends()):
    session = SessionLocal()
    db_user = session.query(User).filter(
        or_(
            User.username == user.username_or_email,
            User.email == user.username_or_email
        )
    ).first()

    if db_user and check_password_hash(db_user.password, user.password):
        access_lifetime = datetime.timedelta(minutes=60)
        refresh_lifetime = datetime.timedelta(days=3)
        access_token = Authorize.create_access_token(subject=db_user.username, expires_time=access_lifetime)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username, expires_time=refresh_lifetime)
        token = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        response_data = {
            'status': status.HTTP_200_OK,
            'message': "Successfully logged in",
            'token': token
        }
        return response_data
    raise HTTPException(status=status.HTTP_400_BAD_REQUEST, detail='Invalid username, email or password')