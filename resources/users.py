from models.user import User_Model
from flask_restful import Resource
from flask import request

class Users(Resource):
    def get(self,name=None):
        item= User_Model.user_details(name)
        if item:
            return item.json()
        return {"Message ": "No Record Found."}

    def post(self,name):
        if User_Model.user_details(name):
            return {"Message ": "User Already Found."}
        else:
            data = request.get_json()
            item = User_Model(**data)
        try:
            item.add_auth()
        except:
            return {"Message ": "having issues."}
        return item.json()




