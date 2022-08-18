from flask_restful import Resource
from models.student_database import Student_Model
from flask import request

class Students(Resource):
    def get(self,add_no):
        item =Student_Model.get_details(add_no)
        if item:
            return item.json()
        return {"Message ": "No Record Found."}
    def post(self,add_no):
        print(add_no)
        if Student_Model.get_details(add_no):
            return {"Message ": "Record Already Found."}
        else:
           data = request.get_json()
           item = Student_Model(data['Name'],data['Class'],data['Section'],data['Phone_Number'],add_no)
        try:
            item.set_details()
        except:
            return {"Message ": "having issues."}
        return item.json()
    def put(self,add_no):
        return Student_Model.get_update(add_no)
    def delete(self,add_no):
        item = Student_Model.get_details(add_no)
        if item:
            item.delete_rec()
            return {"Message ": "Record Deleted."}
        return {"Message ": "having Issues with Deletion."}

class Database(Resource):
    def get(self):
        item = Student_Model.get_database_details(self)
        k=[]
        for i in item:
            print( {'item':i.json()})
            k.append(i.json())
        return {"Details ":k}





