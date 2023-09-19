from fastapi import APIRouter, HTTPException, Depends, Form, File, UploadFile
from typing import Annotated, Union
from app.db.database import get_db
from app.db.models import Role as DBRole
from app.schemas.user import UserData, UserInfo
from app.schemas.baby import SexType
from app.schemas.interaction import Interaction
from app.schemas.role import UserRoleEnum
from app.crud import user as crud_user
from app.crud import account as crud_account
from app.crud import role as crud_role
from app.crud import baby as crud_baby
from app.crud import interaction as crud_interaction
from app.utils import user as utils_user
from app.utils import auth as utils_auth
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import date


router = APIRouter(
    prefix='/api/v1/baby',
    tags=["Baby"],
    deprecated=False
)


# http://localhost:8004/api/v1/baby/create
@router.post("/create")
def create_baby(
        baby_id: Annotated[UUID, Form()],
        baby_name: Annotated[str, Form()],
        baby_avatar: Annotated[UploadFile, Form()],
        baby_birth: Annotated[date, Form()],
        baby_sex: Annotated[SexType, Form()],
        baby_diseases: Annotated[Union[str, list[str]], Form()],
        user_role: Annotated[UserRoleEnum, Form()],
        current_user: UserInfo = Depends(utils_auth.get_current_user)
    ):
    # print(current_user)
    # print(baby_id)
    # print(baby_name)
    # print(type(baby_avatar))
    # print(baby_avatar)
    # print(baby_birth)
    # print(baby_sex)
    # print(baby_diseases)
    db = next(get_db())
    crud_baby.create_baby(
        baby_id,
        baby_name,
        baby_avatar,
        baby_birth,
        baby_sex,
        baby_diseases,
        current_user,
        db
    )

    interaction = Interaction(
        user_id=current_user.user_id,
        baby_id=baby_id,
        user_role=user_role
    )
    crud_interaction.create_interaction(interaction, db)


# @router.get("/role")
# def get_user_role(test: str, current_user: UserInfo = Depends(utils_auth.get_current_user)):
#     db = next(get_db())
#     roles = db.query(DBRole).filter(DBRole.user_id == current_user.user_id).all()

#     return roles
