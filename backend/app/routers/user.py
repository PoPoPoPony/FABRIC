from fastapi import APIRouter, HTTPException
from app.db.database import get_db
from app.db.models import UserInfo as DBUserInfo
from app.schemas.user import UserInfo
from app.utils.account import generate_random_string, verify_account
from app.crud import user as crud_user
from app.crud import account as crud_account
from fastapi import Depends
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/api/v1/user',
    tags=["User"],
    deprecated=False
)



@router.post("/create")
def create_user(user:UserInfo, db: Session=Depends(get_db)):
    result = crud_user.create_user(user, db=db)
    if result:
        return True
    else:
        raise HTTPException(status_code=403, detail="Create User Failed!")


@router.get("/login")
def user_login(user_email: str, frontend_hashed_pwd: str, db: Session=Depends(get_db)):
    # 一個email會有兩個user_id(role)
    DB_users = crud_user.get_user(user_email, db)

    if len(DB_users) == 0:
        raise HTTPException(status_code=403, detail="User not exist!")

    verify_list = []
    for DB_user in DB_users:
        DB_account = crud_account.get_account(DB_user.user_id, db)
        verify_list.append(verify_account(DB_account.user_hashed_pwd, frontend_hashed_pwd, DB_account.salt))
    
    if verify_list.count(True) == len(verify_list):
        return True
    else:
        raise HTTPException(status_code=403, detail="User login Failed!")

