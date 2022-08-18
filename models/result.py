from db import db

class Result_Model(db.Model):

    __tablenmae__ ="Result"
    Id =db.Column(db.Integer ,primary_key ="True")
    Subject =db.Column(db.String(40))
    Marks =db.Column(db.Float(precision =2))
    Roll_No = db.Column(db.Integer ,db.ForeignKey('STUDENTS.Roll_No') )
    student = db.relationship("Student_Model")

    def __int__(self,Subject,Marks,Roll_no):
        self.Subject =Subject
        self.Marks =Marks
        self.Roll_No =Roll_no

    def json(self):
        return {
            "Result_Id": self.Id,
            "Subject":self.Subject,
            "Marks": self.Marks
        }

    def get_details(Subject,Roll_No):
        return Result_Model.query.filter_by(Subject=Subject , Roll_No=Roll_No).first()

    def set_details(self):
        db.session.add(self)
        db.session.commit()

