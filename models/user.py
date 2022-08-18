from db import db

class User_Model(db.Model):
    __tablename__ = "USERS"
    USER_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Password =db.Column(db.String(100))

    def __init__(self, Name,Password):
        self.Name = Name
        self.Password = Password

    def json(self):
        return {
            "User Id":self.USER_ID,
            "Name ":self.Name,
            "password":self.Password
        }
    @classmethod
    def user_details(cls,name=None):
        return User_Model.query.filter_by(Name =name).first()

    def add_auth(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id (cls,_id):
        return User_Model.query.filter_by(USER_ID=_id).first()