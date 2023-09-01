from sqlalchemy.orm import Session
from passlib.hash import sha512_crypt
from app.db.models import UserInfo as DB_UserInfo
from app.schemas.user import UserData


def create_user(user: UserData, db):
    DB_user = db.query(DB_UserInfo).filter(
        DB_UserInfo.user_email == user.user_email
    ).first()

    if not DB_user:
        new_user = DB_UserInfo(
            user_id=user.user_id,
            user_email=user.user_email,
            account_type=user.account_type,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)



def get_user(email: str, db):
    DB_user = db.query(DB_UserInfo).filter(
        DB_UserInfo.user_email == email
    ).first()

    return DB_user



def delete_user(user_id, db):
    delete_rows = db.query(DB_UserInfo).filter(
        DB_UserInfo.user_id == user_id
    ).delete()

    if delete_rows > 0:
        db.commit()