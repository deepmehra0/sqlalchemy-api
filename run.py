from db import db
from main import app

db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()
