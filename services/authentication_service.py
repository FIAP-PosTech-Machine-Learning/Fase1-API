import os
from fastapi import HTTPException
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from schemas import TokenResponseSchema
from db.crud import get_user

SECRET_KEY = os.getenv("SECRET_KEY", default="your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password context for hashing passwords securely
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to create access token (JWT)
def create_access_token(data: dict):
    to_encode = data.copy()

    if 'user_id' not in to_encode:
        raise HTTPException(status_code=400 ,detail="user_id is missing from the token payload")

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    prefix = "Bearer"
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return TokenResponseSchema(prefix=prefix, token=token)

# Function to validate the JWT
def validate_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return HTTPException(status_code=401, detail='Invalid token') 

# Password hashing and verification functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def validate_user(data, ip):
    # Convert the email to lowercase when querying the repository
    user = await get_user(email=data.email.lower())

    # Check if the user was found
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Check if the user is active
    if not user.is_active:
        raise HTTPException(status_code=403, detail="User account is inactive")

    # Check if the password is valid (case-sensitive)
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Validate the IP address
    # if user.ip_address == ip:
    #     # Generate the JWT token
    return create_access_token({"user_id": user.id})