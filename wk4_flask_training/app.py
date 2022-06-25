import os
from flask import Flask
from resource.user import UserRegister, UserLogin
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tobi:1234@localhost:5432/movies'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =  False

# os.environ.get['JWT_SECRET_KEY']

print( "secret Key",os.getenv('JWT_SECRET_KEY'))
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

jwt = JWTManager(app)
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()


api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)