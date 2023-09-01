from sqlalchemy.orm import Session
from app.utils.account import encrypt
from app.db.models import AccountInfo as DB_AccountInfo


# encrypt user pwd and creat instance
def create_account(db:Session, user_id, frontend_hashed_pwd):
    backend_hashed_pwd, salt = encrypt(frontend_hashed_pwd)
    backend_hashed_pwd = backend_hashed_pwd.split("$")[-1] # 只取密碼部分


    new_pwd = DB_AccountInfo(
        user_id=user_id,
        user_hashed_pwd=backend_hashed_pwd,
        salt=salt
    )

    db.add(new_pwd)
    db.commit()
    db.refresh(new_pwd)

# get user pwd and salt
def get_account(user_id, db):
    DB_account = db.query(DB_AccountInfo).filter(DB_AccountInfo.user_id == user_id).first()

    return DB_account