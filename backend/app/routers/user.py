from fastapi import APIRouter, HTTPException, Depends, Header, Query
from typing import Annotated
from app.db.database import get_db
from app.db.models import UserInfo as DBUserInfo
from app.db.models import Interaction as DBInteraction
from app.db.models import Role as DBRole
from app.schemas.user import UserData, UserInfo, UserRoleEnum
from app.crud import user as crud_user
from app.crud import account as crud_account
from app.crud import role as crud_role
from app.utils import user as utils_user
from app.utils import auth as utils_auth
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/api/v1/user',
    tags=["User"],
    deprecated=False
)



@router.post("/create")
def create_user(user:UserData, db: Session=Depends(get_db)):
    try:
        crud_user.create_user(user, db=db)
        crud_account.create_account(db, user.user_id, user.frontend_hashed_pwd)
        for user_role in user.user_roles:
            crud_role.create_role(user_id=user.user_id, role=user_role, db=db)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=403, detail="Create User Failed!")






@router.get("/role")
def get_user_role(current_user: UserInfo = Depends(utils_auth.get_current_user)):
    db = next(get_db())
    roles = db.query(DBRole).filter(DBRole.user_id == current_user.user_id).all()
    db.close()

    return roles

@router.get("/babys")
def get_user_babys(user_role: Annotated[UserRoleEnum, Query()], current_user: UserInfo = Depends(utils_auth.get_current_user)):
    db = next(get_db())
    baby_infos = crud_user.get_user_babys(current_user.user_id, user_role, db)
    db.close()

    return baby_infos





# @router.get("/login")
# def user_login(user_email: str, frontend_hashed_pwd: str, db: Session=Depends(get_db)):
#     user = utils_user.authenticate_user(db, user_email, frontend_hashed_pwd)

#     if not user:
#         raise HTTPException(status_code=403, detail="User login Failed!")
#     else:
#         return user_email

# @router.get("/login")
# def user_login(current_user: UserData = Depends(utils_auth.get_current_user), db: Session=Depends(get_db)):
#     # user = utils_user.authenticate_user(db, user_email, frontend_hashed_pwd)

#     # if not user:
#     #     raise HTTPException(status_code=403, detail="User login Failed!")
#     # else:
#     #     return user_email

#     return current_user