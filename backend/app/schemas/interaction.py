from pydantic import BaseModel
from uuid import UUID
from app.schemas.role import UserRoleEnum


class Interaction(BaseModel):
    user_id: UUID
    baby_id: UUID
    user_role: UserRoleEnum

    class Config:
        from_attributes=True