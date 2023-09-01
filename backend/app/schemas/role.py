from pydantic import BaseModel
from enum import Enum



class UserRoleEnum(str, Enum):
    Mom = "Mom"
    Dad = "Dad"
    Nurse = "Nurse"