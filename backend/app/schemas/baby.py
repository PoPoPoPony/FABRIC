from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import UUID, uuid4
from app.schemas.role import UserRoleEnum
from datetime import datetime


class SexType(str, Enum):
    Male = "Male"
    Female = "Female"



class BabyInfo(BaseModel):
    baby_id: UUID = Field(default_factory=uuid4)
    baby_name: str
    baby_avatar: str
    baby_birth: datetime
    baby_sex: SexType

    class Config:
        from_attributes=True