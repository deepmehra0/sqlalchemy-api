import sqlite3
from flask import request
from db import db

class Student_Model(db.Model):
    __tablename__ ="STUDENTS"
    Name = db.Column(db.String(100) )
    Class = db.Column(db.String(5))
    Section = db.Column(db.String(1))
    Roll_No = db.Column(db.Integer,primary_key =True)
    Phone_Number = db.Column(db.Integer )
    Admission_No = db.Column(db.Integer)
    result = db.relationship("Result_Model",cascade="all, delete-orphan",
    lazy='dynamic',
    passive_deletes=True)


    def __init__(self,name,Class,section,Phone_Number,Admission_No):
        self.Name =name
        self.Class = Class
        self.Section = section
        self.Admission_No = Admission_No
        self.Phone_Number = Phone_Number

    def json(self):
        return {
            'Name': self.Name,
             'Class': self.Class,
             'Section': self.Section,
             'Roll_No': self.Roll_No,
             'Phone_Number': self.Phone_Number,
             'Admission_No': self.Admission_No


        }
    def get_details(admission_no):
        return Student_Model.query.filter_by(Admission_No=admission_no).first()

    def set_details( self):
        db.session.add(self)
        db.session.commit()

    def get_update(admission_no):
        if Student_Model.get_details(admission_no):
            connection = sqlite3.connect('student_database.db')
            cursor = connection.cursor()
            data = request.get_json()
            for key ,values in data.items():
                query_c =f"UPDATE STUDENTS SET {key} = '{values}' where admission_no ={admission_no}"
                result = cursor.execute(query_c)
                connection.commit()
            connection.close()
            if result:
                return({"Message ": "Record Updated Sucessfully."})
            return{{"Message ": "Having Technical Issues."}}
        return {"Message ": "No Record Found For This Admission Number."}

    def delete_rec(self):
        db.session.delete(self)
        db.session.commit()

    def get_database_details(self):
        return db.session.query(Student_Model).all()






