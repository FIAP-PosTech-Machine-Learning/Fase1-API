from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Schema for the user request."""
    email: EmailStr = Field(..., description="Email address of the user",
                            example="user@email.com")
    password: str = Field(..., description="Password for the user",
                          example="password")
    role: str = Field(...,
                      description="User role (e.g., admin, user, viewer)", example="user")


class AuthenticationSchema(BaseModel):
    """Schema for the authentication request."""
    email: EmailStr = Field(..., description="Email address of the user",
                            example="user@email.com")
    password: str = Field(..., description="Password for the user",
                          example="password")


class TokenResponseSchema(BaseModel):
    """Schema for the token response."""
    prefix: str = Field(..., description="Token prefix", example="Bearer")
    token: str = Field(..., description="Bearer token",
                       example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
