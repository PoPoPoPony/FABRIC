from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import UUID, uuid4
from app.schemas.role import UserRoleEnum
from datetime import datetime


class SexType(str, Enum):
    Male = "Male"
    Female = "Female"


# file -> baby_avatar: str(暫時不確定怎麼修改element-ui上的設定)
# class BabyInfo(BaseModel):
#     baby_id: UUID = Field(default_factory=uuid4)
#     baby_name: str
#     file: bytes
#     baby_birth: datetime
#     baby_sex: SexType
#     baby_diseases: list[str] | str

#     class Config:
#         from_attributes=True