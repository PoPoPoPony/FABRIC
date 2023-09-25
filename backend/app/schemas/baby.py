from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import UUID, uuid4
from app.schemas.role import UserRoleEnum
from datetime import datetime


class SexType(str, Enum):
    Male = "Male"
    Female = "Female"


# 目前暫時用form讀，之後有時間可以改回來
# class BabyInfo(BaseModel):
#     baby_id: UUID = Field(default_factory=uuid4)
#     baby_name: str
#     baby_avatar: bytes
#     baby_birth: datetime
#     baby_sex: SexType
#     baby_diseases: list[str] | str

#     class Config:
#         from_attributes=True

# 不知道為啥用responsive_model有問題
# basic 只有id、avatar、name
# class BabyInfoBasic(BaseModel):
#     baby_id: UUID
#     baby_name: str
#     baby_avatar: str

#     class Config:
#         from_attributes=True