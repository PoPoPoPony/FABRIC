from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import UUID, uuid4


class AccountTypeEnum(str, Enum):
    Google = 'Google'
    Apple = 'Apple'
    Local = 'Local'


class UserRoleEnum(str, Enum):
    Mom = "Mom"
    Dad = "Dad"
    Nurse = "Nurse"


class UserInfo(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    user_email: EmailStr
    frontend_hashed_pwd: str
    account_type: AccountTypeEnum = AccountTypeEnum.Local
    user_role: UserRoleEnum

    class Config:
        from_attributes=True

# class UserLogin(BaseModel):
#     user_email: EmailStr
#     frontend_hashed_pwd: str

#     class Config:
#         from_attributes=True