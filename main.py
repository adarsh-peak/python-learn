from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from models import User
from schema import UserSchema, UserCreateSchema
from database import engine
app = FastAPI()
session = Session(bind=engine)

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users 

@app.post("/users", response_model=UserCreateSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    # if user.id:
    #     # update existing user 
    #     pass
    # else:
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    
    db.commit()
    db.refresh(new_user) 
    return new_user