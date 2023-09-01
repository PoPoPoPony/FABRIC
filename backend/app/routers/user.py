from fastapi import APIRouter, HTTPException
from app.db.database import get_db
from app.db.models import UserInfo as DBUserInfo
from app.schemas.user import UserData
from app.crud import user as crud_user
from app.crud import account as crud_account
from app.crud import role as crud_role
from app.utils import user as utils_user
from fastapi import Depends
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



@router.get("/login")
def user_login(user_email: str, frontend_hashed_pwd: str, db: Session=Depends(get_db)):
    user = utils_user.authenticate_user(db, user_email, frontend_hashed_pwd)

    if not user:
        raise HTTPException(status_code=403, detail="User login Failed!")
    else:
        return user_email