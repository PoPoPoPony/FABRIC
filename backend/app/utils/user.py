from app.crud import account as crud_account
from app.crud import user as crud_user
from app.utils.account import verify_account



def authenticate_user(db, user_email, frontend_hashed_pwd):
    DB_user = crud_user.get_user(user_email, db=db)
    
    if not DB_user:
        return False
    
    DB_account = crud_account.get_account(DB_user.user_id, db)

    if not DB_account:
        return False

    result = verify_account(DB_account.user_hashed_pwd, frontend_hashed_pwd, DB_account.salt)
    
    if result:
        return DB_user
    else:
        return False