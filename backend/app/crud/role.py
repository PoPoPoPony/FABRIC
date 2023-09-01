from sqlalchemy.orm import Session
from app.db.models import Role as DB_RoleInfo

def create_role(user_id, role, db):
    DB_role = db.query(DB_RoleInfo).filter(
        DB_RoleInfo.user_id == user_id,
        DB_RoleInfo.user_role == role
    ).first()

    new_role = DB_RoleInfo(
        user_id=user_id,
        user_role=role
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)
