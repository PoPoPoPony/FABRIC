from sqlalchemy.orm import Session
from passlib.hash import sha512_crypt
from app.db.models import UserInfo as DB_UserInfo
from app.schemas.user import UserInfo
from app.crud import account as crud_account

def create_user(user: UserInfo, db):
    DB_user = db.query(DB_UserInfo).filter(
        DB_UserInfo.user_email == user.user_email,
        DB_UserInfo.user_role == user.user_role
    ).first()

    if DB_user:
        return False

    new_user = DB_UserInfo(
        user_id=user.user_id,
        user_email=user.user_email,
        account_type=user.account_type,
        user_role=user.user_role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    crud_account.create_account(db, user.user_id, user.frontend_hashed_pwd)

    return True


def get_user(email: str, db):
    DB_user = db.query(DB_UserInfo).filter(
        DB_UserInfo.user_email == email
    ).all()

    return DB_user




# def user_login_verify(user: UserLogin, db):
#     DB_user = db.query(DB_UserInfo).filter(
#         DB_UserInfo.user_email==user.user_email
#     ).first()
