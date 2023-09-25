from sqlalchemy.orm import Session
from passlib.hash import sha512_crypt
from app.db.models import UserInfo as DBUserInfo
from app.db.models import Interaction as DBInteraction
from app.db.models import BabyInfo as DBBabyInfo
from app.schemas.user import UserData


def create_user(user: UserData, db):
    DB_user = db.query(DBUserInfo).filter(
        DBUserInfo.user_email == user.user_email
    ).first()

    if not DB_user:
        new_user = DBUserInfo(
            user_id=user.user_id,
            user_email=user.user_email,
            account_type=user.account_type,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)



def get_user(email: str, db):
    DB_user = db.query(DBUserInfo).filter(
        DBUserInfo.user_email == email
    ).first()

    return DB_user



def delete_user(user_id, db):
    delete_rows = db.query(DBUserInfo).filter(
        DBUserInfo.user_id == user_id
    ).delete()

    if delete_rows > 0:
        db.commit()

def get_user_babys(user_id, user_role, db):
    baby_ids = db.query(DBInteraction.baby_id).filter(DBInteraction.user_id == user_id, DBInteraction.user_role == user_role).all()
    if len(baby_ids)==0:
        return []
    else:
        baby_infos = []
        for baby_id in baby_ids:
            # 不知道為啥會在一個tuple裡，所以用baby_id[0]
            baby_info = db.query(DBBabyInfo).filter(DBBabyInfo.baby_id == baby_id[0]).first()
            baby_infos.append(baby_info)
    return baby_infos