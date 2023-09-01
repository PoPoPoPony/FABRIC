from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import UUID, uuid4
from app.schemas.role import UserRoleEnum


class AccountTypeEnum(str, Enum):
    Google = 'Google'
    Apple = 'Apple'
    Local = 'Local'



class UserInfo(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    user_email: EmailStr
    account_type: AccountTypeEnum
    
    class Config:
        from_attributes=True

class UserData(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    user_email: EmailStr
    frontend_hashed_pwd: str
    account_type: AccountTypeEnum = AccountTypeEnum.Local
    user_roles: list[UserRoleEnum]

    class Config:
        from_attributes=True

# class UserLogin(BaseModel):
#     user_email: EmailStr
#     frontend_hashed_pwd: str

#     class Config:
#         from_attributes=True