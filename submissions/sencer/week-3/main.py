from fastapi import FastAPI,HTTPException,Depends,status
from datetime import datetime, timezone
import requests
from pydantic import BaseModel
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./hsd_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    age = Column(Integer,index=True)

class UserCreate(BaseModel):
    name:str
    age:int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    current_time = datetime.now(timezone.utc)
    return {"message":"Servisimiz ve ben aktif olarak çalışıyoruz!!",
            "timestamp": current_time}

@app.get("/user/{id}")
def get_user_info(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    user_data = response.json()
    return user_data

@app.post("/users/")
def create_user(user:UserCreate,db:Session = Depends(get_db)):
    yeni_kullanici = UserDB(name=user.name,age=user.age)
    db.add(yeni_kullanici)
    db.commit()
    db.refresh(yeni_kullanici)
    return yeni_kullanici

@app.get("/users/{user_id}")
def read_user(user_id:int,db:Session = Depends(get_db)):
    bulunan_kullanici = db.query(UserDB).filter(UserDB.id == user_id).first()
    if bulunan_kullanici is None:
        raise HTTPException(status_code=404,detail="Kullanici Bulunamadi")
    return bulunan_kullanici