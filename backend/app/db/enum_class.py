from enum import Enum


class AccountType(Enum):
    Google = "google"
    Apple = "apple"
    Local = "local"


class UserRole(Enum):
    Mom = "mom"
    Dad = "dad"
    # Nurse = "nurse"

class SexType(Enum):
    Male = "male"
    Female = "female"