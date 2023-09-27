from fastapi import APIRouter, HTTPException, Depends, Form, File, UploadFile, Query, status, Body
from fastapi.responses import FileResponse
from typing import Annotated, Union, Optional
from app.db.database import get_db
from app.db.models import Role as DBRole
from app.db.models import Interaction as DBInteraction
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
import os


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
        baby_diseases: Annotated[str, Form()],
        user_role: Annotated[UserRoleEnum, Form()],
        current_user: UserInfo = Depends(utils_auth.get_current_user)
    ):

    db = next(get_db())
    # baby_desease = -1 時代表沒有遺傳性疾病
    if baby_diseases == '-1':
        baby_diseases = ["-1"]
    else:
        baby_diseases = baby_diseases.split(',')

    # check if interaction exist
    is_interaction = crud_interaction.check_interaction(baby_id, current_user.user_id, user_role, db)
    print(is_interaction)
    if is_interaction:
        # update baby info
        crud_baby.update_baby(
            baby_id,
            baby_name,
            baby_avatar,
            baby_birth,
            baby_sex,
            baby_diseases,
            current_user,
            db
        )
    else:
        # create baby info and interaction between user and baby
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
    db.close()


# @router.post("/temp")
# # Union[List[str], None] = Query(default=None)
# # 
# def get_user_role(test: Annotated[str, Form()]):
#     for i in test:
#         print(i)

#     return test


@router.get("/avatar/{file_name}")
def get_avatar(
        file_name: str,
    ):

    path = os.path.join("app", "public", "avatar", file_name)

    if os.path.exists(path):
        return FileResponse(path)
    else:
        exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="baby's avatar not found!",
        )
        raise exception
    

@router.get("/info")
def get_babys_info(
        baby_ids: Annotated[list[UUID], Query()],
        user_role: Annotated[UserRoleEnum, Query()],
        current_user: UserInfo = Depends(utils_auth.get_current_user)
    ):

    # retv = []

    # db = next(get_db())
    # baby_infos = crud_user.get_user_babys(current_user.user_id, user_role, db)
    # db.close()
    # for baby_info in baby_infos:
    #     if baby_info.baby_id in baby_ids:
    #         retv.append(baby_info)
    #     else:
    #         retv.append(None)

    # return retv
    db = next(get_db())
    for idx in range(len(baby_ids)):
        is_interaction = crud_interaction.check_interaction(baby_ids[idx], current_user.user_id, user_role, db)
        if not is_interaction:
            baby_ids[idx] = None
    
    baby_infos = crud_baby.get_babys(baby_ids, db)
    db.close()

    return baby_infos
