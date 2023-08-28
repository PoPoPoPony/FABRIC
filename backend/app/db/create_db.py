from database import Base, engine
from models import UserInfo


print("Creating database...")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("Success!")