from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserDTO(BaseModel):
    id: Optional[int] = None
    first_name: str = Field(min_length=2, max_length=255)
    last_name: str = Field(min_length=2, max_length=255)
    email: EmailStr
