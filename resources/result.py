from flask_restful import Resource
from models.result import Result_Model
from flask import request

class Results(Resource):
    def get(self,name):
        data =name.split(' ')
        print(data)
        item =Result_Model.get_details(data[0],data[1])
        if item:
            return item.json()
        return {"Message ": "No Record Found."}
    def post(self,name):
        data1 = name.split(' ')
        print(data1)
        if Result_Model.get_details(data1[0], data1[1]):
            return {"Message ": "Record Already Found."}
        else:
           data = request.get_json()
           print(data)
           item = Result_Model(**data)
        try:
            item.set_details()
        except:
            return {"Message ": "having issues."}
        return item.json()