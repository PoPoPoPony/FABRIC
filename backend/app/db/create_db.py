from database import Base, engine, SessionLocal
from models import Disease


print("Creating database...")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


print("Success!")


print("Adding default rows...")

default_diseases = [
    Disease(0, "高血壓"),
    Disease(1, "糖尿病"),
    Disease(2, "心臟疾病"),
    Disease(3, "氣喘"),
    Disease(4, "唐氏症"),
    Disease(5, "高血脂症"),
    Disease(6, "胃癌"),
    Disease(7, "乳癌"),
    Disease(8, "白化症"),
    Disease(9, "色盲"),
]

session = SessionLocal()
session.add_all(default_diseases)
session.commit()
session.close()


print("Success!")