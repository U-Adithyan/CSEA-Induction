from .database import db

class User(db.Model):
    __tablename__="user"
    user_id=db.Column(db.Integer,autoincrement=True,unique=True,primary_key=True)
    name=db.Column(db.String,nullable=False)
    dob=db.Column(db.String,nullable=False)
    roll=db.Column(db.String,nullable=False)
    branch=db.Column(db.String,nullable=False)
    mobile=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String,nullable=False)
    sex=db.Column(db.String,nullable=False)
    