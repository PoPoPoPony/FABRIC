import uuid
from .database import Base
from .enum_class import AccountType, UserRole, SexType
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float, Enum, Date, ARRAY
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from passlib.hash import sha512_crypt
import base64





class AccountInfo(Base):
    __tablename__="account_info"
    user_id = Column(UUID(as_uuid=True), ForeignKey("user_info.user_id", ondelete="CASCADE"), primary_key=True, unique=True, nullable=False, )
    user_hashed_pwd = Column(String, nullable=False)
    salt = Column(String, nullable=False)

    def __init__(self, user_id, user_hashed_pwd, salt):
        self.user_id = user_id
        self.user_hashed_pwd = user_hashed_pwd
        self.salt = salt


class UserInfo(Base):
    __tablename__="user_info"
    user_id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    user_email = Column(EmailType, nullable=False)
    account_type = Column(Enum(AccountType), nullable=False, default=AccountType.Local)

    roles = relationship("Role", backref='user_info')
    baby_ids = relationship("Interaction", backref='user_info')

    def __init__(self, user_id, user_email, account_type):
        self.user_id = user_id
        self.user_email = user_email
        self.account_type = account_type


class Role(Base):
    __tablename__="role"
    user_id = Column(UUID(as_uuid=True), ForeignKey("user_info.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    user_role = Column(Enum(UserRole), primary_key=True, nullable=False)

    def __init__(self, user_id, user_role):
        self.user_id = user_id
        self.user_role = user_role


class BabyInfo(Base):
    __tablename__="baby_info"
    baby_id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    baby_name = Column(String, nullable=False)
    # 存avatar的路徑
    baby_avatar = Column(String, nullable=False)
    baby_birth = Column(Date, nullable=False)
    baby_sex = Column(Enum(SexType), nullable=False)
    # 應為disease.disease_id的foreign key，暫省略
    baby_diseases = Column(ARRAY(Integer), nullable=True)

    carers = relationship("Interaction", backref='baby_info')

    def __init__(self, baby_id, baby_name, baby_avatar, baby_birth, baby_sex, baby_diseases):
        self.baby_id = baby_id
        self.baby_name = baby_name
        self.baby_avatar = baby_avatar
        self.baby_birth = baby_birth
        self.baby_sex = baby_sex
        self.baby_diseases = baby_diseases


class Interaction(Base):
    __tablename__="interaction"

    user_id = Column(UUID(as_uuid=True), ForeignKey("user_info.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    baby_id = Column(UUID(as_uuid=True), ForeignKey("baby_info.baby_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    user_role = Column(Enum(UserRole), primary_key=True, nullable=False)

    def __init__(self, user_id, baby_id, user_role):
        self.user_id = user_id
        self.baby_id = baby_id
        self.user_role = user_role


class Disease(Base):
    __tablename__="disease"

    disease_id = Column(String, primary_key=True, nullable=False)
    disease_name = Column(String, nullable=False)

    def __init__(self, disease_id, disease_name):
        self.disease_id = disease_id
        self.disease_name = disease_name





