from enum import Enum


class AccountType(Enum):
    Google = "Google"
    Apple = "Apple"
    Local = "Local"


class UserRole(Enum):
    Mom = "Mom"
    Dad = "Dad"
    # Nurse = "nurse"

class SexType(Enum):
    Male = "Male"
    Female = "Female"