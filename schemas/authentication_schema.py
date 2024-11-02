from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Schema for the user request."""
    email: EmailStr = Field(..., description="Email address of the user", example="user@email.com")
    password: str = Field(..., description="Password for the user", example="password")
    role: str = Field(..., description="User role (e.g., admin, user, viewer)", example="user")
    ip_address: str = Field(..., description="IP address allowed for this user", example="127.0.0.1")
    
class AuthenticationSchema(BaseModel):
    """Schema for the authentication request."""
    email: EmailStr = Field(..., description="Email address of the user", example="user@email.com")
    password: str = Field(..., description="Password for the user", example="password")
    
class TokenResponseSchema(BaseModel):
    """Schema for the token response."""
    prefix: str = Field(..., description="Token prefix", example="Bearer")
    token: str = Field(..., description="Bearer token", example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")