import os
from fastapi import APIRouter
from db import crud, SessionLocal
from services import authentication_service as service
from schemas import AuthenticationSchema as Schema
from schemas import UserSchema

router = APIRouter(
    tags=[os.path.basename(__file__).replace("public_", "").replace(
        "_router.py", "").replace("_", " ").title()],
    prefix=f"/{os.path.basename(__file__).replace('public_', '').replace('_router.py', '')}",
)


@router.post('/')
async def authentication(data: Schema):
    '''
    Authentication route to obtain a bearer token
    '''
    return await service.validate_user(data)


@router.post('/register')
async def register(data: UserSchema):
    '''
    Registration route to create a new user
    '''
    db = SessionLocal()
    return await crud.create_user(db, data)
