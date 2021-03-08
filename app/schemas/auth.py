from typing import Optional
from string import (ascii_lowercase as lowercase_letters,
                    ascii_uppercase as uppercase_letters,
                    punctuation as special_chars,
                    digits)
from pydantic import BaseModel, EmailStr, Field, validator

from .base import as_form


@as_form
class UserRegistration(BaseModel):
    email: EmailStr = Field(...)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    raw_password: str = Field(..., alias='password')

    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if v is not None and any(char.lower() not in lowercase_letters for char in v):
            raise ValueError('Name must contain only letters')
        return v

    @validator('raw_password')
    def validate_password(cls, v):
        min_len = 8
        if len(v) < min_len:
            raise ValueError('Password must contain at least eight characters')
        if all(char not in uppercase_letters for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if all(char not in digits for char in v):
            raise ValueError('Password must contain at least one digit')
        if all(char not in special_chars for char in v):
            raise ValueError('Password must contain at least one special character')
        return v

    class Config:
        orm_mode = True


@as_form
class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    raw_password: str = Field(..., alias='password')
