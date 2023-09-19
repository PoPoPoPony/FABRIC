from fastapi import UploadFile
from uuid import UUID
from sqlalchemy.orm import Session
from app.db.models import BabyInfo as DB_BabyInfo
from app.schemas.user import UserData
from datetime import date
from app.schemas.baby import SexType
from typing import Union
import shutil


def create_baby(
        baby_id: UUID,
        baby_name: str,
        baby_avatar: bytes,
        baby_birth: date,
        baby_sex: SexType,
        baby_diseases: Union[str, list[str]],
        curreny_user: UserData,
        db
    ):
    DB_baby = db.query(DB_BabyInfo).filter(
        DB_BabyInfo.baby_id == baby_id
    ).first()

    if not DB_baby:
        # 將baby_avatar的圖片存到 backend/app/public
        with open(f'app/public/avatar/{curreny_user.user_id}_{baby_id}.jpg', 'wb') as file:
            # shutil.copyfileobj(baby_avatar.file, file) 
            
            avatar = baby_avatar.file.read()
            file.write(avatar)


        new_baby = DB_BabyInfo(
            baby_id=baby_id,
            baby_name=baby_name,
            baby_avatar=f"{curreny_user.user_id}_{baby_id}.jpg",
            baby_birth=baby_birth,
            baby_sex=baby_sex,
            baby_diseases=baby_diseases
        )

        db.add(new_baby)
        db.commit()
        db.refresh(new_baby)