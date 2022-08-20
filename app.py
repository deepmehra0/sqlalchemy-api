from resources.students import Students ,Database
from resources.users import Users
from resources.result import Results
from flask import Flask
from flask_restful import Api
from securtity import authenticate,identity
from flask_jwt import JWT

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///student_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='DKSRDKS'
api =Api(app)
jwt = JWT(app, authenticate, identity)
api.add_resource(Students,'/Students/database/<add_no>')
api.add_resource(Database,'/Students/database')
api.add_resource(Users,'/Students/database/users/<name>')
api.add_resource(Results,'/Students/Results/<name>')

if __name__ =="__main__":
    app.run(debug=True)