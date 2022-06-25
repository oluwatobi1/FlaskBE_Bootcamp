
from flask_restful import Resource, reqparse
from models.user import UserModel
from utils.helper import validate_email
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

from werkzeug.security import generate_password_hash, check_password_hash


parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help = "This field cannot be blank")
parser.add_argument("password", type=str, required=True, help = "This field cannot be blank")



class UserRegister(Resource):
    
    def post(self):
        # get details
        data = parser.parse_args()
        # check if user is register

        # validate_email(data['email'])

        user = UserModel.find_by_name(data['username'])
        if user:
            return {"message":"user already exist"}, 400

        data['password'] = generate_password_hash(data['password'])
    
        user = UserModel(**data)
        try:
            UserModel.create(user)
        except Exception as exc:
            return {"error": "Registration Failed"}, 400

        return {"message":"user created"}, 201

   



class UserLogin(Resource):
    
    def post(self):
        # log user in
        data = parser.parse_args()
        user = UserModel.find_by_name(data["username"])

        if not user:
            return {"error": "invalid Credentials"}, 401
        
        if not check_password_hash(user.password, data['password']):
            return {"error": "invalid Credentials"}, 401

        access_token = create_access_token(identity= user.username, fresh=True)
        refresh_token  = create_refresh_token(user.username)

        return {
            "access":access_token,
            "refresh": refresh_token
        }
    @jwt_required(fresh=True)
    def get(self):
        return {
            'status':"You are logged in"            
        }


