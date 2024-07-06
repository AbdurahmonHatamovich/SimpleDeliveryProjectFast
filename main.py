from fastapi import FastAPI
from auth_routers import auth_router


app = FastAPI()


app.include_router(auth_router)



@app.get("/")
async def get_home():
    return {"message": "Hello FastAPI"}







































# from fastapi import FastAPI, Query, Path, Body, Header, Request
# from enum import Enum
# from typing import Annotated
# from fastapi.responses import Response, RedirectResponse, JSONResponse
# from pydantic import BaseModel, Field, EmailStr
# from typing import Optional
#
#
# app = FastAPI()
#
# #run fastapi uvicorn main:app --reload
# @app.get('/api')
# async def get_info():
#     return {
#         'message': 'Welcome to the FastAPI microservice!'
#     }
#
#
# @app.get('/')
# async def root():
#     return {
#         'message': 'Hello'
#     }
#
#
# @app.get('/details/1')
# async def get_user():
#     return {
#         'user_id': 1,
#         'name': 'Bekzod',
#         'email': 'bekzod1234124@example.com'
#     }
#
#
# @app.get('/details/{user_id}')
# async def get_user(user_id: int):
#     return {
#         'user_id': user_id,
#         'name': 'John Doe',
#         'email': 'johndoe@example.com'
#     }
#
#
# class Test(str, Enum):
#     TEST_VALUE1 = 'AbdurahmonHatamovich'
#     TEST_VALUE2 = 'shaxriyorsharofov'
#     TEST_VALUE3 = 'gtrirf'
#
#
# from fastapi import FastAPI, Path, HTTPException
# from fastapi.responses import RedirectResponse, JSONResponse
#
# app = FastAPI()
#
#
#
# @app.get('/test/{test_type}')
# async def test_get(test_type: str ):
#     if test_type == 'AbdurahmonHatamovich':
#         return RedirectResponse(url='https://github.com/AbdurahmonHatamovich')
#     elif test_type == 'shaxriyorsharofov':
#         return RedirectResponse(url='https://github.com/shaxriyorsharofov')
#     elif test_type == 'gtrirf':
#         return RedirectResponse(url='https://github.com/gtrirf')
#     else:
#         raise HTTPException(status_code=404, detail='User not found')
#
#
#
#
# query_f = Query(max_length=5, min_length=2)
#
# @app.get('/cars') #http://127.0.0.1:8000/cars?search=13&date=12.05.23
# async def cars_get(
#         search: Annotated[str, query_f],
#         date: str|None=None,
#         id: Annotated[int, Path(gt=45, le=452)]|None=None):
#     return {'message': "Cars",
#             'search': search,
#             'date': date,
#             'id': id}
#
#
#
# @app.get('/cars/{cars_id}')
# async def cars_get_by_id(cars_id: int):
#     return {'message': "Cars", "cars_id": cars_id}
#
# @app.get('/headers')
# async def headers_get(request: Request):
#     user_agent = request.headers.get('user-agent')
#     accept = request.headers.get('Accept')
#     lang = request.headers.get('Accept-Language')
#     date = request.headers.get('Date')
#     return {"user_agent": user_agent,
#             'accept': accept,
#             'lang': lang,
#             'date': date}
#
#
#
# @app.get('/repo/{user_input}')
# async def redirect_to_github(user_input: str) -> Response:
#     if user_input == 'shaxriyorsharofov':
#         return RedirectResponse(url=f'https://github.com/shaxriyorsharofov')
#     elif user_input == 'gtrirf':
#         return RedirectResponse(url=f'https://github.com/gtrirf')
#     else:
#         return JSONResponse({'error': 'User not found'})
#
#
# class User(BaseModel):
#     name: str = Field(..., min_length=2, max_length=50)
#     username: str = Field(..., min_length=2, max_length=50)
#     password: str = Field(..., min_length=2, max_length=50)
#     email: EmailStr = Field(..., min_length=2, max_length=50)
#
# class Cars(BaseModel):
#     model: str = Field(..., max_length=120)
#     make: str = Field(..., min_length=1)
#     description: Optional[str] = None
#     price: float
#     user: User
#
# @app.post('/create_cars/{car_id}',response_model_exclude_unset=False)
# async def create_car(
#         car_id: Annotated[int, Path(gt=10, lt=100)],
#         car: Cars,
#         search: Annotated[str, Body()],
#
# ) -> Response:
#     return {'message': 'Cars created',
#             'car_id': car_id,
#             "car": car,
#             'user': car.user,
#             'search': search
#             }
#
#
