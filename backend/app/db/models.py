import uuid
from .database import Base
from .enum_class import AccountType, UserRole
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float, Enum
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from passlib.hash import sha512_crypt







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